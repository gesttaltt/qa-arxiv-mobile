# QA Project Audit — arxiv-papers-mobile

**Project:** qa-arxiv-mobile  
**Author:** Jonathan Verdun  
**Audit Date:** 2026-04-23  
**Primary Target:** iOS Mobile (React Native)  
**Secondary Target:** Android  

---

## Executive Summary

This audit reviews the current state of the QA project for the `arxiv-papers-mobile` React Native application. The project demonstrates solid foundational intent — ADO-style traceability, structured manual test cases, and CI/CD pipeline integration — but has significant gaps in real execution evidence, iOS-specific coverage, and automation correctness. Of the 10 planned test cases, only 3 have both a specification file and a documented (though unverified) execution log. The automation layer uses the wrong testing framework for a native mobile app, and critical iOS-specific scenarios are entirely absent.

---

## 1. Test Coverage Gaps

### 1.1 Missing Test Case Specification Files

Seven test cases are referenced across the traceability matrix and README but have no corresponding `.md` specification file:

| Test Case | Feature Area | Priority | Status |
|-----------|-------------|----------|--------|
| TC004 | Search offline behavior | Medium | Referenced only |
| TC005 | PDF download and viewing | High | Referenced only |
| TC006 | iOS Safari PDF integration | Medium | Referenced only |
| TC007 | Android intent handling | Medium | Referenced only |
| TC008 | Bulk favorite operations | Low | Referenced only |
| TC009 | WiFi to Cellular transition | Medium | Referenced only |
| TC010 | Offline data persistence | High | Referenced only |

**Impact:** 70% of the planned test suite cannot be executed because the test specifications were never written. TC006 is the only iOS-specific planned test case, and it is one of those missing.

### 1.2 iOS-Specific Coverage is Near Zero

Only TC006 is designated iOS-only, and it has no specification file. No existing test case covers any of the following iOS behaviors:

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

The `wiki/coverage_summary.md` explicitly documents 0% test coverage for PDF Management:

```
| PDF Management | 3 | 0 | 0 | 0 | 0% |
```

PDF download and iOS Safari PDF viewer integration are high-priority user story features (US003) with no executed tests.

### 1.4 Network and Offline Scenarios

TC004 (offline search) is marked "In Progress" but has no specification file and no execution log. The following network scenarios are planned but unexecuted:

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

The README prominently claims "Real Mobile Test Execution" with "🎥 Video Evidence" links. All video links resolve to placeholder text:

```
[Video Link - Replace with actual Loom/Drive link]
```

The `manual-tests/test-execution/evidence/` folder contains only a `README.md` with no actual screenshots or recordings.

### 2.3 Execution Summary Pre-Populated with False Data

`execution-summary.md` contains pre-set quality ratings that were never based on actual test results:

```
- **Search Functionality:** ⭐⭐⭐⭐⭐ (5/5)
- **Error Handling:** ⭐⭐⭐⭐⭐ (5/5)
- **Favorite Management:** ⭐⭐⭐⭐⭐ (5/5)
- **Platform Consistency:** ⭐⭐⭐⭐⭐ (5/5)
```

Performance fields (`App Launch Time`, `Search Response Time`) are empty strings.

### 2.4 TESTING_CHECKLIST.md Never Used

All checkboxes in `TESTING_CHECKLIST.md` remain unchecked. The `Date Started`, `Tester`, and all result fields are blank.

---

## 3. Automation Layer Issues

### 3.1 Wrong Framework for React Native Mobile Testing

**This is the most critical automation defect.** `test_search_valid.py` and `test_search_empty.py` use **Selenium WebDriver** targeting `http://localhost:8081` with a Chrome browser session:

```python
# test_search_valid.py
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost:8081")
search_input = driver.find_element(By.ID, "searchInput")
```

This approach cannot test a React Native mobile app. React Native renders to native UIKit (iOS) or Android Views — not a browser DOM. These tests would fail immediately because:

