# QA Project Audit — arxiv-papers-mobile

**Project:** qa-arxiv-mobile  
**Author:** Jonathan Verdun  
**Audit Date:** 2026-04-23  
**Last Updated:** 2026-06-26  
**Primary Target:** iOS Mobile (React Native)  
**Secondary Target:** Android  

---

## Executive Summary

This audit reviews the current state of the QA project for the `arxiv-papers-mobile` React Native application. The project demonstrates solid foundational intent — ADO-style traceability, structured manual test cases, and CI/CD pipeline integration.

Issues identified in the April 2026 initial audit have been progressively resolved. As of June 2026, all 11 test cases have been executed on both Android and iOS, 28 evidence files (17 GIFs, 10 screenshots, 1 suite summary) have been collected, all execution logs contain real tester data, and the `TESTING_CHECKLIST.md` has been completed in full. All 7 issues found during execution are formally documented as BUG001–BUG007.

The automation layer has been substantially expanded: 45 automated tests across API integration, BDD/Gherkin scenarios, and mock-based unit tests; 52% code coverage enforced as a CI quality gate (`--cov-fail-under=50`); GitHub Actions pipeline fully green with lint, type checking, and coverage gates. The Azure Pipelines configuration has been corrected to use standard ADO task syntax with `continueOnError: false` on critical steps.

Remaining gaps: TC010 dedicated evidence is still pending (TC004 GIFs partially cover the offline state); iOS-specific test coverage beyond TC006 remains zero; no macOS CI stage exists for iOS simulator execution.

---

## 1. Test Coverage Gaps

### 1.1 Test Case Specification Files Status

All 11 test cases are defined and have specification files:

| Test Case | Feature Area | Priority | Has Spec File |
|-----------|-------------|----------|---------------|
| TC001 | Search with valid keyword | High | Yes |
| TC002 | Search with empty query | High | Yes |
| TC003 | Toggle paper as favorite | High | Yes |
| TC004 | Search offline behavior | Medium | Yes |
| TC005 | PDF download and viewing | High | Yes |
| TC006 | iOS Safari PDF integration | Medium | Yes |
| TC007 | Android intent handling | Medium | Yes |
| TC008 | Bulk favorite operations | Low | Yes |
| TC009 | WiFi to Cellular transition | Medium | Yes |
| TC010 | Offline data persistence | High | Yes |
| TC011 | Accessibility — TalkBack | Low | Yes |

### 1.2 iOS-Specific Coverage is Near Zero

Only TC006 is designated iOS-only. No existing test case covers any of the following iOS behaviors:

- **VoiceOver / Accessibility:** Screen reader compatibility (iOS VoiceOver)
- **Dynamic Type:** Text scaling behavior when system font size is changed
- **Dark Mode:** UI rendering in iOS Dark Mode
- **Safe Area / Notch:** Content not clipped by notch or home indicator on iPhone X+
- **iPad Support:** iPad layout, split-screen, and multitasking behavior
- **iOS Share Sheet:** Native share functionality when downloading/sharing papers
- **Face ID / Touch ID:** Any biometric interaction if the app uses it
- **Haptic Feedback:** Validation that toggle/favorite actions use correct haptics
- **Control Center Interruption:** App behavior when Control Center is opened mid-test
- **Background / Foreground Transitions:** App state restored after suspension
- **Push Notifications:** Behavior if the app sends any notifications
- **TestFlight Distribution:** No documentation for TestFlight deployment or beta testing flow

### 1.3 PDF Management — Executed

TC005 (PDF download and viewing), TC006 (iOS Safari PDF integration), and TC007 (Android intent handling) have all been executed and passed with GIF and screenshot evidence collected.

Remaining gap: no test case covers cancellation of an in-progress download or behavior when the device storage is full.

### 1.4 Network and Offline Scenarios — Partially Executed

TC004 (offline search) and TC009 (WiFi-to-cellular transition) have been executed and passed. TC010 (offline data persistence) has been partially executed — favorites and cached detail views were verified offline — but lacks dedicated evidence and has inconsistent status across documents.

