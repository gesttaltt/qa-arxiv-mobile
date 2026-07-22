# Appium Setup Guide

Mobile UI automation for the arXiv Papers mobile app (React Native, Android/iOS).

---

## Prerequisites

| Tool | Version | Install |
|---|---|---|
| Node.js | 20 LTS or later (CI uses 24) | https://nodejs.org |
| Appium | 2.x | `npm install -g appium` |
| UiAutomator2 driver | latest | `appium driver install uiautomator2` |
| Android Studio + SDK | latest stable | https://developer.android.com/studio |
| Java JDK | 17 or 21 | https://adoptium.net |
| Python | 3.12 | https://python.org |
| Python deps | (see below) | `pip install -r automation/requirements.txt` |

**macOS only (iOS):**

| Tool | Install |
|---|---|
| Xcode + Command Line Tools | `xcode-select --install` |
| XCUITest driver | `appium driver install xcuitest` |
| ios-deploy | `npm install -g ios-deploy` |

---

## 1. Build the APK

```bash
# Clone the app if not already done
bash setup-app.sh

cd /tmp/arxiv-mobile-testing/arxiv-papers-mobile

# Android debug build
cd android
./gradlew assembleDebug
# APK output: android/app/build/outputs/apk/debug/app-debug.apk
```

---

## 2. Start an Android Emulator

```bash
# List available AVDs
emulator -list-avds

# Start one (replace Pixel_6_API_33 with your AVD name)
emulator -avd Pixel_6_API_33 &

# Verify the device is visible to ADB
adb devices
```

---

## 3. Start the Appium Server

```bash
appium --log appium.log
```

Confirm the server is running:

```bash
curl http://127.0.0.1:4723/status
```

---

## 4. Configure Environment Variables

The test suite reads three optional env vars. Defaults target the fixture APK checked into the
repo (`automation/appium/arxiv-papers-v1.0.apk`), so `pytest -m appium` works against a local
emulator with zero configuration — override `ARXIV_APK_PATH` only if testing a different build:

| Variable | Default | Description |
|---|---|---|
| `APPIUM_SERVER_URL` | `http://127.0.0.1:4723` | Appium server address |
| `ARXIV_APK_PATH` | `automation/appium/arxiv-papers-v1.0.apk` (repo-relative) | Absolute path to the APK to install |
| `ANDROID_DEVICE_NAME` | `Android Emulator` | Name matching `adb devices` output |

Example (only needed to point at a different build than the checked-in fixture APK):

```bash
export APPIUM_SERVER_URL="http://127.0.0.1:4723"
export ARXIV_APK_PATH="/tmp/arxiv-mobile-testing/arxiv-papers-mobile/android/app/build/outputs/apk/debug/app-debug.apk"
export ANDROID_DEVICE_NAME="emulator-5554"
```

---

## 5. Validate Locators with Appium Inspector

Before the first test run, open **Appium Inspector** and inspect the running app to confirm
the `accessibilityLabel` values match the locators in the test files.

```
Download: https://github.com/appium/appium-inspector/releases
```

Connect with these capabilities in Appium Inspector:

```json
{
  "platformName": "Android",
  "appium:deviceName": "Android Emulator",
  "appium:app": "/path/to/app-debug.apk",
  "appium:automationName": "UiAutomator2"
}
```

Key elements to verify:

| Element | Expected locator strategy | Expected value |
|---|---|---|
| Search text input (Home screen) | `accessibility id` | `homeSearchInput` |
| Search submit | Android keycode | `driver.press_keycode(66)` (Enter — fires `onSubmitEditing`) |
| Result cards | `xpath` | `//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[.//android.widget.TextView]` |
| Downloaded article items | `accessibility id` | `downloadedArticle` |
| DOWNLOADED tab | `xpath` | `//android.widget.TextView[@text='DOWNLOADED']` |

Locators confirmed via two methods:

1. **App source code** (`github.com/lopespm/arxiv-papers-mobile`) — `homeSearchInput` and `downloadedArticle` are real `testID` props in the React Native source.
2. **BrowserStack `page_source` analysis** — `driver.page_source` dumped on Samsung Galaxy S22 / Android 12 confirmed that `TouchableNativeFeedback` (NativeBase 2.x) does **not** expose `clickable="true"` on Android 12. Result cards are located by DOM position: second-level `ViewGroup` children of the `ScrollView` that contain at least one `TextView`.

