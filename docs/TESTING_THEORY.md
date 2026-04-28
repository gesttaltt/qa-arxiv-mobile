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
| Postman – Author field | Author field query vs full-text query |

---

### Boundary Value Analysis (BVA)
Test at and just inside/outside the edges of each equivalence partition.

| Test Case | Boundary tested |
|---|---|
| TC008 – Bulk favorites | 0 items (below min), 1 item (minimum), 3+ items (multiple) |
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
| TC003 – Toggle favorite | Not-favorited → Favorited → Not-favorited |

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
the backend database. The arXiv Papers app stores favourites and downloaded paper metadata
locally (SQLite on device). The queries below illustrate what would be run against that
local DB or a staging backend.

```sql
-- Verify a favourited paper was persisted
SELECT id, title, is_favourite, date_favourited
FROM papers
WHERE is_favourite = 1;

-- Confirm no duplicate paper IDs exist after bulk operations (TC008)
SELECT paper_id, COUNT(*) AS occurrences
FROM favourites
GROUP BY paper_id
HAVING COUNT(*) > 1;

-- Validate required fields are never NULL (data quality gate)
SELECT id FROM papers
WHERE title IS NULL
   OR authors IS NULL
   OR published_date IS NULL;

-- Check paper count matches what is displayed in the Favourites tab (UI vs DB reconciliation)
SELECT COUNT(*) AS db_count FROM favourites WHERE user_id = 1;
-- Expected: matches the number of cards shown in the Favourites tab

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
| **Response time** | API round-trip under normal load | pytest (`time`), Postman | `test_search_api.py` — `test_api_response_time` |
| **Load testing** | Behaviour under expected concurrent users | JMeter, k6 | Not implemented (out of scope for junior portfolio) |
| **Stress testing** | Breaking point beyond normal load | JMeter | Not implemented |
| **Soak testing** | Stability over extended time | Custom script | Not implemented |

The response time assertion in this project establishes a baseline (< 3 s) for the
arXiv API and demonstrates awareness of non-functional requirements.

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
| **Unit** | Smallest testable unit in isolation | `test_favorites_data_structure` in `test_search_api.py` |
| **Integration** | Interaction between components | `test_search_valid_keyword_api_response` (app ↔ arXiv API) |
| **System** | End-to-end behaviour of the full system | All Appium smoke tests in `automation/tests/appium/` |
| **Acceptance** | Business requirements met | Manual TCs against real app build |

---

## 8. Test Types

| Type | Examples in this project |
|---|---|
| **Functional** | TC001–TC005, TC008–TC009 |
| **Non-functional (Performance)** | TC009, `test_api_response_time` |
| **Non-functional (Accessibility)** | TC011 |
| **Regression** | Re-running TC001–TC003 after any build change |
| **Smoke** | Appium tests in `automation/tests/appium/` |
| **Exploratory** | Postman collection — manual API exploration |