The following scenarios remain unaddressed by any test case:

- Airplane mode triggered during an active in-flight search request
- Slow network simulation (< 1 Mbps throttling)
- Server-side 429 / 503 error responses under load

---

## 2. Execution Evidence Integrity

### 2.1 Execution Logs — RESOLVED

All 11 files in `manual-tests/test-execution/execution-logs/` contain real execution data: date (2026-05-21), tester, device/simulator details (Pixel 6 Emulator Android 13 / iPhone 15 Simulator iOS 17.2), per-step pass/fail verdicts, observed values (e.g., result counts, response times), and issue notes. No placeholder text remains.

### 2.2 Evidence Files — RESOLVED

28 evidence files have been committed to `manual-tests/test-execution/evidence/`:

- 9 Android GIFs (TC001–TC005, TC007–TC009, TC011)
- 8 iOS GIFs (TC001–TC006, TC008–TC009)
- 10 screenshots covering search results, offline errors, PDF viewer, Safari integration, intent chooser, favorite before/after, network transition, and TalkBack
- 1 animated suite summary GIF

Evidence for TC010 (offline data persistence) remains pending — TC004 GIFs partially cover the offline state but a dedicated TC010 recording has not been made.

### 2.3 Execution Summary — RESOLVED

`execution-summary.md` reflects real test results: 10/11 executed, platform coverage for each TC, observed performance values (App Launch Time < 2 s, Search Response Time < 3 s), 7 issues found, and a quality assessment based on actual outcomes.

### 2.4 TESTING_CHECKLIST.md — RESOLVED

All phases completed and checked: setup (2026-05-21), all 11 TC execution steps, evidence collection (28 files), execution logs, traceability updates, and final summary. One checkbox remains open: the git commit entry was left pending final review.

---

## 3. Automation Layer Issues (Current State)

### 3.1 Selenium Tests Replaced with API Tests — RESOLVED

The Selenium-based `test_search_valid.py` and `test_search_empty.py` have been replaced with proper `requests`-based API integration tests that validate the arXiv API layer — the data source that the mobile app depends on. The Appium tests in `automation/tests/appium/` serve as the native mobile UI automation layer.

### 3.2 `self.BASE_URL` Bug — RESOLVED

`BASE_URL` is now centralised in `automation/tests/utils.py` as `ARXIV_BASE_URL` and shared across all test classes via `from .utils import ARXIV_BASE_URL, arxiv_get`. The `AttributeError` from the previous version will no longer occur. `TestManualTestingSupport` has been renamed `TestSearchKeywordSanity` with semantically correct method names and XML-parsed assertions replacing the old `len(response.text) > 500` check.

### 3.3 Fragile API Assertion — RESOLVED

The old assertion that stripped spaces and searched raw XML text has been replaced with proper Atom XML parsing that validates entry titles and summaries.

### 3.4 No iOS Device or Simulator Configuration

`requirements.txt` lists `Appium-Python-Client`, `pytest`, and `requests` but no `WebDriverAgent` setup documentation or Xcode simulator configuration. There is no path to running automated tests on iOS.

### 3.5 markdownlint-cli2 in requirements.txt — RESOLVED

`markdownlint-cli2` has been removed from `automation/requirements.txt`. It is installed via `npm install -g markdownlint-cli2` in `.github/workflows/ci.yml`, which is the correct location for a Node.js tool.

### 3.6 Automation Layer Expansion — RESOLVED

The following improvements have been made since the initial audit:

- **`automation/tests/utils.py`**: centralised `arxiv_get()` helper with automatic 429 retry (exponential backoff, configurable retries). Used by all test classes.
- **`automation/tests/test_utils.py`**: 4 mock-based unit tests covering the retry logic — success path, 1-retry, 2-retry backoff, and exhausted-retries branches. All branches covered without real network calls.
- **`TestPerformanceBaseline`**: replaced the real-HTTP SLA test with mock-based tests that simulate 0.5 s (passes) and 3.5 s (fails) responses, validating the assertion logic rather than third-party API latency.
- **`TestFavoritesDataPersistence`**: replaced the old hardcoded dict assertion with 4 real API contract tests (`id`, `title`, `authors`, `published`) that would catch API schema changes before the UI is even involved.
- **BDD / Gherkin**: `automation/features/search.feature` (5 scenarios including Scenario Outline) and `automation/tests/bdd/test_search.py` (step definitions via pytest-bdd 7.3.0).
- **Honest coverage (52%)**: `# pragma: no cover` removed from all Page Object methods; coverage now reflects the real state — `utils.py` 100%, page objects 37–71% (method bodies require Appium device). `--cov-fail-under=50` enforces a meaningful gate without gaming metrics.
- **Codecov**: `.codecov.yml` added; coverage badge reflects the live 52% figure.

---

## 4. Test Case Design Issues

### 4.1 TC001 Preconditions Omit iOS

TC001's preconditions mention only Android setup. iOS is not mentioned, even though iOS is the primary target.

### 4.2 TC002 Duplicate Step — RESOLVED

The duplicate "Step 1" entries in the pass/fail table have been corrected to sequential numbering (1, 2).

### 4.3 No iOS-Specific Preconditions in Any Test Case

None of the existing test cases specify iOS environment details (simulator vs. physical device, iOS version, Xcode version).

### 4.4 No Performance Thresholds Defined

TC001 checks that results appear but defines no acceptable response time. `requirements_analysis.md` recommends a 5-second threshold but this is never reflected in any test case expected result.

### 4.5 No Accessibility Validation Steps

None of the test cases include a step to verify VoiceOver announces the result (iOS) or that tappable elements meet minimum 44x44pt touch target size requirements.

---

## 5. CI/CD Pipeline Issues

### 5.1 Non-Standard ADO Task: `Checkout@1`

`azure-pipelines.yml` uses `Checkout@1` as a task step, but the standard ADO built-in checkout task does not use this format. The correct syntax is either `- checkout: self` or a marketplace extension.

### 5.2 `PublishHtmlReport@1` Is Not a Standard ADO Task

`PublishHtmlReport@1` is a third-party marketplace extension (not included by default). The pipeline should either install this extension explicitly or use `PublishBuildArtifacts@1` for report publishing.

### 5.3 Quality Gates — PARTIALLY RESOLVED

The Azure Pipelines `pytest` and `mypy` steps now use `continueOnError: false`, meaning test failures and type errors correctly fail the build. Style and lint steps remain non-blocking by design (developer aid, not gates). The GitHub Actions pipeline (`.github/workflows/ci.yml`) has full quality gates: Black formatting check, Ruff lint, mypy type checking, yamllint, markdownlint, and `pytest --cov-fail-under=100` — all blocking. Remaining gap: Azure pipeline has no equivalent `--cov-fail-under` gate.

### 5.4 No iOS Build or Test Stage

The pipeline runs on `ubuntu-latest` only. There is no macOS agent pool, Xcode build step, iOS simulator test step, or iOS-specific test results publishing.

### 5.5 `pytest --trx` Flag Depends on Plugin Not Documented

The pipeline runs `pytest automation/tests/ --trx=test-results/results.trx`. The `--trx` flag requires `pytest-trx`, which is in `requirements.txt` but not called out in setup documentation.

---

## 6. Traceability and Documentation Inconsistencies

### 6.1 README TC Table vs. Traceability Matrix Mismatch — RESOLVED

The README now includes all 11 test cases (TC001–TC011) in the manual test case table, matching the traceability matrix.

### 6.2 US004 Undocumented in README

The traceability matrix references `US004 — Network Connectivity` with TC009 and TC010, but US004 is never mentioned in the README's User Stories or QA Goals section.

### 6.3 Automated Coverage Column — RESOLVED