---

## 6. Run the Appium Tests

```bash
# Run only Appium-marked tests
pytest automation/tests/appium/ -m appium -v

# Run a single file
pytest automation/tests/appium/test_search_smoke.py -m appium -v

# Run with HTML report
pytest automation/tests/appium/ -m appium --html=test-results/appium-report.html -v
```

To **exclude** Appium tests from the standard suite (they require a running device):

```bash
pytest automation/tests/ -m "not appium" -v
```

---

## 7. CI/CD Integration (GitHub Actions + Azure Pipelines)

### GitHub Actions (`.github/workflows/ci.yml`)

The `test-appium` job runs automatically on every push to `main` or `develop`, against a
**local Android emulator** (`reactivecircus/android-emulator-runner`, API 33, Pixel 6) started
directly in the CI runner — no external account or secrets required. The runner script lives at
`automation/ci/run_appium_emulator.sh` rather than inline in the workflow YAML, and the job has
`timeout-minutes: 15` as a hard ceiling.

> **History and current disclosure:** this is a retry. The job originally ran against
> **BrowserStack App Automate**, whose free trial expired 2026-07-08. A 2026-07-09 attempt to
> replace it with a local Android emulator failed twice in CI — the first on missing KVM
> permissions, the second booted the emulator fine (~2m17s) but then hung for the full 6-hour job
> timeout because a shell syntax error in an inline test-runner script left the job stuck in
> cleanup instead of failing fast — leaving `main`'s CI red for 5 days. It was reverted to
> BrowserStack on 2026-07-14. This retry (2026-07-22) fixes the root cause — the script is now a
> standalone file, checked with `bash -n`/`dash -n` before commit — and adds `timeout-minutes` so
> a repeat bug fails in minutes, not hours. See `docs/QA_AUDIT.md` §3.7 for the full timeline.
> **Unconfirmed until a real CI run has been observed** — check the Actions tab rather than
> trusting this doc. To run against BrowserStack instead (e.g. for real-device validation), set
> `BROWSERSTACK=true` plus the three secrets below and point the job at that path manually — it is
> no longer wired into `ci.yml` by default.

| Secret (optional, BrowserStack path only) | Description |
|---|---|
| `BROWSERSTACK_USERNAME` | BrowserStack account username |
| `BROWSERSTACK_ACCESS_KEY` | BrowserStack access key |
| `BROWSERSTACK_APP_ID` | `bs://` app ID returned after uploading the APK |

Upload the APK to BrowserStack once and store the returned `bs://` ID as the secret:

```bash
curl -u "USER:KEY" \
  -X POST "https://api-cloud.browserstack.com/app-automate/upload" \
  -F "file=@automation/appium/arxiv-papers-v1.0.apk"
```

### Azure Pipelines (`automation/ci/azure-pipelines.yml`)

The `AppiumSmoke` stage is **opt-in** — it only runs when the pipeline variable
`BROWSERSTACK_ENABLED` is set to `true`. Set the same three values as pipeline variables:
`BROWSERSTACK_USERNAME`, `BROWSERSTACK_ACCESS_KEY`, `BROWSERSTACK_APP_ID`.

```bash
az pipelines run --name <pipeline-name> \
  --variables BROWSERSTACK_ENABLED=true \
              BROWSERSTACK_USERNAME=<user> \
              BROWSERSTACK_ACCESS_KEY=<key> \
              BROWSERSTACK_APP_ID=bs://<id>
```

---

## 8. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `WebDriverException: Connection refused` | Appium server not running | Run `appium` and retry |
| `Device not found` | Emulator not started | `emulator -avd <AVD_NAME> &` then `adb devices` |
| `App not installed` | Wrong APK path | Verify `ARXIV_APK_PATH` points to the built APK |
| Element not found | Locator mismatch | Inspect live app with Appium Inspector |
| `implicitly_wait` timeouts on slow device | Emulator is under-resourced | Increase `options.new_command_timeout` in `conftest.py` |
