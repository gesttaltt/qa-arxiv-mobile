---
name: project-overview
description: QA portfolio project by Jonathan Verdun for arxiv-papers-mobile; current state, structure, and purpose
metadata:
  type: project
---

QA portfolio applied to the open-source React Native app arxiv-papers-mobile, demonstrating full testing lifecycle following Azure DevOps enterprise practices.

**Why:** Portfolio project to showcase QA skills for job applications.
**How to apply:** Frame all suggestions in terms of portfolio impact — what signals competence to a hiring manager or technical interviewer.

## Current state (as of 2026-07-08)

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
- **Appium tests**: 7 tests in `tests/appium/` — `test_search_smoke.py` (TC001/TC002) + `test_downloaded_smoke.py` (TC003/TC008)
- **Postman**: `arXiv_API.postman_collection.json` with 8 requests, run via Newman in CI
- **Coverage**: 100% on `utils.py` (10 statements, retry logic); `pages/` excluded — require real device

### CI/CD
- **GitHub Actions** (`.github/workflows/ci.yml`) — 5 jobs: lint, postman, test-unit (blocking), test-integration (continue-on-error), test-appium (BrowserStack)
- **Azure Pipelines** (`automation/ci/azure-pipelines.yml`) — 3 stages: Linting, Testing (UnitTests + IntegrationTests jobs), AppiumSmoke (BrowserStack, gated on `BROWSERSTACK_ENABLED=true`)
- **BrowserStack App Automate**: conftest dual-mode (`BROWSERSTACK=true` env var); Samsung Galaxy S22, Android 12; secrets: `BROWSERSTACK_USERNAME`, `BROWSERSTACK_ACCESS_KEY`, `BROWSERSTACK_APP_ID`

### Manual testing (`manual-tests/`)
- 11 ADO-format test cases (TC001–TC011), all ✅ Passed
- 7 defect reports (BUG001–BUG007)
- Execution evidence: Android GIFs (10 TCs), iOS GIFs (8 TCs), screenshots (11)
- Traceability: 4 user stories → 11 TCs → evidence → defects (CSV matrix)

### Documentation (`docs/`)
- `TESTING_THEORY.md`, `QA_AUDIT.md`, `MARKET_GAP_ANALYSIS.md`, `APPIUM_SETUP.md`
- GitHub Pages site at `docs/`
- `pytest-ci-demo.gif` regenerated via `bash docs/demo.tape` (asciinema + agg; VHS dropped)

## Known gaps (as of 2026-07-08)
1. **No dedicated iOS GIF for TC010** — Android has a dedicated recording (`TC010_OfflineDataPersistence_Android_Pass.gif`); iOS still shares TC004's GIF. (TC011 is Android-only by design — TalkBack has no iOS equivalent in scope — so it has no iOS gap.)
2. **iOS Appium coverage** — requires macOS + Xcode + WebDriverAgent, documented as out of scope; no macOS CI stage exists.
