# QA Portfolio – Market Gap Analysis
## Alignment with Junior QA Tester Requirements (2025–2026)

**Research basis:** LinkedIn job postings and career pages from MentorMate, Tietoevry, EPAM,
SoftServe, and Endava; supplemented by Coursera, LeadWithSkills, Quash, and CV compiler data.
**Date:** April 2026
**Last Updated:** June 2026
**Project:** qa-arxiv-mobile (React Native mobile app QA overlay)

---

## 1. Market Landscape Summary

Companies like **MentorMate** and **Tietoevry** represent the archetypal IT services/consulting
employer for junior QA roles. Their postings, alongside peers (EPAM, SoftServe, Endava), converge
on the same profile:

| Category | Market Expectation |
|---|---|
| Manual testing | Strong foundation — test case design, defect lifecycle, STLC |
| Test automation | At minimum awareness; UI automation (Selenium/Cypress/Playwright) preferred |
| API testing | Postman or Rest Assured; ability to validate status codes, response bodies |
| Mobile testing | iOS + Android coverage; Appium awareness for automation |
| CI/CD | Pipeline exposure (Azure DevOps, Jenkins, GitHub Actions) |
| Languages | Java or Python; basic OOP knowledge |
| Databases | SQL queries for data validation |
| Agile | Sprint ceremonies, JIRA usage, Agile vocabulary |
| Documentation | Test plans, traceability, ADO-style wiki |
| Certifications | ISTQB Foundation Level (widely mentioned as a differentiator) |

---

## 2. What This Project Currently Covers

| Area | Evidence in Repo | Strength |
|---|---|---|
| Manual test cases (ADO-style) | `manual-tests/test-cases/TC001–TC011` (11 TCs) | Strong |
| Execution logs with evidence | `manual-tests/test-execution/` — 28 GIFs + screenshots | Strong |
| Traceability matrix | `manual-tests/traceability-matrix.csv` — Automation Notes column | Strong |
| Testability feedback | `manual-tests/testability-feedback/` | Good |
| ADO wiki documentation | `manual-tests/wiki/coverage_summary.md` | Good |
| Defect reports | `manual-tests/defects/BUG001–BUG007` (7 reports) | Strong |
| API test automation (Python/pytest) | `automation/tests/` — 57 tests, 55% coverage | Strong |
| BDD / Gherkin automation | `automation/features/` (search + favorites) + `tests/bdd/` | Strong |
| Mobile UI automation (Appium) | `automation/pages/` POM + `tests/appium/` smoke tests | Good |
| ISTQB concepts reference | `docs/TESTING_THEORY.md` — STLC, EP, BVA, BDD, SQL, Defect lifecycle | Strong |
| XML / data validation | `automation/tests/test_data_validation.py` | Good |
| SQL data validation examples | `docs/TESTING_THEORY.md` §4 | Moderate |
| Performance testing | `TestPerformanceBaseline` — mock-based SLA; `TESTING_THEORY.md` §5 | Good |
| Accessibility testing | TC011 TalkBack; BUG007 WCAG 2.1 AA; `TESTING_THEORY.md` §6 | Good |
| Azure Pipelines CI/CD | `automation/ci/azure-pipelines.yml` | Good |
| GitHub Actions CI/CD | `.github/workflows/ci.yml` — full quality gates, green badge | Strong |
| Code quality tooling | Black, Ruff, mypy, yamllint, markdownlint — all in CI | Strong |
| Coverage reporting | Codecov badge; `--cov-fail-under=55` gate; 55% honest coverage | Good |

---

## 3. Gap Analysis by Skill Area

### 3.1 Mobile Test Automation — RESOLVED

**Market demand:** MentorMate specifically hires Senior QA Engineers with a "strong background in
mobile application testing for Android and iOS." Tietoevry Junior QE posting requires UI
test automation tools. Appium is the standard for mobile automation.

**Resolution (June 2026):** Page Object Model implemented with `BasePage`, `SearchPage`, and
`FavoritesPage` in `automation/pages/`. Two Appium smoke tests cover search and favorites flows
(`automation/tests/appium/`). `conftest.py` configures the Android emulator capabilities and
provides a screenshot-on-failure hook. `docs/APPIUM_SETUP.md` documents prerequisites.

