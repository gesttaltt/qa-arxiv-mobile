# QA Portfolio – Market Gap Analysis
## Alignment with Junior QA Tester Requirements (2025–2026)

**Research basis:** LinkedIn job postings and career pages from MentorMate, Tietoevry, EPAM,
SoftServe, and Endava; supplemented by Coursera, LeadWithSkills, Quash, and CV compiler data.
**Date:** April 2026  
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
| Manual test cases (ADO-style) | `manual-tests/test-cases/TC001–TC003` | Good |
| Execution logs with evidence | `manual-tests/test-execution/` | Good |
| Traceability matrix | `manual-tests/traceability-matrix.csv` | Good |
| Testability feedback | `manual-tests/testability-feedback/` | Good |
| ADO wiki documentation | `manual-tests/wiki/` | Moderate |
| API test automation (Python/pytest) | `automation/tests/test_search_api.py` | Moderate |
| Azure Pipelines CI/CD | `automation/ci/azure-pipelines.yml` | Good |
| Code quality tooling | `ruff.toml`, `pyproject.toml`, `yamllint`, `markdownlint` | Good |
| Coverage reporting | `azure-pipelines.yml` (Cobertura) | Basic |

---

## 3. Gap Analysis by Skill Area

### 3.1 Mobile Test Automation — CRITICAL GAP

**Market demand:** MentorMate specifically hires Senior QA Engineers with a "strong background in
mobile application testing for Android and iOS." Tietoevry Junior QE posting requires UI
test automation tools. Appium is the standard for mobile automation.

**Current state:** Zero mobile automation code. Test cases mention "Android emulator" but no
automated UI or Appium tests exist. For a project whose entire purpose is mobile QA, this is
the most visible gap to any interviewer.

**What to add:**
- At least one Appium test that launches the app, runs a search, and asserts a result appears
- Device/emulator configuration file (capabilities JSON or `conftest.py` fixture)
- Screenshot-on-failure capability
- A brief `APPIUM_SETUP.md` covering prerequisites (Node, Appium server, emulator)

---

### 3.2 UI Automation Framework — HIGH GAP

**Market demand:** Tietoevry Junior QE: "implement simple automated test cases using UI Test
Automation tools like Selenium, Cypress or Playwright." EPAM campus program lists Selenium,
TestNG, JUnit, Cypress, and Playwright as expected tools.

**Current state:** All existing automation is API-level (HTTP requests to arXiv API). There is
no browser or UI automation layer whatsoever.

**What to add:**
- Even a minimal Playwright or Cypress smoke test for the web-facing arXiv API interface
  demonstrates understanding of UI automation concepts
- Alternatively, expand the Appium work (above) to serve as the UI automation showcase since
  the target app is mobile

---

### 3.3 SQL / Database Testing — MODERATE GAP

**Market demand:** Tietoevry Junior QE: "SQL databases and database testing understanding."
EPAM: "basic knowledge of SQL and database concepts." Practically every junior posting lists
SQL as a required or strongly preferred skill.

**Current state:** No SQL, no database, no data-validation layer in the project.

**What to add:**
- A `test_data_validation.py` module that queries the arXiv Atom XML response and validates
  data types, field presence, and format (simulates what a SQL validation step would do against
  a backend DB)
- A markdown document showing example SQL queries a QA tester would run to validate app data
  (even if the app itself has no database, demonstrating the concept in a README section adds
  visible signal)

---

### 3.4 Postman / API Testing Visibility — MODERATE GAP

**Market demand:** Postman is the single most cited API testing tool across all 2025–2026 job
postings reviewed. Even Tietoevry's junior posting expects "good API and API testing notions."

**Current state:** API testing exists in Python (`requests` library) but there is no Postman
collection visible in the repo. Recruiters scanning a portfolio specifically look for a
Postman collection as proof of tool familiarity.

**What to add:**
- Export an actual Postman collection (`arXiv_API.postman_collection.json`) covering:
  - Valid search request + response assertion
  - Empty query edge case
  - Rate limit / error response
- Include the collection in `automation/` with a short usage note in README

---

### 3.5 iOS Coverage — MODERATE GAP

**Market demand:** MentorMate Senior QA Mobile posting requires "Android and iOS" coverage.
Every mobile QA job description reviewed listed both platforms.

**Current state:** Test cases only reference "Android emulator or device." iOS is mentioned in
README but no test case, execution log, or test plan entry covers iOS.

**What to add:**
- Duplicate TC001–TC003 with iOS-specific notes (different simulator, iOS-specific UI quirks)
- Or add a "Platform Matrix" table in the traceability matrix documenting intended coverage vs.
  actual execution status per platform
- Document known platform differences (e.g., back navigation behavior differs between Android
  and iOS)

---

### 3.6 Negative / Edge Case Test Coverage — MODERATE GAP

**Market demand:** Junior QA testers are expected to apply test design techniques:
Equivalence Partitioning and Boundary Value Analysis. ISTQB Foundation Level formalizes these.

**Current state:** Only 3 test cases total (TC001 valid search, TC002 empty query, TC003
toggle favorite). TC002 is the only negative case. Coverage is very narrow.

**What to add:**
- TC004: Network offline / connectivity loss
- TC005: Special characters in search field (boundary + injection awareness)
- TC006: Very long search string (boundary value)
- TC007: Rapid consecutive searches (stress / stability)
- TC008: PDF download with no storage permission (permission handling)
- TC009: Search result with no PDF available
- Label each new TC with the design technique used (BVA, EP, Error Guessing, etc.)

