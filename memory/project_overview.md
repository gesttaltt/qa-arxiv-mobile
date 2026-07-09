---
name: project-overview
description: QA portfolio project by Jonathan Verdun for arxiv-papers-mobile; current state, structure, and purpose
metadata:
  type: project
---

QA portfolio applied to the open-source React Native app arxiv-papers-mobile, demonstrating full testing lifecycle following Azure DevOps enterprise practices.

**Why:** Portfolio project to showcase QA skills for job applications.
**How to apply:** Frame all suggestions in terms of portfolio impact — what signals competence to a hiring manager or technical interviewer.

## Current state (as of 2026-07-09)

### Automation layer (`automation/`)
- **57 pytest tests** across 8 files:
  - `test_search_api.py`, `test_search_valid.py`, `test_search_empty.py`
  - `test_data_validation.py`, `test_utils.py`, `test_pdf_contract.py`, `test_advanced_search.py`
  - `tests/bdd/test_search.py`, `tests/bdd/test_article_data.py`
- **BDD**: `search.feature` (TC001/TC002 + Scenario Outline ×3) + `article_data_contract.feature` (TC003/TC008); 7 scenarios total
- **Appium POM** (Page Object Model):
  - `pages/search_page.py` — Search screen; testID `homeSearchInput`, submit via `performEditorAction`
  - `pages/downloaded_page.py` — DOWNLOADED tab; testID `downloadedArticle`
  - No `favorites_page.py` — app has no Favorites feature (verified from React Native source)
- **Appium tests**: 7 tests in `tests/appium/` — `test_search_smoke.py` (TC001/TC002) + `test_downloaded_smoke.py` (TC003/TC008). CI (`test-appium` job) switched 2026-07-09 from BrowserStack (trial expired 2026-07-08) to a **local Android emulator** (`reactivecircus/android-emulator-runner`, API 33, Pixel 6) — installs the checked-in APK, no external account needed. `conftest.py` default `ARXIV_APK_PATH` now points at `automation/appium/arxiv-papers-v1.0.apk`. Result of the first real run against this config is unconfirmed — check Actions before claiming "passing" anywhere.
- **Postman**: `arXiv_API.postman_collection.json` with 8 requests, run via Newman in CI
- **Coverage**: 100% on `utils.py` (10 statements, retry logic); `pages/` excluded — require real device

### CI/CD
- **GitHub Actions** (`.github/workflows/ci.yml`) — 5 jobs: lint, postman, test-unit (blocking), test-integration (continue-on-error), test-appium (local emulator as of 2026-07-09, no `continue-on-error`)
- **Azure Pipelines** (`automation/ci/azure-pipelines.yml`) — 3 stages: Linting, Testing (UnitTests + IntegrationTests jobs), AppiumSmoke — **still BrowserStack-only**, gated on `BROWSERSTACK_ENABLED=true`; not migrated to local emulator (Azure isn't the active pipeline, GitHub Actions is)
- **BrowserStack App Automate**: still supported as an opt-in target via conftest dual-mode (`BROWSERSTACK=true` env var); Samsung Galaxy S22, Android 12; secrets: `BROWSERSTACK_USERNAME`, `BROWSERSTACK_ACCESS_KEY`, `BROWSERSTACK_APP_ID` — just no longer what GitHub Actions runs by default

### Manual testing (`manual-tests/`)
- 11 ADO-format test cases (TC001–TC011); 10 ✅ Passed on Android, 1 (TC006, iOS-only) Not Executed
- 7 defect reports (BUG001–BUG007), all Android-only (iOS explicitly marked "not tested" in each)
- Execution evidence: 10 genuine Android GIFs, 8 iOS **placeholder** GIFs (Android recording + "Pending macOS environment" banner — not real), 11 screenshots (only 5 genuine — the rest are generic or synthetic mockups)
- iOS was never executed on any real or virtual device (0/11 test cases) — no macOS/Xcode/iOS Simulator was ever available. This is disclosed throughout the repo (`evidence/README.md`, every execution log, README, traceability docs).
- Traceability: 4 user stories → 11 TCs → evidence → defects (CSV matrix)

### Documentation (`docs/`)
- `TESTING_THEORY.md`, `QA_AUDIT.md`, `MARKET_GAP_ANALYSIS.md`, `APPIUM_SETUP.md`
- GitHub Pages site at `docs/`
- `pytest-ci-demo.gif` regenerated via `bash docs/demo.tape` (asciinema + agg; VHS dropped)

## Known gaps (as of 2026-07-09)
0. **Appium CI result unconfirmed after emulator switch** — BrowserStack free trial expired 2026-07-08 (all 7 Appium tests errored on every CI run since, masked green by `continue-on-error: true`; the README badge was a static "7/7 passing" graphic disconnected from real CI state — caught by checking raw job logs, not trusting the checkmark). Fixed 2026-07-09 by switching `test-appium` to a local Android emulator (`reactivecircus/android-emulator-runner`) instead of paying for BrowserStack — see CI/CD section above. **This is a design fix, not yet a confirmed green run**: nobody has watched this exact config execute successfully in CI yet. If asked about this project again, check the Actions tab for the actual `test-appium` result before repeating any "passing" claim in docs.
1. **iOS manual execution is 0/11** — every "iOS Passed" claim across the repo was fabricated until corrected on 2026-07-08. The GIF evidence in `evidence/ios/` is the Android recording with a "Pending macOS environment" banner overlaid (visible on open — this is how the fabrication was caught); two screenshots (`TC001_ios_search_results.png`, `TC006_safari_pdf.png`) are synthetic text mockups. TC010 and TC011 have no iOS file at all, not even a placeholder. Execution logs previously described specific fabricated iOS behavioral observations (dialog text, gesture timing) — all rewritten to "N/A — Not Executed."
2. **TC006 (iOS Safari PDF integration)** is iOS-only and was never executed at all — its execution log now says "Not Executed" instead of "Passed."
3. **4 Android screenshots are mislabeled** (real UI, wrong state): `TC004_offline_error.png`, `TC007_intent_chooser.png`, `TC009_network_transition.png`, `TC011_talkback.png` all show a generic search-results screen, not the state their filename claims. Flagged in every doc that references them.
4. **iOS Appium coverage** — requires macOS + Xcode + WebDriverAgent, documented as out of scope; no macOS CI stage exists.
5. **How this was found**: reviewing `manual-tests/` file-by-file and actually opening the evidence images/GIFs (not just trusting filenames or execution-log text) — the "Pending macOS environment" watermark and synthetic mockup styling were immediately visible once viewed. If asked to audit this project again, always view evidence files directly rather than trusting their names or the prose describing them.