---

### 3.2 UI Automation Framework — RESOLVED (via Appium)

**Market demand:** Tietoevry Junior QE: "implement simple automated test cases using UI Test
Automation tools like Selenium, Cypress or Playwright." EPAM campus program lists Selenium,
TestNG, JUnit, Cypress, and Playwright as expected tools.

**Resolution (June 2026):** Appium serves as the UI automation layer for the React Native mobile
app. Selenium/Cypress/Playwright were not added because the target app has no browser interface —
Appium is the correct and expected tool for mobile UI automation. The POM pattern (`BasePage` →
`SearchPage`/`FavoritesPage`) demonstrates the same structural thinking as a Selenium Page Object
framework.

---

### 3.3 SQL / Database Testing — RESOLVED

**Market demand:** Tietoevry Junior QE: "SQL databases and database testing understanding."
EPAM: "basic knowledge of SQL and database concepts." Practically every junior posting lists
SQL as a required or strongly preferred skill.

**Resolution (June 2026):** `automation/tests/test_data_validation.py` validates Atom XML
response data — field presence, types, and format — simulating what SQL assertions would verify
against a backend DB. `docs/TESTING_THEORY.md` §4 contains five concrete SQL examples
(favorites persistence, duplicate detection, NULL field validation, UI-DB reconciliation,
date format assertion) with commentary.

---

### 3.4 Postman / API Testing Visibility — RESOLVED

**Market demand:** Postman is the single most cited API testing tool across all 2025–2026 job
postings reviewed. Even Tietoevry's junior posting expects "good API and API testing notions."

**Resolution (June 2026):** `automation/postman/arXiv_API.postman_collection.json` contains
6 requests with `pm.test()` assertions covering TC001 (valid search — status, Content-Type,
body, response time), TC002 (empty query — no 5xx, response time), Equivalence Partitioning
(author field query), BVA (max\_results=1 boundary, start=1 pagination offset), and Error
Guessing (XSS special characters — server must not crash). Uses a `{{baseUrl}}` collection
variable for easy environment switching. Run via Newman CLI:
`newman run arXiv_API.postman_collection.json`

---

### 3.5 iOS Coverage — PARTIALLY RESOLVED

**Market demand:** MentorMate Senior QA Mobile posting requires "Android and iOS" coverage.
Every mobile QA job description reviewed listed both platforms.

**Resolution (June 2026):** All 11 test cases include iOS execution logs and 8 iOS GIFs. The
execution summary documents both platforms. iOS GIFs are honest placeholders labeled "Pending
macOS device" — a transparent acknowledgement of the hardware constraint rather than fabricated
evidence.

**Remaining gap:** No macOS CI stage for iOS simulator testing. No Appium fixture for iOS
(requires Xcode + WebDriverAgent). Documenting the gap honestly is the correct approach for a
portfolio without physical iOS hardware.

---

### 3.6 Negative / Edge Case Test Coverage — RESOLVED

**Market demand:** Junior QA testers are expected to apply test design techniques:
Equivalence Partitioning and Boundary Value Analysis. ISTQB Foundation Level formalizes these.

**Resolution (June 2026):** TC001–TC011 cover functional, integration, performance,
accessibility, and negative paths. `docs/TESTING_THEORY.md` §2 maps each TC to ISTQB design
techniques (EP, BVA, State Transition, Decision Table, Error Guessing). API parametrised tests
cover boundary values and edge cases in `test_search_api.py` and `test_data_validation.py`.

---

### 3.7 ISTQB Concepts — RESOLVED

**Market demand:** ISTQB Foundation Level is the most cited certification across all reviewed
postings. Tietoevry lists it as an "advantageous qualification." EPAM and general market data
list it as the single most recognised QA credential.

**Resolution (June 2026):** `docs/TESTING_THEORY.md` maps every TC in the project to ISTQB
Foundation Level concepts: STLC phase coverage (§1), test design techniques per TC (§2), defect
lifecycle with ADO states (§3), SQL data validation patterns (§4), performance testing categories
(§5), accessibility standards (§6), test levels (§7), test types (§8), and BDD methodology (§9).

---

### 3.8 Defect Reporting Template — RESOLVED

