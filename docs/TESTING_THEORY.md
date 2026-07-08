# Testing Theory Reference

Maps every test case in this project to ISTQB Foundation Level concepts.
Use this document to explain test design decisions in interviews.

---

## 1. Software Testing Life Cycle (STLC) — Phase Coverage

| STLC Phase | Artefacts in this project |
|---|---|
| **Requirement Analysis** | `manual-tests/testability-feedback/requirements_analysis.md` |
| **Test Planning** | `TESTING_WORKFLOW.md`, `TESTING_CHECKLIST.md` |
| **Test Case Design** | `manual-tests/test-cases/TC001–TC011` |
| **Test Environment Setup** | `setup-app.sh`, `docs/APPIUM_SETUP.md` |
| **Test Execution** | `manual-tests/test-execution/`, `automation/tests/` |
| **Test Closure** | `manual-tests/wiki/coverage_summary.md`, `manual-tests/test-execution/execution-summary.md` |

---

## 2. Test Design Techniques — TC Mapping

### Equivalence Partitioning (EP)
Divide input into partitions where the system behaves the same for all values in a partition.
Test one value per partition rather than every possible input.

| Test Case | Partitions |
|---|---|
| TC001 – Valid search | **Valid partition:** keyword that returns results |
| TC002 – Empty query | **Invalid partition:** empty input |
| TC005 – PDF download | Valid PDF / no PDF available / network drop mid-download |
| Postman – Author field | `au:lecun` author query vs `all:lecun` full-text query |
| `TestPagination` | `start=0` (page 1) vs `start=5` (page 2) — distinct result page partitions |
| `TestAuthorSearch` | `au:bengio` (author field only) vs `all:bengio` (all fields) — quantitative EP: `au:` must return a strict subset |

---

### Boundary Value Analysis (BVA)
Test at and just inside/outside the edges of each equivalence partition.

| Test Case | Boundary tested |
|---|---|
| TC008 – Bulk downloaded papers | 0 items (below min), 1 item (minimum), 3+ items (multiple) |
| Postman – max_results=1 | Minimum meaningful result count |
| Postman – start=0 vs start=1 | Pagination offset edge |
| `test_data_validation.py` – field length | Empty string vs single character vs max-length title |

---

### State Transition Testing
Model the system as states and transitions; design tests to cover all valid transitions
and attempt invalid ones.

| Test Case | States / Transitions |
|---|---|
| TC004 – Search offline | WiFi active → WiFi disabled → Search attempted → WiFi restored |
| TC009 – WiFi to Cellular | WiFi → Cellular → Offline → WiFi (four states, six transitions) |
| TC003 – Download/remove | Not-downloaded → Downloaded → Not-downloaded |

---

### Decision Table Testing
Enumerate all combinations of conditions and their expected outcomes.
Best for business rules with multiple independent conditions.

| Test Case | Conditions | Outcomes |
|---|---|---|
| TC007 – Android intent | PDF viewer installed (Y/N) × default set (Y/N) | 3 distinct outcomes |

---

### Error Guessing
Use experience and intuition to predict likely failure points not covered by other techniques.

| Test Case | Guessed failure |
|---|---|
| TC004 – Offline search | App hangs instead of showing error (infinite spinner) |
| TC005 – PDF drop mid-download | Corrupt partial file left on device |
| Postman – Special characters | Server 500 on unescaped `<script>` in query param |
| TC007 – No viewer installed | Unhandled `ActivityNotFoundException` crash on Android |

---

### Platform-Specific Integration Testing
Validate platform-level integrations (OS APIs, system apps, hardware features).

| Test Case | Integration point |
|---|---|
| TC006 – iOS Safari PDF | iOS URL scheme handoff (`open in Safari`) |
| TC007 – Android intent | Android implicit intent → external PDF viewer |
| TC011 – TalkBack | Android Accessibility Service API |

---

## 3. Defect Lifecycle

```
New → Assigned → In Progress → Fixed → Re-test → Closed
                                  └──────────────► Reopen (if re-test fails)
```

| Status | Who acts |
|---|---|
| **New** | QA logs defect (JIRA/ADO) |
| **Assigned** | QA lead or dev lead assigns to a developer |
| **In Progress** | Developer investigates and fixes |
| **Fixed** | Developer marks fixed; build is deployed to test env |
| **Re-test** | QA re-executes the original failing steps |
| **Closed** | QA confirms fix; closes the ticket |
| **Reopen** | QA re-opens if the fix is incomplete or introduces a regression |

Sample defect in this project: `manual-tests/defects/BUG001_sample_defect.md`

---

## 4. SQL Data Validation

