# QA Project Audit — arxiv-papers-mobile

**Project:** qa-arxiv-mobile  
**Author:** Jonathan Verdun  
**Audit Date:** 2026-04-23  
**Last Updated:** 2026-05-21  
**Primary Target:** iOS Mobile (React Native)  
**Secondary Target:** Android  

---

## Executive Summary

This audit reviews the current state of the QA project for the `arxiv-papers-mobile` React Native application. The project demonstrates solid foundational intent — ADO-style traceability, structured manual test cases, and CI/CD pipeline integration. Several issues identified in the initial audit (April 2026) have since been resolved: the broken Selenium tests have been replaced with proper API-level tests, the `AttributeError` in `test_search_api.py` has been fixed, the ruff config has been consolidated, and the TC002 duplicate step has been corrected. Remaining gaps include unfilled execution log templates, no real video evidence, and limited iOS-specific coverage.

---

## 1. Test Coverage Gaps

### 1.1 Test Case Specification Files Status

Eleven test cases are defined across the project. All but TC010 (offline data persistence — recently added, see below) have specification files:

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

### 1.3 PDF Management — Zero Executed Coverage

PDF download and iOS Safari PDF viewer integration are high-priority features (US003) with no executed tests.

### 1.4 Network and Offline Scenarios

The following network scenarios are planned but unexecuted:

- Airplane mode during active search
- WiFi to cellular transition mid-request
- Slow network simulation (< 1 Mbps)
- Network recovery after loss

---

## 2. Execution Evidence Integrity

### 2.1 All Execution Logs Are Unfilled Templates

Every file in `manual-tests/test-execution/execution-logs/` contains placeholder text. No real execution date, device, tester name, step result, or observation has been recorded:

```
**Test Date:** [Date to be filled during execution]
**Tester:** [Your name]
**Device/Simulator:** [e.g., iPhone 15, iOS 17.0]
```

### 2.2 Video Evidence Does Not Exist

The README prominently claims "Real Mobile Test Execution" with video evidence links. All video links resolve to placeholder text:

```
[Video Link - Replace with actual Loom/Drive link]
```

The `manual-tests/test-execution/evidence/` folder contains only a `README.md` with no actual screenshots or recordings.

### 2.3 Execution Summary Pre-Populated with False Data

`execution-summary.md` contains pre-set quality ratings that were never based on actual test results. Performance fields (`App Launch Time`, `Search Response Time`) are empty strings.

### 2.4 TESTING_CHECKLIST.md Never Used

All checkboxes remain unchecked. The `Date Started`, `Tester`, and all result fields are blank.

---

## 3. Automation Layer Issues (Current State)

### 3.1 Selenium Tests Replaced with API Tests — RESOLVED

The Selenium-based `test_search_valid.py` and `test_search_empty.py` have been replaced with proper `requests`-based API integration tests that validate the arXiv API layer — the data source that the mobile app depends on. The Appium tests in `automation/tests/appium/` serve as the native mobile UI automation layer.

### 3.2 `self.BASE_URL` Bug — RESOLVED

`TestManualTestingSupport` in `test_search_api.py` now defines its own `BASE_URL = "http://export.arxiv.org/api/query"`. The `AttributeError` from the previous version will no longer occur.

### 3.3 Fragile API Assertion — RESOLVED

The old assertion that stripped spaces and searched raw XML text has been replaced with proper Atom XML parsing that validates entry titles and summaries.

### 3.4 No iOS Device or Simulator Configuration

`requirements.txt` lists `Appium-Python-Client`, `pytest`, and `requests` but no `WebDriverAgent` setup documentation or Xcode simulator configuration. There is no path to running automated tests on iOS.

### 3.5 markdownlint-cli2 in requirements.txt

`markdownlint-cli2` is listed in `automation/requirements.txt` as a Python package but it is a Node.js package installed via `npm`. This `pip install` will fail. **Recommendation:** Remove it from `requirements.txt` and keep it in `.github/workflows/ci.yml` where it's installed via `npm install -g markdownlint-cli2`.

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

### 5.3 All Quality Gates Use `continueOnError: true`

Every linting and testing step has `continueOnError: true`, meaning the pipeline will always report green even if Python linting, type checking, or tests fail.

### 5.4 No iOS Build or Test Stage

The pipeline runs on `ubuntu-latest` only. There is no macOS agent pool, Xcode build step, iOS simulator test step, or iOS-specific test results publishing.

### 5.5 `pytest --trx` Flag Depends on Plugin Not Documented

The pipeline runs `pytest automation/tests/ --trx=test-results/results.trx`. The `--trx` flag requires `pytest-trx`, which is in `requirements.txt` but not called out in setup documentation.

---

## 6. Traceability and Documentation Inconsistencies

### 6.1 README TC Table vs. Traceability Matrix Mismatch

The README shows TC001–TC007. The `traceability-matrix.csv` includes TC008, TC009, TC010 (mapped to US002 and US004) that are not listed in the README at all.

### 6.2 US004 Undocumented in README

The traceability matrix references `US004 — Network Connectivity` with TC009 and TC010, but US004 is never mentioned in the README's User Stories or QA Goals section.

### 6.3 Automated Coverage Column is Inconsistent