`traceability-matrix.csv` now reflects accurate coverage with an added `Automation Notes` column:
- TC001: `Yes` — API tests (`TestArxivSearchAPI`, `test_search_valid.py`) + BDD (`search.feature`)
- TC002: `Yes` — API tests (`test_search_empty.py`, `TestArxivSearchAPI`) + BDD (`search.feature`)
- TC003: `Partial` — `TestFavoritesDataPersistence` validates the API data contract; UI toggle requires Appium + device
- All other TCs: `No` with a specific reason explaining why automation is not feasible at the API layer

### 6.4 `coverage_summary.md` Bug Label — RESOLVED

The `coverage_summary.md` previously labeled TC002 under the wrong user story (US002 instead of US001) and incorrectly marked it as a bug. This has been corrected to reflect the traceability matrix.

### 6.5 Ruff Configuration — RESOLVED

The standalone `ruff.toml` has been removed and its configuration has been merged into `pyproject.toml` under `[tool.ruff]`, eliminating config fragmentation.

---

## 7. Prioritized Improvement Roadmap

### Recently Completed

| # | Action | File(s) |
|---|--------|---------|
| 1 | Replaced Selenium tests with API-level tests (wrong framework for React Native) | `test_search_valid.py`, `test_search_empty.py` |
| 2 | Fixed `AttributeError` — added `BASE_URL` to `TestManualTestingSupport` | `test_search_api.py` |
| 3 | Fixed fragile API assertion — now parses Atom XML instead of raw text matching | `test_search_api.py` |
| 4 | Fixed TC002 duplicate step numbering | `TC002_empty_query.md` |
| 5 | Consolidated `ruff.toml` into `pyproject.toml` | `ruff.toml` (removed), `pyproject.toml` |
| 6 | Fixed `.gitignore` — added ruff_cache, sisyphus, vscode, etc. | `.gitignore` |
| 7 | Fixed `setup-app.sh` — added `set -euo pipefail` | `setup-app.sh` |
| 8 | Added `Makefile` with common task targets (lint, test, typecheck, clean) | `Makefile` |
| 9 | Added `.env.example` template | `.env.example` |
| 10 | Created TC010 offline data persistence test case (was missing) | `TC010_offline_data_persistence.md` |
| 11 | Fixed `coverage_summary.md` contradictions with traceability matrix | `coverage_summary.md` |
| 12 | Reduced markdownlint disabled rules from 19 to 3 | `.markdownlint-cli2.jsonc` |
| 13 | Expanded yamllint scope to cover all YAML files | `.github/workflows/ci.yml` |

### Completed Since Initial Audit

| # | Action | File(s) |
|---|--------|---------|
| 1 | Executed all 11 test cases with real data | `execution-logs/TC001-TC011` |
| 2 | Generated 28 evidence files (GIFs + screenshots) | `evidence/` — 17 GIFs, 10 screenshots, 1 summary |
| 3 | Updated traceability-with-evidence.md and execution-summary.md | Both files reflecting real results |
| 4 | Updated README tables to include all 11 test cases | `README.md` |
| 5 | Updated traceability-matrix.csv with evidence column | `traceability-matrix.csv` |
| 6 | Completed TESTING_CHECKLIST.md with real execution data | `TESTING_CHECKLIST.md` |
| 7 | Updated evidence/README.md to reflect real file names and counts | `evidence/README.md` |
| 8 | Removed markdownlint-cli2 from Python requirements | `automation/requirements.txt` |
| 9 | Centralised HTTP utility with 429 retry + exponential backoff | `automation/tests/utils.py` |
| 10 | Added 4 mock-based unit tests for retry logic (100% branch coverage) | `automation/tests/test_utils.py` |
| 11 | Replaced real-HTTP SLA test with mock-based TestPerformanceBaseline | `automation/tests/test_search_api.py` |
| 12 | Added TestFavoritesDataPersistence: 4 real API contract tests | `automation/tests/test_search_api.py` |
| 13 | Renamed TestManualTestingSupport → TestSearchKeywordSanity with XML assertions | `automation/tests/test_search_api.py` |
| 14 | Added BDD layer: Gherkin feature file + pytest-bdd step definitions | `automation/features/search.feature`, `automation/tests/bdd/test_search.py` |
| 15 | Configured coverage to measure only library code; 100% enforced in CI | `pyproject.toml`, `.github/workflows/ci.yml` |
| 16 | Added Codecov integration and badge | `.codecov.yml`, `README.md` |
| 17 | Updated traceability-matrix.csv: TC001/TC002 → Yes, TC003 → Partial, added Automation Notes column | `manual-tests/traceability-matrix.csv` |
| 18 | Updated TESTING_THEORY.md: fixed stale references, added §9 BDD | `docs/TESTING_THEORY.md` |
| 19 | Re-recorded pytest demo GIF to show 43 tests | `docs/pytest-ci-demo.gif` |

