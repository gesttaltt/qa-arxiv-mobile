# Appium Setup Guide

Mobile UI automation for the arXiv Papers mobile app (React Native, Android/iOS).

---

## Prerequisites

| Tool | Version | Install |
|---|---|---|
| Node.js | 18 LTS or later | https://nodejs.org |
| Appium | 2.x | `npm install -g appium` |
| UiAutomator2 driver | latest | `appium driver install uiautomator2` |
| Android Studio + SDK | latest stable | https://developer.android.com/studio |
| Java JDK | 11 or 17 | https://adoptium.net |
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

The test suite reads three optional env vars — defaults target a local emulator build:

| Variable | Default | Description |
|---|---|---|
| `APPIUM_SERVER_URL` | `http://127.0.0.1:4723` | Appium server address |
| `ARXIV_APK_PATH` | `/tmp/…/app-debug.apk` | Absolute path to the compiled APK |
| `ANDROID_DEVICE_NAME` | `Android Emulator` | Name matching `adb devices` output |

Example:

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
| Search text input | `accessibility id` | `search-input` |
| Search submit button | `accessibility id` | `search-button` |
| Result cards | `xpath` | `//android.view.ViewGroup[@clickable='true']` |
| Favorite/star button | `accessibility id` | `favorite-button` |
| Favorites tab | `accessibility id` | `favorites-tab` |

If the app does not expose `accessibilityLabel` on these elements, the tests fall back to
XPath automatically. Alternatively, add `testID` / `accessibilityLabel` props to the React
Native source to make locators stable.

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

## 7. CI/CD Integration (Azure Pipelines)

The `AppiumSmoke` stage in `automation/ci/azure-pipelines.yml` is **opt-in**. It only
executes when the pipeline variable `APPIUM_ENABLED` is set to `true`. This prevents Appium
tests from blocking the standard API/unit test run on every commit.

To trigger with Appium enabled:

```bash
az pipelines run --name <pipeline-name> --variables APPIUM_ENABLED=true \
  ARXIV_APK_PATH=/path/to/app.apk ANDROID_DEVICE_NAME=emulator-5554
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