**Market demand:** All job descriptions reference defect tracking (JIRA), defect lifecycle,
and the ability to write clear, reproducible bug reports.

**Resolution (June 2026):** Seven defect reports filed in `manual-tests/defects/BUG001–BUG007`,
each following ADO/JIRA format: title, environment, severity/priority, steps to reproduce,
actual vs expected, and attachments. All 7 issues found during TC execution are formally
documented. BUG007 specifically covers a WCAG 2.1 AA accessibility gap.

---

### 3.9 GitHub Actions — RESOLVED

**Market demand:** While Azure DevOps is the primary pipeline for MentorMate/Tietoevry,
many postings also list GitHub Actions, GitLab CI, or Jenkins. Showing CI/CD awareness
across more than one platform strengthens the portfolio.

**Resolution (June 2026):** `.github/workflows/ci.yml` runs on every push — Black formatting,
Ruff linting, mypy type checking, yamllint, markdownlint, pytest with `--cov-fail-under=55`,
and Codecov upload. CI badge is green on `main`. Node.js 24 used (20 was deprecated).

---

### 3.10 Performance / Non-Functional Testing Awareness — RESOLVED

**Market demand:** Tietoevry Banking Automation Test Engineer posting lists JMeter as a bonus.
General market data cites performance testing as an "underrated skill" that differentiates
junior candidates.

**Resolution (June 2026):** `TestPerformanceBaseline` in `test_search_api.py` uses mock-based
SLA tests to validate the 3-second assertion logic under controlled fast (0.5 s) and slow
(3.5 s) conditions. `docs/TESTING_THEORY.md` §5 explains performance testing categories (load,
stress, soak, response time) with notes on why mock-based SLA tests are more meaningful than
measuring a third-party API in CI.

---

### 3.11 Accessibility Testing — RESOLVED

**Market demand:** Emerging requirement in 2025–2026, particularly at companies with
healthcare or government clients (MentorMate is heavily health-tech focused). Not universal
at junior level but a differentiator.

**Resolution (June 2026):** TC011 covers TalkBack screen reader on Android with GIF evidence.
BUG007 documents the missing `accessibilityRole` on result cards (WCAG 2.1 AA violation).
`docs/TESTING_THEORY.md` §6 references WCAG 2.1 AA and both Android TalkBack and iOS
VoiceOver standards.

---

### 3.12 BDD / Gherkin — NOT IN ORIGINAL ANALYSIS (Added June 2026)

**Market demand:** BDD is increasingly listed in junior QA postings as evidence of
collaboration between QA and non-technical stakeholders. Gherkin + a test framework
(Cucumber, pytest-bdd, Behave) is the standard combination.

**Current state (June 2026):** `automation/features/search.feature` contains 5 Gherkin
scenarios (TC001 valid search, TC002 empty query, Scenario Outline × 3 academic keywords).
`automation/tests/bdd/test_search.py` implements step definitions using pytest-bdd 7.3.0.
`docs/TESTING_THEORY.md` §9 explains BDD methodology and maps each scenario to a User Story.

---

## 4. Prioritized Improvement Roadmap

### Completed (April → June 2026)

| # | Area | Status |
|---|---|---|
| 1 | Appium mobile automation (smoke test + POM) | ✅ Done |
| 2 | Expand test cases to TC001–TC011 (negative/edge/accessibility) | ✅ Done |
| 3 | ISTQB/testing theory doc | ✅ Done (`docs/TESTING_THEORY.md`) |
| 4 | Formal defect reports (BUG001–BUG007) | ✅ Done |
| 5 | iOS platform coverage notes + GIFs | ✅ Done (honest placeholders) |
| 6 | GitHub Actions CI workflow with full quality gates | ✅ Done |
| 7 | SQL / data validation | ✅ Done (`test_data_validation.py` + theory §4) |
| 8 | Response time / SLA assertion (mock-based) | ✅ Done (`TestPerformanceBaseline`) |
| 9 | Accessibility TC (TalkBack) + defect | ✅ Done (TC011, BUG007) |
| 10 | BDD / Gherkin scenarios (pytest-bdd) | ✅ Done (added beyond original scope) |
| 11 | Honest coverage reporting (55%, no pragma gaming) | ✅ Done (Codecov badge) |
| 12 | Postman collection (6 requests + pm.test() assertions) | ✅ Done (`automation/postman/`) |