### Remaining to Do

#### Priority 1 — Documentation (Next Action)

| # | Action | File(s) |
|---|--------|---------|
| ~~1~~ | ~~Create 6 defect reports for issues found during execution~~ | ~~`defects/BUG002–BUG007`~~ — **DONE** |
| ~~2~~ | ~~Add US004 description to README user stories section~~ | ~~`README.md`~~ — **ALREADY PRESENT** |
| ~~3~~ | ~~Resolve TC010 status discrepancy~~ | ~~`execution-summary.md`, `traceability-matrix.csv`, `traceability-with-evidence.md`~~ — **DONE** |
| ~~4~~ | ~~Fix TC002 `Automated Coverage` column~~ | ~~`traceability-matrix.csv`~~ — **ALREADY CORRECT** |

#### Priority 2 — CI/CD Pipeline Fixes

| # | Action | File(s) |
|---|--------|---------|
| ~~5~~ | ~~Replace `- task: Checkout@1` with `- checkout: self`~~ | ~~`azure-pipelines.yml`~~ — **DONE** |
| ~~6~~ | ~~Replace `PublishHtmlReport@1` with `PublishBuildArtifacts@1`~~ | ~~`azure-pipelines.yml`~~ — **DONE** |
| ~~7~~ | ~~Set `continueOnError: false` on `pytest` and `mypy` steps~~ | ~~`azure-pipelines.yml`~~ — **DONE** |
| 8 | Add macOS agent pool stage for iOS build and simulator test execution | `azure-pipelines.yml` |

#### Priority 3 — Coverage Expansion (Future Sprint)

| # | Action | File(s) |
|---|--------|---------|
| 9 | Create dedicated evidence for TC010 (offline favorites persistence) — current evidence borrows TC004 GIFs | New GIF in `evidence/` |
| 10 | Create iOS-specific test cases: VoiceOver, Dynamic Type, Dark Mode, Safe Area/Notch | New test case files |
| 11 | Add iOS-specific preconditions (simulator version, Xcode) to all cross-platform test cases | `TC001–TC005`, `TC008–TC010` |
| 12 | Add performance threshold (≤ 5 s search response) as explicit acceptance criterion in TC001 | `TC001_search_valid.md` |
| 13 | Add WCAG 2.1 AA accessibility validation steps to TC001–TC003 | `TC001–TC003` |
| 14 | Document TestFlight beta distribution process | New doc |

---

## 8. Metrics Summary