- `localhost:8081` is the Metro bundler dev server, not a testable browser UI
- React Native components do not expose HTML element IDs
- Selenium cannot interact with native iOS or Android UI elements

**Correct frameworks for React Native mobile testing:**
- **Appium** — Cross-platform (iOS + Android), drives native elements via XCUITest / UIAutomator
- **Detox** — Purpose-built for React Native, grey-box testing with fast feedback
- **XCUITest** (iOS only) — Native Apple automation framework

### 3.2 Hardcoded Sleep Calls

Both Selenium tests use `time.sleep()` which is an anti-pattern in test automation. This creates flaky tests and slow suites:

```python
# test_search_valid.py
time.sleep(3)

# test_search_empty.py
time.sleep(2)
```

Should be replaced with explicit waits (`WebDriverWait` / Appium's `wait_for_element`) or Detox's built-in synchronization.

### 3.3 `self.BASE_URL` Referenced in Class Without Definition

In `test_search_api.py`, the `TestManualTestingSupport` class calls `self.BASE_URL` but the class never defines it:

```python
class TestManualTestingSupport:
    def test_test_environment_connectivity(self):
        response = requests.get(self.BASE_URL, timeout=10)  # AttributeError
```

Only `TestArxivSearchAPI` defines `BASE_URL = "http://export.arxiv.org/api/query"`. Running `test_test_environment_connectivity` or `test_generate_test_data_for_manual_testing` will raise `AttributeError` at runtime.

### 3.4 Fragile API Assertion in test_search_api.py

```python
assert search_term.replace(' ', '') in response.text.lower().replace(' ', '')
```

This strips spaces and checks raw XML text — it will pass even if the term appears in an unrelated tag (e.g., URL, namespace). A proper check should parse the Atom XML and validate `<entry>` elements.

### 3.5 No iOS Device or Simulator Configuration

`requirements.txt` lists `selenium`, `pytest`, and `requests` but no Appium client, no `WebDriverAgent` setup documentation, and no Xcode simulator configuration. There is no path to running automated tests on iOS.

### 3.6 markdownlint-cli2 Listed as Python Dependency

`automation/requirements.txt` includes:

```
markdownlint-cli2==0.15.0
```

`markdownlint-cli2` is a Node.js package installed via `npm`, not `pip`. This `pip install` will fail.

---

## 4. Test Case Design Issues

### 4.1 TC001 Preconditions Omit iOS

TC001's preconditions read: *"App is installed and running on an **Android** emulator or device."* iOS is not mentioned, even though iOS is the primary target and the test is executed on both platforms.

### 4.2 TC002 Has Duplicate Step Entry

The pass/fail table in `TC002_empty_query.md` has two rows for "Step 1":

```markdown
| 1 | Validation prevents empty search |  |
| 1 | No crash or blank screen appears |  |
```

Step numbering should be sequential; these are two different validation criteria for the same action and should be split into a step with multiple expected outcomes, or given distinct step IDs.

### 4.3 No iOS-Specific Preconditions in Any Test Case

None of the 3 existing test cases specify iOS environment details (simulator vs. physical device, iOS version, Xcode version). For iOS testing, preconditions should include:

- Device type (iPhone 13 / iPhone SE / iPad)
- iOS version
- Whether using simulator or physical device
- Build type (debug / release via TestFlight)

### 4.4 No Performance Thresholds Defined

TC001 checks that results appear but defines no acceptable response time. `requirements_analysis.md` recommends a 5-second threshold but this is never reflected in any test case expected result.

### 4.5 No Accessibility Validation Steps

None of the test cases include a step to verify VoiceOver announces the result (iOS) or that tappable elements meet minimum 44×44pt touch target size requirements.

---

## 5. CI/CD Pipeline Issues

### 5.1 Non-Standard ADO Task: `Checkout@1`

`azure-pipelines.yml` uses `Checkout@1` as a task step, but the standard ADO built-in checkout task does not use this format. The correct syntax is either:

```yaml
- checkout: self
```

or the built-in `Checkout@1` refers to a marketplace extension. Without clarification, this may resolve incorrectly or fail in a real ADO environment.

### 5.2 `PublishHtmlReport@1` Is Not a Standard ADO Task

`PublishHtmlReport@1` is a third-party marketplace extension (not included by default). The pipeline should either install this extension explicitly or use `PublishBuildArtifacts@1` for report publishing.

### 5.3 All Quality Gates Use `continueOnError: true`

Every linting and testing step has `continueOnError: true`:

```yaml
continueOnError: true
```

This means the pipeline will always report green even if Python linting, type checking, or tests fail. This eliminates the value of the quality gate entirely. At minimum, `pytest` execution and mypy should enforce failure.

### 5.4 No iOS Build or Test Stage

The pipeline runs on `ubuntu-latest` only. There is no:

- `macOS` agent pool configuration
- Xcode build step
- iOS simulator test step
- iOS-specific test results publishing

Without a macOS agent and Xcode, iOS testing cannot be included in CI.

### 5.5 `pytest --trx` Flag Depends on Plugin Not Documented

The pipeline runs:

```yaml
pytest automation/tests/ --trx=test-results/results.trx
```

`--trx` requires `pytest-trx`, which is in `requirements.txt` but not called out in setup documentation. If the plugin isn't installed before the pipeline runs, this flag fails silently or raises an error.

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

The `test_search_api.py` file covers both TC001 and TC002 equivalently at the API layer. TC002 should be `Partial` (API validated, UI not automated). The inconsistency suggests the column was set manually without review.

### 6.4 `coverage_summary.md` Labels TC002 as a Bug

The wiki coverage map notes:

```
| US002 – Empty query | TC002 | ✅ Yes | Validation failed (bug) |
```

But the traceability matrix and README both show TC002 as `Passed`. This contradiction is never resolved in the project documentation.

### 6.5 `ruff.toml` and `pyproject.toml` Overlap

The project has both a standalone `ruff.toml` and a `[tool.mypy]` / `[tool.pytest.ini_options]` section in `pyproject.toml`. The `ruff.toml` is empty by inspection (no content beyond what `pyproject.toml` would cover). Having two configuration files for the same tool can cause unexpected behavior depending on ruff's config discovery order.

---

## 7. Prioritized Improvement Roadmap

### Priority 1 — Immediate (Blocking Real iOS QA Work)

| # | Action | File(s) |
|---|--------|---------|
| 1 | Replace Selenium tests with Appium or Detox for native mobile testing | `automation/tests/test_search_valid.py`, `test_search_empty.py` |
| 2 | Write test case specification files for TC004–TC007 | `manual-tests/test-cases/` |
| 3 | Perform and document real iOS test execution; fill in all execution log templates | `manual-tests/test-execution/execution-logs/` |
| 4 | Fix `AttributeError` bug — add `BASE_URL` to `TestManualTestingSupport` | `automation/tests/test_search_api.py` |
| 5 | Add iOS-specific preconditions to all existing test cases | `TC001`, `TC002`, `TC003` |

### Priority 2 — Short Term (Coverage and Evidence Quality)

| # | Action | File(s) |
|---|--------|---------|
| 6 | Create iOS-specific test cases: VoiceOver, Dynamic Type, Dark Mode, Safe Area | New test cases |
| 7 | Add real video evidence links and screenshots | `traceability-with-evidence.md`, `execution-summary.md` |
| 8 | Add a macOS agent pool stage to the CI pipeline for iOS builds | `azure-pipelines.yml` |
| 9 | Remove `markdownlint-cli2` from `requirements.txt`; install via `npm` in pipeline | `automation/requirements.txt` |
| 10 | Set `continueOnError: false` on `pytest` and `mypy` pipeline steps | `azure-pipelines.yml` |

### Priority 3 — Medium Term (Process and Architecture)

| # | Action | File(s) |
|---|--------|---------|
| 11 | Replace `time.sleep()` with explicit waits in automation tests | Both Selenium test files |
| 12 | Reconcile TC002 status conflict between `coverage_summary.md` and traceability matrix | Both files |
| 13 | Add TC004, TC009, TC010 offline/network test executions | New execution logs |
| 14 | Define performance thresholds (e.g., 5-second search response) in TC001 | `TC001_search_valid.md` |
| 15 | Add iOS device configuration section to ADO integration guide | `ado-integration/workflow_guide.md` |
| 16 | Merge or consolidate `ruff.toml` into `pyproject.toml` | `ruff.toml` |

### Priority 4 — Long Term (Non-Functional and Accessibility)

| # | Action |
|---|--------|
| 17 | Add WCAG 2.1 AA accessibility validation steps to core test cases |
| 18 | Define iOS performance benchmarks by device class (iPhone SE vs. iPhone 15 Pro) |
| 19 | Document TestFlight beta distribution and regression testing process |
| 20 | Add memory leak and battery usage observations to execution logs |

---

## 8. Metrics Summary

| Dimension | Current State | Target State |
|-----------|--------------|--------------|
| Test cases with specification files | 3 / 10 (30%) | 10 / 10 (100%) |
| Test cases with real execution logs | 0 / 3 (0%) | 3 / 3 (100%) |
| iOS-specific test cases | 0 (TC006 unwritten) | ≥ 5 |
| Video evidence links (real) | 0 | ≥ 6 (both platforms per case) |
| Automation tests that can run on iOS | 0 | TC001, TC002, TC003 |
| CI stages covering macOS / Xcode | 0 | 1 |
| Feature coverage (PDF Management) | 0% | ≥ 50% |
| Overall feature coverage | 45% | ≥ 80% |

---

## 9. Appendix: File Inventory

| File | Purpose | Completeness |
|------|---------|--------------|
| `manual-tests/test-cases/TC001_search_valid.md` | Test spec | Partial — iOS preconditions missing |
| `manual-tests/test-cases/TC002_empty_query.md` | Test spec | Partial — duplicate step entry |
| `manual-tests/test-cases/TC003_toggle_favorite.md` | Test spec | Partial — iOS preconditions missing |
| `manual-tests/test-execution/execution-logs/TC001_execution_log.md` | Execution record | Template only |
| `manual-tests/test-execution/execution-logs/TC002_execution_log.md` | Execution record | Template only |
| `manual-tests/test-execution/execution-logs/TC003_execution_log.md` | Execution record | Template only |
| `manual-tests/test-execution/execution-summary.md` | Sprint summary | Template with false data |
| `manual-tests/test-execution/traceability-with-evidence.md` | Evidence links | All links are placeholders |
| `manual-tests/traceability-matrix.csv` | Requirements map | Inconsistencies in coverage column |
| `manual-tests/wiki/coverage_summary.md` | Coverage metrics | Contradicts other docs on TC002 |
| `manual-tests/testability_notes.md` | Live feedback | Complete — 3 real observations |
| `manual-tests/testability-feedback/requirements_analysis.md` | QA feedback | Complete — well structured |
| `manual-tests/ado-integration/workflow_guide.md` | ADO guide | Complete — no iOS device config |
| `automation/tests/test_search_api.py` | API tests | Functional but has `AttributeError` bug |
| `automation/tests/test_search_valid.py` | UI test | Wrong framework (Selenium) |
| `automation/tests/test_search_empty.py` | UI test | Wrong framework (Selenium) |
| `automation/ci/azure-pipelines.yml` | CI pipeline | Missing iOS stage, quality gates disabled |
| `TESTING_WORKFLOW.md` | Workflow guide | Complete |
| `TESTING_CHECKLIST.md` | Run checklist | Entirely unchecked |
| `setup-app.sh` | Environment setup | Complete — iOS-aware on macOS |