In `traceability-matrix.csv`:
- TC001: `Partial`
- TC002: `Yes`
- TC003: `No`

The `test_search_api.py` file covers both TC001 and TC002 equivalently at the API layer. TC002 should be `Partial` (API validated, UI not automated).

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
| 2 | Generated 28 evidence files (GIFs + screenshots) | `evidence/` - 17 GIFs, 10 screenshots, 1 summary |
| 3 | Updated traceability-with-evidence.md and execution-summary.md | Both files reflecting real results |
| 4 | Updated README tables to include all 11 test cases | `README.md` |
| 5 | Updated traceability-matrix.csv with evidence column | `traceability-matrix.csv` |

### Remaining to Do

#### Priority 1 — Documentation Polish
| # | Action | File(s) |
|---|--------|---------|
| 1 | Fill TESTING_CHECKLIST.md with execution dates and results | `TESTING_CHECKLIST.md` |
| 2 | Update evidence/README.md to reflect real file names and counts | `evidence/README.md` |
| 3 | Create defect reports from real execution issues found | `defects/` (new files) |
| 4 | Add US004 description to README user stories section | `README.md` |

#### Priority 2 — Automation & CI
| # | Action | File(s) |
|---|--------|---------|
| 5 | Set `continueOnError: false` on `pytest` and `mypy` pipeline steps | `azure-pipelines.yml` |
| 6 | Add macOS agent pool stage to CI pipeline for iOS builds | `azure-pipelines.yml` |

#### Priority 3 — Coverage Expansion (Future Sprint)
| # | Action | File(s) |
|---|--------|---------|
| 7 | Create iOS-specific test cases: VoiceOver, Dynamic Type, Dark Mode, Safe Area | New test cases |
| 8 | Add iOS-specific preconditions to all cross-platform test cases | TC001-TC005, TC008-TC010 |
| 9 | Define performance thresholds (e.g., 5-second search response) in TC001 | `TC001_search_valid.md` |
| 10 | Create TC010 dedicated evidence video (offline favorites persistence) | New evidence |
| 11 | Add WCAG 2.1 AA accessibility steps to core test cases | TC001-TC003 |
| 12 | Define iOS performance benchmarks by device class | New doc |
| 13 | Document TestFlight beta distribution process | New doc |

---

## 8. Metrics Summary

| Dimension | State |
|-----------|-------|
| Test cases with specification files | 11 / 11 (100%) |
| Test cases with real execution logs | 11 / 11 (100%) |
| iOS-specific test cases | 1 (TC006 — tested) |
| Evidence files (GIFs + screenshots) | 28 |
| Automation tests using correct framework | ✅ (Appium + API) |
| Selenium-based tests (wrong framework) | 0 (replaced) |
| Config fragmentation (ruff) | Resolved — consolidated in pyproject.toml |
| CI stages covering macOS / Xcode | 0 |
| Feature coverage (PDF Management) | 100% executed, evidence collected |
| Overall feature coverage | 91% (10/11 executed, evidence collected) |

---

## 9. Appendix: File Inventory

| File | Purpose | Completeness |
|------|---------|--------------|
| `manual-tests/test-cases/TC001-TC011` (11 files) | Test specs | All present; iOS preconditions missing |
| `manual-tests/test-execution/execution-logs/TC001-003` | Execution records | Templates only — need real data |
| `manual-tests/test-execution/execution-summary.md` | Sprint summary | Template with false data |
| `manual-tests/test-execution/traceability-with-evidence.md` | Evidence links | All links are placeholders |
| `manual-tests/traceability-matrix.csv` | Requirements map | Minor automation-coverage inconsistency |
| `manual-tests/wiki/coverage_summary.md` | Coverage metrics | Corrected |
| `manual-tests/testability_notes.md` | Live feedback | Complete — 3 real observations |
| `manual-tests/testability-feedback/requirements_analysis.md` | QA feedback | Complete |
| `manual-tests/ado-integration/workflow_guide.md` | ADO guide | Complete |
| `manual-tests/defects/BUG001_sample_defect.md` | Sample defect | Complete |
| `automation/tests/test_search_api.py` | API tests | Functional — bugs fixed |
| `automation/tests/test_search_valid.py` | API test (valid queries) | Replaced from Selenium |
| `automation/tests/test_search_empty.py` | API test (empty/malformed) | Replaced from Selenium |
| `automation/tests/test_data_validation.py` | Atom XML data validation | Complete |
| `automation/tests/appium/test_search_smoke.py` | Appium UI test (search) | Functional |
| `automation/tests/appium/test_favorites_smoke.py` | Appium UI test (favorites) | Functional |
| `automation/ci/azure-pipelines.yml` | CI pipeline | Missing iOS stage, quality gates disabled |
| `.github/workflows/ci.yml` | GitHub Actions CI | Functional |
| `pyproject.toml` | Project config + ruff config | Consolidated (ruff.toml removed) |
| `Makefile` | Common task targets | Added |
| `.env.example` | Environment template | Added |
| `TESTING_WORKFLOW.md` | Workflow guide | Complete |
| `TESTING_CHECKLIST.md` | Run checklist | Entirely unchecked |
| `setup-app.sh` | Environment setup | Fixed — added `set -euo pipefail` |