---

### 3.7 ISTQB Concepts — Visibility Gap

**Market demand:** ISTQB Foundation Level is the most cited certification across all reviewed
postings. Tietoevry lists it as an "advantageous qualification." EPAM and general market data
list it as the single most recognised QA credential.

**Current state:** No mention of ISTQB anywhere in the project. Test cases do not reference
test design techniques by name.

**What to add:**
- A `docs/TESTING_THEORY.md` that maps the test cases in this project to ISTQB concepts:
  - STLC phases covered
  - Test design techniques applied per TC (EP, BVA, State Transition, Error Guessing)
  - Defect lifecycle (even if illustrated with hypothetical examples)
- This document doubles as interview prep and shows conceptual depth beyond tool usage

---

### 3.8 Defect Reporting Template — LOW-MODERATE GAP

**Market demand:** All job descriptions reference defect tracking (JIRA), defect lifecycle,
and the ability to write clear, reproducible bug reports.

**Current state:** Execution logs exist, but there is no formal defect report in the repo. A
reader cannot tell whether any actual defects were found or how they would be documented.

**What to add:**
- At least one realistic mock defect report following ADO/JIRA bug template:
  - Title, Environment, Severity/Priority, Steps to Reproduce, Actual vs Expected, Attachments
- Place in `manual-tests/defects/BUG001_sample_defect.md`
- Reference it from the traceability matrix

---

### 3.9 GitHub Actions — LOW GAP

**Market demand:** While Azure DevOps is the primary pipeline for MentorMate/Tietoevry,
many postings also list GitHub Actions, GitLab CI, or Jenkins. Showing CI/CD awareness
across more than one platform strengthens the portfolio.

**Current state:** Only Azure Pipelines. The project lives on GitHub but has no
`.github/workflows/` directory.

**What to add:**
- A minimal `.github/workflows/ci.yml` that runs `pytest` and linting on push — it can mirror
  the Azure Pipelines logic at a small scale
- This is a 30-line file and gives the repo a green checkmark badge on GitHub

---

### 3.10 Performance / Non-Functional Testing Awareness — LOW GAP

**Market demand:** Tietoevry Banking Automation Test Engineer posting lists JMeter as a bonus.
General market data cites performance testing as an "underrated skill" that differentiates
junior candidates.

**Current state:** Not represented at all. The TESTING_CHECKLIST.md references
"Network connectivity scenarios" but has no performance test cases.

**What to add:**
- TC010: Response time assertion (the arXiv API should return results in under 3 seconds)
  — implementable with `time.time()` in the existing pytest suite
- A short section in `docs/TESTING_THEORY.md` explaining performance testing categories
  (load, stress, soak) even if not fully implemented

---

### 3.11 Accessibility Testing — LOW GAP

**Market demand:** Emerging requirement in 2025–2026, particularly at companies with
healthcare or government clients (MentorMate is heavily health-tech focused). Not universal
at junior level but a differentiator.

**Current state:** Not mentioned.

**What to add:**
- TC011: Screen reader / TalkBack basic check on Android (manual, 1 test case)
- Reference WCAG 2.1 AA as the target standard in the test plan context

---

## 4. Prioritized Improvement Roadmap

| Priority | Area | Effort | Impact |
|---|---|---|---|
| 1 | Appium mobile automation (smoke test) | High | Critical |
| 2 | Expand test cases to TC004–TC009 (negative/edge) | Medium | High |
| 3 | Postman collection export | Low | High |
| 4 | ISTQB/testing theory doc | Low | High |
| 5 | Mock defect report (BUG001) | Low | Medium |
| 6 | iOS platform coverage notes | Low | Medium |
| 7 | GitHub Actions CI workflow | Low | Medium |
| 8 | SQL / data validation notes or test | Medium | Medium |
| 9 | Response time assertion in pytest | Low | Low–Medium |
| 10 | Accessibility TC (TalkBack) | Low | Low–Medium |

---

## 5. Skills Already Well-Represented

These areas are solid and should be maintained or expanded — they already match what
employers ask for:

- **ADO-style documentation** — test cases, execution logs, wiki, traceability matrix
- **Azure DevOps CI/CD integration** — azure-pipelines.yml is detailed and realistic
- **Python automation with pytest** — parametrized, structured, CI-integrated
- **Testability feedback** — requirement analysis and feedback notes show QA mindset beyond
  just execution
- **Code quality gates** — ruff, black, mypy, yamllint, markdownlint all in CI

---

## 6. Key Tools Reference Table

| Tool | Market Frequency | In Project | Action |
|---|---|---|---|
| JIRA | Universal | Referenced only | Add mock ticket IDs to defect report |
| Postman | Universal | Missing | Export collection |
| Selenium/Cypress/Playwright | Very high | Missing | Add via Appium (mobile) |
| Appium | High (mobile roles) | Missing | Add smoke test |
| TestRail / Zephyr | High | Missing | Markdown TCs partially substitute |
| Git | Universal | Yes (repo) | Already present |
| Azure DevOps | High (MentorMate/Tietoevry) | Yes (pipeline) | Already present |
| GitHub Actions | Moderate | Missing | Add `.github/workflows/` |
| SQL | High | Missing | Add validation notes |
| Java | High | Missing | Python compensates but note gap |
| Python | Moderate-high | Yes (pytest) | Already present |
| ISTQB | High (certification) | Missing | Add theory doc |

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