A QA tester uses SQL to validate that data shown in the UI matches what is stored in
the backend database. The arXiv Papers app stores downloaded paper metadata
locally (SQLite on device). The queries below illustrate what would be run against that
local DB or a staging backend.

```sql
-- Verify a downloaded paper was persisted
SELECT id, title, is_downloaded, date_downloaded
FROM papers
WHERE is_downloaded = 1;

-- Confirm no duplicate paper IDs exist after bulk operations (TC008)
SELECT paper_id, COUNT(*) AS occurrences
FROM downloads
GROUP BY paper_id
HAVING COUNT(*) > 1;

-- Validate required fields are never NULL (data quality gate)
SELECT id FROM papers
WHERE title IS NULL
   OR authors IS NULL
   OR published_date IS NULL;

-- Check paper count matches what is displayed in the DOWNLOADED tab (UI vs DB reconciliation)
SELECT COUNT(*) AS db_count FROM downloads WHERE user_id = 1;
-- Expected: matches the number of cards shown in the DOWNLOADED tab

-- Validate date format (ISO 8601)
SELECT id, published_date FROM papers
WHERE published_date NOT LIKE '____-__-__T__:__:__Z';
```

These queries serve as **data layer assertions** — complementing the UI tests in
`automation/tests/appium/` and the API tests in `automation/tests/test_search_api.py`.

---

## 5. Performance Testing Categories

| Category | What it measures | Tool | Covered in project |
|---|---|---|---|
| **Response time** | SLA assertion logic under simulated latency | pytest + `unittest.mock` | `test_search_api.py` — `TestPerformanceBaseline` |
| **Load testing** | Behaviour under expected concurrent users | JMeter, k6 | Not implemented (out of scope for junior portfolio) |
| **Stress testing** | Breaking point beyond normal load | JMeter | Not implemented |
| **Soak testing** | Stability over extended time | Custom script | Not implemented |

`TestPerformanceBaseline` uses mocks to simulate 0.5 s (fast) and 3.5 s (slow) responses
and asserts that the SLA check logic correctly detects each case. Measuring arXiv's actual
server speed in CI is not meaningful — it is a third-party service outside our control.

---

## 6. Accessibility Testing

| Standard | Scope | Covered in project |
|---|---|---|
| WCAG 2.1 AA | Web + mobile (React Native) | TC011 – TalkBack manual check |
| Android TalkBack | Screen reader for Android | TC011 |
| iOS VoiceOver | Screen reader for iOS | Not yet covered |

See `manual-tests/test-cases/TC011_accessibility_talkback.md`.

---

## 7. Test Levels

| Level | Definition | Examples in this project |
|---|---|---|
| **Unit** | Smallest testable unit in isolation | `TestArxivGetRetry` in `test_utils.py` — mocks HTTP and `time.sleep` to test retry logic in isolation |
| **Integration** | Interaction between components | `test_search_valid_keyword_api_response` (app ↔ arXiv API); `TestArticleDataContract` (API contract) |
| **System** | End-to-end behaviour of the full system | All Appium smoke tests in `automation/tests/appium/` |
| **Acceptance** | Business requirements met | BDD scenarios in `search.feature` + `article_data_contract.feature`; manual TCs against real app build |

---

## 8. Test Types

| Type | Examples in this project |
|---|---|
| **Functional** | TC001–TC005, TC008–TC009 |
| **Non-functional (Performance)** | TC009; `TestPerformanceBaseline` in `test_search_api.py` (mock-based SLA validation) |
| **Non-functional (Accessibility)** | TC011 |
| **Regression** | Re-running TC001–TC003 after any build change |
| **Smoke** | Appium tests in `automation/tests/appium/` |
| **Exploratory** | Postman collection — manual API exploration |
| **BDD/Acceptance** | Gherkin scenarios in `search.feature` + `article_data_contract.feature` executed via pytest-bdd |

---

## 9. Behaviour-Driven Development (BDD)

BDD extends test-driven development by expressing test scenarios in natural language
(Gherkin) that both technical and non-technical stakeholders can read and validate.
This removes the translation layer between business requirements and test code.

### Gherkin structure

Given–When–Then steps map directly to: precondition, action, and expected outcome.

```gherkin
Feature: arXiv paper search

  Scenario: Valid keyword returns results
    Given I have access to the arXiv search API
    When I search for "machine learning"
    Then the response status is 200
    And the response contains at least 1 paper
    And each paper has a non-empty title
```

### BDD vs traditional test cases

| Aspect | ADO/JIRA Test Case | BDD Scenario |
|---|---|---|
| Author | QA engineer | QA + Product Owner |
| Language | Technical steps | Plain English |
| Traceability | Manual linkage to User Stories | Implicit in the scenario title |
| Step re-use | None | `Given I have access to the arXiv search API` shared across all scenarios |
| Parametrisation | Separate test cases per variant | `Scenario Outline` with `Examples` table |

