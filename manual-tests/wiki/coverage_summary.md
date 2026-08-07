# Test Coverage Summary

## Executive Summary

Comprehensive test coverage analysis for arxiv-papers-mobile application focusing on manual testing execution, traceability maintenance, and quality assurance metrics.

## Coverage Metrics

### Feature Coverage

| Feature Area | Test Cases | Executed | Passed | Failed | Coverage % |
|--------------|------------|----------|--------|--------|------------|
| Search | 6 | 4 | 4 | 0 | 67% (TC014, TC016 added 2026-08-07, not executed) |
| Article Data / Downloaded | 2 | 2 | 2 | 0 | 100% |
| PDF Management | 5 | 2 | 2 | 0 | 40% (TC006 not executed — iOS-only, no device available; TC012, TC013 added 2026-08-07, not executed) |
| Network Handling | 3 | 2 | 2 | 0 | 67% (TC015 added 2026-08-07, not executed) |
| **Total** | **16** | **10** | **10** | **0** | **63%** (6 not executed: TC006 + TC012–TC016) |

### Platform Coverage

| Platform | Test Cases | Executed | Pass Rate |
|----------|------------|----------|-----------|
| Android | 15 (applicable — excludes TC006, iOS-only) | 10 | 67% (TC012–TC016 added 2026-08-07, not yet executed on any platform) |
| iOS | 16 | 0 | N/A — no macOS/Xcode/iOS Simulator available; test cases designed but never executed |
| Cross-Platform (design scope) | 12 (7 previously tracked + 5 added 2026-08-07: TC012–TC016) | 7 on Android only | 58% (Android, of 12); iOS unexecuted; the 5 new TCs are unexecuted on both platforms |

### Test Type Distribution

| Test Type | Count | % of 57 automated |
|-----------|-------|-------------------|
| Functional (manual) | 11 | 19% |
| API integration (pytest) | 46 | 81% |
| Retry / unit (mock-based) | 4 | 7% |
| BDD / Gherkin (pytest-bdd) | 7 | 12% |
| Performance / SLA (mock-based) | 2 | 4% |

> Totals exceed 100% because BDD and SLA tests overlap in scope with API integration and manual test cases.
> Performance / SLA (2) is a subset of API integration (46), shown separately for emphasis.

## Quality Metrics

### Defect Analysis

- **Total Issues Found**: 7 (all low severity UX improvements)
- **Critical**: 0
- **High**: 0
- **Medium**: 0
- **Low**: 6
- **Defect Reports Filed**: 6 real reports from execution (BUG002–BUG007, in `manual-tests/defects/`). BUG001 in the same folder is a pre-execution format template (severity "Major," never observed) — see the banner in that file; not counted here.

### Test Execution Summary

- **Manual test cases**: 10 executed on Android, 10 passed; 6 not executed — TC006 (iOS-only, no macOS/Xcode/iOS Simulator available) plus TC012–TC016 (added 2026-08-07, designed but not yet run on any platform)
- **Automated API + unit tests**: 50 passing (pytest, runs in CI on every push)
- **BDD scenarios**: 7 passing (pytest-bdd, Gherkin feature files: search + article_data_contract)
- **Total automated**: 57 (excludes 7 Appium tests — run in CI on a local Android emulator, confirmed passing; 1 @slow excluded from regular CI runs)
- **Code coverage**: 100% on `automation/tests/utils.py` (11 statements, retry logic); page objects excluded — require real device, verified passing by Appium tests on a local emulator; gate at `--cov-fail-under=100`
- **CI pipeline**: GitHub Actions — green badge on `main`
- **Average manual execution time**: ~15 minutes per test case

## Traceability Status

All test cases properly linked to user stories with bidirectional traceability.

- Total User Stories: **4** (US001–US004)
- Manual Test Cases: **16** (TC001–TC016; 10 executed)
- Automated Test Cases: **57** (50 API/unit + 7 BDD, excludes 7 Appium — run on a local Android emulator)
- Traceability Matrix: ✅ Present (`manual-tests/traceability-matrix.csv`)
- CI Pipeline: ✅ GitHub Actions (`.github/workflows/ci.yml` — active, green badge)
- ADO Pipeline: ✅ Azure Pipelines config (`automation/ci/azure-pipelines.yml`)
- Code Quality: ✅ Black, Ruff, mypy, markdownlint, yamllint

## Coverage Map

| User Story | Manual Test Case | API Automated | BDD Automated | Notes |
|------------|-----------------|---------------|---------------|-------|
| US001 – Search valid | TC001 | ✅ Yes | ✅ Yes | `test_search_api.py`, `test_search_valid.py`, `test_advanced_search.py` (pagination + author EP), `features/search.feature` |
| US001 – Empty query | TC002 | ✅ Yes | ✅ Yes | `test_search_empty.py`, `features/search.feature` |
| US001 – Offline search | TC004 | ❌ No | ❌ No | Manual only |
| US001 – Accessibility | TC011 | ❌ No | ❌ No | Manual only (TalkBack) |
| US002 – Download/remove | TC003 | ✅ Partial | ✅ Partial | API: `test_search_api.py` (field contract); BDD: `article_data_contract.feature` scenario 1 |
| US002 – Bulk downloaded papers | TC008 | ✅ Partial | ✅ Partial | API: `test_search_api.py`; BDD: `article_data_contract.feature` scenario 2 (bulk uniqueness) |
| US003 – PDF download | TC005 | ✅ Partial | ❌ No | API contract: `test_pdf_contract.py` (PDF link presence + URL pattern) |
| US003 – iOS Safari | TC006 | ✅ Partial | ❌ No | API contract: `test_pdf_contract.py` (abstract link presence + URL pattern) |
| US003 – Android intent | TC007 | ✅ Partial | ❌ No | API contract: `test_pdf_contract.py` (PDF link href that Android intent consumes) |
| US004 – WiFi to cell | TC009 | ❌ No | ❌ No | Manual only |
| US004 – Offline persist | TC010 | ❌ No | ❌ No | Manual only |
| US003 – Cancel download | TC012 | ❌ No | ❌ No | Not executed — formalizes known gap BUG003 |
| US003 – Storage full | TC013 | ❌ No | ❌ No | Not executed — requires real device storage manipulation |
| US001 – Airplane mode mid-request | TC014 | ❌ No | ❌ No | Not executed — requires precisely-timed device network control |
| US004 – Slow network throttling | TC015 | ❌ No | ❌ No | Not executed — requires real device/simulator throttling |
| US001 – 429/503 errors | TC016 | ✅ Partial | ❌ No | Unit: `test_utils.py` (`TestArxivGetRetry`) covers retry logic; UI-level rendering not executed |

## Observations

- Manual QA coverage is complete for 10 of 16 test cases on Android, with real GIF evidence; TC006 (iOS-only) was never executed, and TC012–TC016 (added 2026-08-07) are designed but not yet run on any platform
- API automation covers the data layer for Search (TC001, TC002) and article data contract (TC003)
- BDD scenarios in `automation/features/search.feature` bridge TC001/TC002 to Gherkin, readable by non-technical stakeholders
- SLA logic tested deterministically via mocks — not subject to network variability
- Retry logic (`arxiv_get()` 429 backoff) covered by 4 dedicated mock-based unit tests in `automation/tests/test_utils.py`, which is also the automated layer backing TC016
- Offline and UI-only flows (TC004, TC005–TC011, TC012–TC016) remain manual-only, appropriate for scenarios that depend on device state

---

*This document simulates an ADO Wiki QA Summary page updated each sprint.*