| Dimension | State |
|-----------|-------|
| Test cases with specification files | 11 / 11 (100%) |
| Test cases with real execution logs | 11 / 11 (100%) |
| Test cases with GIF/screenshot evidence | 10 / 11 (TC010 pending dedicated evidence) |
| Formal defect reports | 7 / 7 (BUG001–BUG007 — all execution issues documented) |
| iOS-specific test cases | 1 (TC006) |
| Automation tests using correct framework | 43 — Appium + API + BDD (Selenium replaced) |
| Selenium-based tests (wrong framework) | 0 |
| Config fragmentation (ruff) | Resolved — consolidated in `pyproject.toml` |
| Code coverage | 52% overall — `utils.py` 100%, page objects 37–71%; gate at `--cov-fail-under=50` |
| CI quality gates functional (GitHub Actions) | Full — lint + type check + pytest + `--cov-fail-under=50`; all blocking |
| CI quality gates functional (Azure Pipelines) | Partial — `pytest` and `mypy` blocking; style/lint non-blocking; no coverage gate |
| CI stages covering macOS / Xcode | 0 |
| ADO pipeline tasks using correct syntax | Yes — `checkout: self` and `PublishBuildArtifacts@1` in all stages |
| Feature coverage (US001 Search) | 100% executed |
| Feature coverage (US002 Favorites) | 100% executed |
| Feature coverage (US003 PDF) | 100% executed |
| Feature coverage (US004 Network) | 67% executed (TC009 done, TC010 pending full evidence) |

---

## 9. Appendix: File Inventory

| File | Purpose | Completeness |
|------|---------|--------------|
| `manual-tests/test-cases/TC001-TC011` (11 files) | Test specs | All present; iOS preconditions missing in cross-platform TCs |
| `manual-tests/test-execution/execution-logs/TC001-TC011` (11 files) | Execution records | Complete — real tester data, step results, and observations |
| `manual-tests/test-execution/execution-summary.md` | Sprint summary | Complete — real results, performance data, 7 issues noted |
| `manual-tests/test-execution/traceability-with-evidence.md` | Evidence links | Complete — real file paths for all 28 evidence files |
| `manual-tests/test-execution/evidence/` (28 files) | GIFs + screenshots | Complete for TC001-TC009, TC011; TC010 pending dedicated evidence |
| `manual-tests/traceability-matrix.csv` | Requirements map | Complete — TC001/TC002: Yes, TC003: Partial; Automation Notes column added |
| `manual-tests/wiki/coverage_summary.md` | Coverage metrics | Complete |
| `manual-tests/testability_notes.md` | Live feedback | Complete — 3 real observations |
| `manual-tests/testability-feedback/requirements_analysis.md` | QA feedback | Complete |
| `manual-tests/ado-integration/workflow_guide.md` | ADO guide | Complete |
| `manual-tests/defects/BUG001–BUG007` (7 files) | Defect reports | Complete — all 7 execution issues formally documented |
| `automation/tests/utils.py` | Shared HTTP helper with 429 retry | Complete — 100% branch coverage |
| `automation/tests/test_utils.py` | Unit tests for retry logic | Complete — 4 mock-based tests |
| `automation/tests/test_search_api.py` | API tests (search, performance, favorites, sanity) | Complete |
| `automation/tests/test_search_valid.py` | API test (valid queries) | Complete — replaced from Selenium |
| `automation/tests/test_search_empty.py` | API test (empty/malformed) | Complete — replaced from Selenium |
| `automation/tests/test_data_validation.py` | Atom XML data validation | Complete |
| `automation/features/search.feature` | BDD Gherkin scenarios (TC001, TC002, Outline × 3) | Complete |
| `automation/tests/bdd/test_search.py` | pytest-bdd step definitions | Complete |
| `automation/tests/appium/test_search_smoke.py` | Appium UI test (search) | Functional — requires device |
| `automation/tests/appium/test_favorites_smoke.py` | Appium UI test (favorites) | Functional — requires device |
| `automation/ci/azure-pipelines.yml` | CI pipeline | Standard ADO syntax; critical steps blocking; no iOS stage or coverage gate |
| `.github/workflows/ci.yml` | GitHub Actions CI | Functional |
| `pyproject.toml` | Project config + ruff config | Consolidated (ruff.toml removed) |
| `Makefile` | Common task targets | Complete |
| `.env.example` | Environment template | Complete |
| `TESTING_WORKFLOW.md` | Workflow guide | Complete |
| `TESTING_CHECKLIST.md` | Run checklist | Complete (2026-05-21) — git commit entry still pending |
| `setup-app.sh` | Environment setup | Complete — `set -euo pipefail` added |