### Implementation in this project

| File | Role |
|---|---|
| `automation/features/search.feature` | Gherkin scenarios covering TC001, TC002, and a Scenario Outline × 3 keywords |
| `automation/features/article_data_contract.feature` | Gherkin scenarios covering TC003 (field contract) and TC008 (bulk uniqueness) |
| `automation/tests/bdd/test_search.py` | pytest-bdd step definitions for search scenarios |
| `automation/tests/bdd/test_article_data.py` | pytest-bdd step definitions for article data contract scenarios |

Step definitions use a shared `result` dict fixture to pass state between
Given/When/Then steps without global variables:

```python
@pytest.fixture
def result() -> dict:
    return {}

@when(parsers.parse('I search for "{keyword}"'))
def search_for_keyword(result: dict, keyword: str) -> None:
    result["response"] = arxiv_get({"search_query": f"all:{keyword}", ...})

@then("the response contains at least 1 paper")
def has_at_least_one_result(result: dict) -> None:
    entries = ET.fromstring(result["response"].content).findall(...)
    assert len(entries) >= 1
```

The `Scenario Outline` demonstrates parametrised BDD — one scenario template runs
against multiple data rows (quantum physics, neural networks, computer science),
generating three independent pytest functions automatically.

### BDD coverage map

| User Story | Gherkin Scenario | Automated test ID |
|---|---|---|
| US001 (TC001) | Valid keyword returns results | `test_valid_keyword_returns_results` |
| US001 (TC002) | Empty query is handled gracefully | `test_empty_query_is_handled_gracefully` |
| US001 (TC001 ×3) | Popular academic topics — quantum physics | `test_popular_academic_topics_all_return_results[quantum physics]` |
| US001 (TC001 ×3) | Popular academic topics — neural networks | `test_popular_academic_topics_all_return_results[neural networks]` |
| US001 (TC001 ×3) | Popular academic topics — computer science | `test_popular_academic_topics_all_return_results[computer science]` |
| US002 (TC003) | A search result contains all fields needed to display an article | `test_a_search_result_contains_all_fields_needed_to_display_an_article` |
| US002 (TC008) | Multiple results all provide complete article data | `test_multiple_results_all_provide_complete_article_data` |

---

## 10. Mock-Based Unit Testing

A **unit test** exercises a single unit of code in complete isolation — no network, no
database, no device. Dependencies are replaced with **test doubles** (mocks, stubs, fakes)
that the test controls entirely.

### The Testing Pyramid

```
        ┌──────────────────────┐
        │   E2E / Appium       │  Few, slow — require real device
        ├──────────────────────┤
        │   Integration (API)  │  Real HTTP calls, no device
        ├──────────────────────┤
        │   Unit / Mock        │  Many, fast — no network, no device
        └──────────────────────┘
```

| Layer | Files in this project | Speed | Device needed |
|---|---|---|---|
| **Unit** | `test_utils.py` | < 15 s | No |
| **Integration** | `test_search_*.py`, `test_data_validation.py`, `test_pdf_contract.py`, `test_advanced_search.py` | ~80 s | No |
| **E2E** | `tests/appium/test_search_smoke.py`, `test_downloaded_smoke.py` | Minutes | Yes (BrowserStack) |

### Coverage scope — honest over inflated

Page objects (`SearchPage`, `DownloadedPage`, `BasePage`) require a live Appium session to
execute their method bodies. Rather than replacing the driver with `MagicMock` to hit an
artificial 100% figure, the project excludes `automation/pages/` from coverage measurement.

Coverage is reported only for `automation/tests/utils.py` — the retry logic that runs without
any external dependency. 4 unit tests cover all branches:

```python
# test_utils.py — real behaviour, no device needed
def test_retries_once_on_429_then_succeeds(mock_sleep, mock_get):
    mock_get.side_effect = [Mock(status_code=429), Mock(status_code=200)]
    result = arxiv_get({"search_query": "q"})
    assert result.status_code == 200
    assert mock_get.call_count == 2
```

### What this means for the project

| Scope | Coverage | Gate |
|---|---|---|
| `automation/tests/utils.py` (retry logic) | **100%** | `--cov-fail-under=100` in CI |
| `automation/pages/` (POM) | excluded | verified by Appium tests on BrowserStack |

The `--cov-fail-under=100` gate is preserved — it applies to the measurable, device-independent
code. Page objects are validated by real Appium tests running against a Samsung Galaxy S22 on
BrowserStack App Automate, not by mocks.
