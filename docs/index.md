---
title: Home
nav_order: 1
---

# QA – arXiv Papers Mobile

Quality Assurance documentation for the [arxiv-papers-mobile](https://github.com/lopespm/arxiv-papers-mobile) React Native app.

This site is auto-generated from the `docs/` folder on every push to `main`.

---

## Contents

| Document | Description |
|---|---|
| [Testing Theory](TESTING_THEORY) | ISTQB concepts, design techniques, defect lifecycle, SQL validation, and TC mapping |
| [Appium Setup](APPIUM_SETUP) | How to run mobile UI automation tests end-to-end |
| [Market Gap Analysis](MARKET_GAP_ANALYSIS) | Skills gap vs MentorMate / Tietoevry / EPAM junior QA requirements |
| [QA Audit](QA_AUDIT) | Project-level quality audit findings |

---

## Test Cases

Manual test cases are in [`manual-tests/test-cases/`](https://github.com/gesttaltt/qa-arxiv-mobile/tree/main/manual-tests/test-cases).

| ID | Title | Technique | Platform |
|---|---|---|---|
| TC001 | Search with valid keyword | Equivalence Partitioning | Both |
| TC002 | Search with empty query | Equivalence Partitioning | Both |
| TC003 | Toggle paper as favourite | State Transition | Both |
| TC004 | Search offline behavior | State Transition + Error Guessing | Both |
| TC005 | PDF download and viewing | Equivalence Partitioning | Both |
| TC006 | iOS Safari PDF integration | Platform Integration | iOS |
| TC007 | Android intent handling | Decision Table | Android |
| TC008 | Bulk favourite operations | Boundary Value Analysis | Both |
| TC009 | WiFi to Cellular transition | State Transition | Both |
| TC010 | Offline data persistence | State Transition + Error Guessing | Both |
| TC011 | Accessibility – TalkBack | Platform Integration | Android |

---

## Automation

57 automated tests (50 API/unit + 7 BDD) — 100% coverage on `utils.py`, enforced in CI.

- **API + unit tests** — `automation/tests/` (50 tests: integration, SLA, contract, retry logic, pagination, author search)
- **BDD / Gherkin** — `automation/features/` (`search.feature` + `favorites.feature`) + `automation/tests/bdd/`
- **Mobile UI (Appium)** — `automation/tests/appium/` (Page Object Model, 7 tests; runs in CI via BrowserStack App Automate — Samsung Galaxy S22, Android 12)
- **Postman collection** — `automation/postman/arXiv_API.postman_collection.json` (8 requests, Newman CLI)
- **CI/CD** — GitHub Actions (`.github/workflows/ci.yml`) + Azure Pipelines (`automation/ci/azure-pipelines.yml`)