### Remaining

| # | Area | Effort | Impact |
|---|---|---|---|
| 1 | iOS Appium fixture (requires macOS + Xcode) | High | Medium |
| 2 | macOS CI stage for iOS simulator | High | Low (hardware constraint) |

---

## 5. Skills Already Well-Represented

These areas are solid and should be maintained — they already match or exceed what employers ask for:

- **ADO-style documentation** — 11 test cases, execution logs, wiki, traceability matrix with Automation Notes
- **Azure DevOps CI/CD** — `azure-pipelines.yml` with standard syntax, critical steps blocking
- **GitHub Actions CI/CD** — full quality gate pipeline, green badge on `main`
- **Python automation with pytest** — parametrised, typed, BDD, mock-based, CI-integrated; 57 tests
- **BDD / Gherkin** — feature file + pytest-bdd step definitions; mapped to User Stories
- **Appium / POM** — SearchPage, FavoritesPage with BasePage; screenshot-on-failure
- **Testability feedback** — requirements analysis and feedback notes show QA mindset beyond execution
- **Code quality gates** — Black, Ruff, mypy, yamllint, markdownlint all blocking in CI
- **Coverage tooling** — Codecov integration, honest 55% (not gamed with pragmas)
- **ISTQB theory** — TESTING_THEORY.md maps every TC to Foundation Level concepts

---

## 6. Key Tools Reference Table

| Tool | Market Frequency | In Project | Status |
|---|---|---|---|
| JIRA | Universal | Referenced in defect reports | Present (conceptual) |
| Postman | Universal | `automation/postman/arXiv_API.postman_collection.json` | Present |
| Selenium/Cypress/Playwright | Very high | Not applicable (mobile app) | Appium substitutes |
| Appium | High (mobile roles) | POM + smoke tests | Present |
| pytest-bdd / Gherkin | Moderate-high | Feature file + step defs | Present |
| TestRail / Zephyr | High | Markdown TCs partially substitute | Conceptual |
| Git | Universal | Yes (repo) | Present |
| Azure DevOps | High (MentorMate/Tietoevry) | `azure-pipelines.yml` | Present |
| GitHub Actions | Moderate | `.github/workflows/ci.yml` | Present |
| SQL | High | `TESTING_THEORY.md` §4 + `test_data_validation.py` | Present (conceptual) |
| Java | High | Missing | Python compensates — note gap |
| Python | Moderate-high | Yes (57 pytest tests) | Present |
| ISTQB | High (certification) | `docs/TESTING_THEORY.md` | Present (theory) |
| Codecov | Low-Moderate | Yes — badge + `.codecov.yml` | Present |

---

## 7. Sources

Research conducted April 2026 from:

- [MentorMate Senior QA Mobile Engineer – Lever](https://jobs.lever.co/mentormate/722f8c50-3af0-428b-8011-0d31d735db25)
- [MentorMate Automation QA Engineer – Lever](https://jobs.lever.co/mentormate/25cae5dd-d59c-433b-a625-a48e7b516b0f)
- [Tietoevry Junior Quality Engineer – careers.tieto.com](https://careers.tieto.com/job/junior-quality-engineer-tietoevry-create-m-f-d-in-asuncion-paraguay-jid-350)
- [Tietoevry Automation Test Engineer (Banking) – careers.tieto.com](https://careers.tieto.com/job/automation-test-engineer-tietoevry-banking-in-pune-india-jid-278)
- [EPAM Campus – How to become Junior Software Test Engineer](https://campus.epam.com/en/skill/SoftwareTesting)
- [QA Career Roadmap 2026 – LeadWithSkills](https://www.leadwithskills.com/blogs/qa-career-roadmap-2026-junior-senior-roles)
- [QA Tester Career Path 2025 – Quash](https://quashbugs.com/blog/qa-tester-career-path-2025)
- [What Is a QA Tester 2026 – Coursera](https://www.coursera.org/articles/qa-tester)
- [13 QA Tester Resume Examples 2026 – CVCompiler](https://cvcompiler.com/qa-tester-resume-examples)
- [Adaface – Appium Automation Tester Job Description](https://www.adaface.com/job-descriptions/appium-automation-tester-job-description/)
