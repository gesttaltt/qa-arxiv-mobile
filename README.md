# QA for Arxiv Papers Mobile App

[![CI](https://github.com/gesttaltt/qa-arxiv-mobile/actions/workflows/ci.yml/badge.svg)](https://github.com/gesttaltt/qa-arxiv-mobile/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/gesttaltt/qa-arxiv-mobile/graph/badge.svg)](https://codecov.io/gh/gesttaltt/qa-arxiv-mobile)
![Python](https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Appium](https://img.shields.io/badge/Appium-BrowserStack%20%28best--effort%29-blue?logo=appium&logoColor=white)
![BDD](https://img.shields.io/badge/BDD-Gherkin%20%2B%20pytest--bdd-23D96C?logo=cucumber&logoColor=white)
![Tests](https://img.shields.io/badge/tests-57%20passing-4CAF50?logo=pytest&logoColor=white)

![pytest suite — 56 tests passing in CI](docs/pytest-ci-demo.gif)

> Fully documented testing emphasizing **manual QA** and **ADO-style traceability** over a real mobile application.

This repository contains a complete QA portfolio applied to the open-source [arxiv-papers-mobile](https://github.com/lopespm/arxiv-papers-mobile) React Native app — demonstrating the full testing lifecycle from requirements analysis through execution, defect reporting, and CI integration, following Azure DevOps enterprise practices.

---

## Skills Demonstrated

| Area | Details |
|------|---------|
| **Mobile Testing** | Manual execution on Android emulator (API 28) with `adb screenrecord`; offline, network, and accessibility scenarios |
| **Test Design** | 11 ADO-format test cases covering functional, edge-case, and platform-specific flows |
| **Traceability** | Bi-directional: User Stories → Test Cases → Evidence → Defects (CSV matrix + linked wiki) |
| **Defect Reporting** | 7 structured defect reports (BUG001–BUG007) with reproduction steps, severity, and fix suggestions |
| **CI/CD** | GitHub Actions pipeline with linting (Black, Ruff, mypy, markdownlint), pytest quality gates, and green badge; Azure Pipelines config included for ADO environments |
| **Accessibility** | TC011 TalkBack navigation; WCAG 2.1 AA gap identified in BUG007 (`accessibilityRole` missing) |
| **Test Automation** | pytest API layer (57 tests, 100% coverage on utils.py); BDD scenarios in Gherkin (pytest-bdd); Page Object Model (Appium on BrowserStack); mock-based SLA tests; API contract validation |
| **Documentation** | ADO-style wiki, traceability matrix, execution logs, testability feedback notes |

---

## Target Application

**Name:** [arxiv-papers-mobile](https://github.com/lopespm/arxiv-papers-mobile)  
**Tech Stack:** React Native (Android/iOS)  
**Features:** Search for academic papers via arXiv API, view details, download papers for offline access

---

## Goals of This QA Project

- ✅ Define and execute **manual test cases** based on product requirements
- ✅ Maintain **test case traceability** to user stories and automated coverage
- ✅ Contribute to **test documentation** (ADO-style Wiki format)
- ✅ Provide **testability feedback** for future product improvement
- ✅ Showcase ability to collaborate with automation workflows

---

## Repository Structure

```
manual-tests/
├── test-cases/              # 11 ADO-format test cases
├── ado-integration/         # Azure DevOps workflow examples
├── testability-feedback/    # Requirement analysis and feedback
├── wiki/                   # ADO-style documentation
└── traceability-matrix.csv # Requirements-to-tests mapping
automation/
├── features/               # Gherkin feature files (pytest-bdd)
├── pages/                  # Page Object Model (SearchPage, DownloadedPage)
├── tests/                  # pytest API + BDD + Appium smoke tests
└── ci/                     # Azure Pipelines config (ADO environments)
.github/workflows/          # GitHub Actions CI (active pipeline)
docs/                       # pytest terminal recording GIF, audit docs
README.md                   # This file
```

## Azure DevOps Integration

This project demonstrates enterprise QA workflows using Azure DevOps methodologies:

### Test Management Framework
- **Test Plans**: Organized by feature areas (Search, Downloaded Papers, PDF Management)
- **Test Suites**: Grouped by platform (iOS/Android) and test type (Functional/Regression)
- **Work Items**: Each test case linked to corresponding User Stories and Tasks
- **Test Runs**: Execution history with pass/fail metrics and defect linking

### ADO Wiki Documentation
- Test case documentation following ADO Wiki markdown standards
- Requirement traceability matrices with hyperlinks to work items
- Test coverage reports integrated with build pipelines
- Sprint retrospectives and testing metrics

## Mobile Testing Approach

### Platform Coverage
- **Android Testing (executed)**: Multiple device sizes, Android API levels (21+); all applicable test cases recorded on a real emulator
- **iOS Testing (designed, not executed)**: Test cases are written to mirror the Android suite, but no macOS/Xcode/iOS Simulator was available — see "Platform coverage — how to frame it" below for the honest breakdown

### Mobile-Specific Test Areas
- Touch interactions and gestures
- Network connectivity scenarios (WiFi/Cellular/Offline)
- Device orientation changes (Portrait/Landscape)
- Background/Foreground app behavior
- Platform-specific UI/UX guidelines compliance

## Manual Test Cases

Located in `manual-tests/test-cases/` - Following ADO test case format

| ID    | Title                        | User Story | Platform | Status      |
|-------|------------------------------|------------|----------|-------------|
| TC001 | Search with valid keyword    | US001      | Android  | ✅ Passed (iOS not executed) |
| TC002 | Search with empty input      | US001      | Android  | ✅ Passed (iOS not executed) |
| TC003 | Download a paper and remove it | US002    | Android  | ✅ Passed (iOS not executed) |
| TC004 | Search offline behavior      | US001      | Android  | ✅ Passed (iOS not executed) |
| TC005 | PDF download and viewing     | US003      | Android  | ✅ Passed (iOS not executed) |
| TC006 | iOS Safari PDF integration   | US003      | iOS      | ⏸ Not Executed (no iOS device) |
| TC007 | Android intent handling      | US003      | Android  | ✅ Passed   |
| TC008 | Bulk downloaded papers mgmt  | US002      | Android  | ✅ Passed (iOS not executed) |
| TC009 | WiFi to cellular transition  | US004      | Android  | ✅ Passed (iOS not executed) |
| TC010 | Offline data persistence     | US004      | Android  | ✅ Passed (iOS not executed) |
| TC011 | Accessibility TalkBack       | US001/2/3  | Android  | ✅ Passed   |

### Test Case Structure (ADO Format)
Each test case includes:
- **Objective**: Clear test purpose aligned with acceptance criteria
- **Prerequisites**: Environment setup and test data requirements
- **Test Steps**: Detailed step-by-step execution instructions
- **Expected Results**: Specific validation criteria and success metrics
- **Actual Results**: Documented execution outcomes
- **Pass/Fail Status**: Clear verdict with defect linking
- **Linked Work Items**: Associated user stories, tasks, and bugs

📝 Each test case includes objective, steps, expected results, edge case considerations, and pass/fail field.

🔗 **Traceability Matrix:** Located at `manual-tests/traceability-matrix.csv`

This document links:

- User Stories (US001, US002, …)
- Manual Test Cases (TC001, …)
- Automation Test Scripts (if any)

### User Stories

| ID | Title | Description | Test Cases |
|----|-------|-------------|------------|
| US001 | Search for Academic Papers | As a user, I want to search for academic papers by keyword so that I can find relevant research. | TC001, TC002, TC004, TC011 |
| US002 | Manage Downloaded Papers | As a user, I want to download and manage papers for offline access so that I can read them without an internet connection. | TC003, TC008 |
| US003 | Download and View PDFs | As a user, I want to download and open PDF versions of papers so that I can read them offline or in external viewers. | TC005, TC006, TC007 |
| US004 | Network Connectivity | As a user, I want the app to handle network state changes gracefully so that I can continue using the app without data loss or crashes when connectivity changes. | TC009, TC010 |

## QA Methodology & SDLC Integration

### Testing Lifecycle
- **Requirements Analysis**: Participate in story refinement and acceptance criteria definition
- **Test Planning**: Create comprehensive test plans aligned with sprint goals
- **Test Design**: Develop test cases covering functional, usability, and edge cases
- **Test Execution**: Manual execution with detailed defect reporting
- **Defect Management**: Track issues through resolution using ADO work items

### Traceability Framework
- Forward Traceability: Requirements → Test Cases → Test Results
- Backward Traceability: Defects → Test Cases → Requirements
- Bi-directional linking maintained in Azure DevOps

## Requirement Reviews & Testability Feedback

### Participation in Story Refinement
- Review acceptance criteria for completeness and testability
- Identify edge cases and boundary conditions
- Suggest test data requirements and test environment needs
- Validate requirement clarity and measurability

### Testability Improvements Suggested
- **Search Feature**: Added error handling test scenarios
- **Downloaded Papers**: Suggested bulk operations testing
- **PDF Viewer**: Recommended accessibility testing considerations
- **Offline Mode**: Proposed sync behavior validation

Documentation: `manual-tests/testability-feedback/`

## Automation Layer

Located in `automation/tests/`

A few selected user flows are scripted using pytest, simulating how automation might extend QA coverage in collaboration with manual testers.

Also includes:

- `.github/workflows/ci.yml`: GitHub Actions pipeline (lint + test, runs on every push — see badge above)
- `automation/ci/azure-pipelines.yml`: Equivalent Azure DevOps pipeline for ADO environments
- `automation/features/search.feature`: Gherkin scenarios (TC001, TC002) with Scenario Outline for parametrised runs
- `automation/features/article_data_contract.feature`: Gherkin scenarios (TC003, TC008) validating API data requirements for article display and bulk uniqueness
- `automation/tests/bdd/test_search.py`, `test_article_data.py`: pytest-bdd step definitions; shared Given step and `result` fixture extracted to `bdd/conftest.py`
- `automation/pages/`: Page Object Model layer (SearchPage, DownloadedPage) for Appium tests on BrowserStack
- `automation/postman/arXiv_API.postman_collection.json`: Postman collection — 8 requests covering TC001, TC002, EP (author field, pagination offset, cross-request `au:` vs `all:` comparison via `pm.collectionVariables`), BVA (max\_results boundary, pagination edge), and Error Guessing (special characters); run with Newman CLI or Postman Collection Runner
- Modern Python tooling: ruff, black, mypy, pytest-cov, pytest-html, pytest-bdd
- Markdown and YAML linting integration
- Mock-based SLA tests and API contract validation for the Search and data validation features

### Appium — current status

The `test-appium` CI job runs against **BrowserStack App Automate** and is marked
`continue-on-error: true` — it does **not** block merges, and a green checkmark on the job does
**not** mean the 7 Appium tests actually passed. This is disclosed on purpose: BrowserStack's
free trial expired 2026-07-08, so the job errors on setup until the trial/plan is renewed. A
2026-07-09 attempt to replace it with a local Android emulator
(`reactivecircus/android-emulator-runner`) was reverted 2026-07-14 after it hung for 6 hours in
CI without ever booting, rather than failing fast — see `docs/QA_AUDIT.md` §3.7 for the full
history of both attempts. **Check the job's actual log in the Actions tab** for the real
pass/fail state; last confirmed-passing run on BrowserStack was 2026-07-07.

## Documentation and Testability Feedback

Found under:

- `manual-tests/testability_notes.md`
- `manual-tests/wiki/coverage_summary.md`

These emulate how feedback and progress would be captured in a live ADO Wiki environment.

## Project Scope and Objectives

This repository demonstrates comprehensive QA practices applied to the arxiv-papers-mobile application:

- Manual testing methodology for mobile applications across iOS and Android platforms
- Azure DevOps integration for test case management and requirement traceability
- SDLC-aware testing strategies with emphasis on collaboration and documentation
- Test automation collaboration framework supporting manual testing efforts

The testing framework is designed to ensure high-quality mobile application delivery through systematic validation of functional requirements, platform-specific behaviors, and user experience consistency.

## ✅ Real Mobile Test Execution

This repository includes **real manual test execution** on the actual arXiv Papers Mobile app:

### 📱 Live Testing Evidence
- **🤖 Android Testing:** Recorded on Android API 28 emulator (Pixel 3, Google Play image) using `adb screenrecord` + ffmpeg
- **🍎 iOS Testing:** Not executed — no macOS/Xcode/iOS Simulator was available. The "iOS" GIFs in `evidence/ios/` are the Android recording with a "Pending macOS environment" banner overlaid, kept as an honest placeholder rather than deleted. See [Platform coverage — how to frame it](#platform-coverage--how-to-frame-it) below.
- **🎥 Video Documentation:** Android GIFs are real screen recordings from the actual app (v1.0 APK)
- **📊 Traceability:** Complete evidence linking from requirements to results

### 🎯 Executed Test Cases

iOS was never executed on a real or virtual device (no macOS/Xcode/iOS Simulator available).
Where an "iOS GIF" link is shown below, it is a placeholder — the Android recording with a
"Pending macOS environment" banner overlaid — not real iOS evidence. Screenshot links marked
"generic" show real app UI but not the specific state their filename implies (see
[`evidence/README.md`](manual-tests/test-execution/evidence/README.md) for the full breakdown).

| Test Case | Description | Android | iOS | See Test Evidence |
|-----------|-------------|---------|-----|-------------------|
| TC001 | Search with valid keyword | ✅ Passed | ⏸ Not Executed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC001_SearchwithValidKeyword_Android_Pass.gif) · [📷 Screenshot](manual-tests/test-execution/evidence/screenshots/TC001_android_search_results.png) |
| TC002 | Empty query handling | ✅ Passed | ⏸ Not Executed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC002_SearchwithEmptyQuery_Android_Pass.gif) · [📷 Screenshot](manual-tests/test-execution/evidence/screenshots/TC002_android_empty_search.png) |
| TC003 | Download a paper and remove it | ✅ Passed | ⏸ Not Executed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC003_DownloadAndRemovePaper_Android_Pass.gif) · [📷 Before](manual-tests/test-execution/evidence/screenshots/TC003_before_download.png) · [📷 After](manual-tests/test-execution/evidence/screenshots/TC003_after_download.png) |
| TC004 | Search offline behavior | ✅ Passed | ⏸ Not Executed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC004_SearchOfflineBehavior_Android_Pass.gif) · 📷 Screenshot (generic, not the actual error state) |
| TC005 | PDF download and viewing | ✅ Passed | ⏸ Not Executed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC005_PDFDownloadandViewing_Android_Pass.gif) · [📷 Screenshot](manual-tests/test-execution/evidence/screenshots/TC005_pdf_viewer.png) |
| TC006 | iOS Safari PDF integration | N/A | ⏸ Not Executed | No real evidence — GIF/screenshot are a placeholder and a synthetic mockup, not a real iOS capture |
| TC007 | Android intent handling | ✅ Passed | N/A | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC007_AndroidIntentPDFHandling_Android_Pass.gif) · 📷 Screenshot (generic, not the actual intent chooser) |
| TC008 | Bulk downloaded papers management | ✅ Passed | ⏸ Not Executed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC008_BulkDownloadedPapersManagement_Android_Pass.gif) |
| TC009 | WiFi to cellular transition | ✅ Passed | ⏸ Not Executed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC009_WiFitoCellularTransition_Android_Pass.gif) · 📷 Screenshot (generic, not the actual network-transition state) |
| TC010 | Offline data persistence | ✅ Passed | ⏸ Not Executed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC010_OfflineDataPersistence_Android_Pass.gif) — no iOS evidence exists at all for this TC |
| TC011 | Accessibility TalkBack | ✅ Passed | N/A | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC011_AccessibilityTalkBackTesting_Android_Pass.gif) · 📷 Screenshot (generic, not TalkBack-specific) |

### 📁 Evidence Gallery

> Full recordings and screenshots organized by platform:

| Platform | Contents | See Test Evidence |
|----------|----------|-------------------|
| 🤖 Android | 10 genuine animated GIFs (TC001–TC005, TC007–TC011) | [Browse Android evidence](manual-tests/test-execution/evidence/android/) |
| 🍎 iOS | 8 **placeholder** GIFs (Android recording + "Pending macOS environment" banner) — not real iOS captures | [Browse iOS evidence](manual-tests/test-execution/evidence/ios/) |
| 📷 Screenshots | 11 captures — only 5 accurately show the state their filename claims; see [evidence/README.md](manual-tests/test-execution/evidence/README.md) | [Browse screenshots](manual-tests/test-execution/evidence/screenshots/) |
| 🎬 Suite summary | Animated overview of all 11 test cases | [See Test Evidence — suite summary](manual-tests/test-execution/evidence/suite_summary.gif) |

### 📋 Evidence Repository
- **Test Execution Guide:** [`manual-tests/test-execution/README.md`](manual-tests/test-execution/README.md)
- **Evidence with Links:** [`manual-tests/test-execution/traceability-with-evidence.md`](manual-tests/test-execution/traceability-with-evidence.md)
- **Execution Summary:** [`manual-tests/test-execution/execution-summary.md`](manual-tests/test-execution/execution-summary.md)
- **Detailed Logs:** [`manual-tests/test-execution/execution-logs/`](manual-tests/test-execution/execution-logs/)

### 🚀 Quick Start for Real Testing
```bash
# Run the setup script to prepare the app
./setup-app.sh

# Follow the execution guide
open manual-tests/test-execution/README.md
```

This demonstrates **genuine QA work** with verifiable evidence on a real React Native mobile application, showcasing enterprise-level manual testing processes with comprehensive documentation and traceability.

---

## CV / LinkedIn Reference

### CV bullets (ready to adapt)

- Designed 11 manual test cases for a React Native mobile app following ADO enterprise standards, and executed 10 of them on Android with verified evidence (the 11th, iOS Safari integration, is fully designed but not yet executed — no macOS/Xcode access): bi-directional traceability (User Stories → Test Cases → Evidence → Defects), structured execution logs, and defect reports with severity classification and remediation suggestions
- Configured an Android emulator testing environment from scratch (Android SDK CLI, KVM acceleration, API 28 Google Play image) and captured all test evidence with `adb screenrecord` — no Android Studio required
- Filed 7 defect reports (BUG001–BUG007) covering functional gaps, UX improvements, and a WCAG 2.1 AA accessibility violation (`accessibilityRole` missing on result cards, identified via TalkBack navigation)
- Built API test coverage at two layers: a Postman collection (8 requests, `pm.test()` assertions) covering TC001, TC002, Equivalence Partitioning (author field, pagination offset, cross-request `au:` vs `all:` comparison using `pm.sendRequest` + `pm.collectionVariables`), Boundary Value Analysis (max\_results, pagination edge), and Error Guessing (XSS injection); and 57 pytest tests for CI — API integration, mock-based SLA validation, article data contract tests (TC003, TC005–TC007), and retry-logic unit tests (100% coverage on utils.py)
- Authored a GitHub Actions CI pipeline running on every push — Python linting (Black, Ruff, mypy), pytest with `--cov-fail-under=100` quality gate, Codecov coverage reporting, Markdown/YAML validation, and Appium smoke tests on BrowserStack App Automate (Samsung Galaxy S22, Android 12); mirrored as Azure Pipelines config for ADO environments
- Implemented BDD scenarios in Gherkin using pytest-bdd: two feature files — `search.feature` (TC001, TC002, Scenario Outline across three academic domains) and `article_data_contract.feature` (TC003, TC008, validating API field completeness for article display and bulk uniqueness); shared Given step and `result` fixture extracted to `bdd/conftest.py` to eliminate duplication across modules
- Maintained full test traceability linking 4 user stories to 11 test cases, screen recordings, screenshots, and defect tickets in a single auditable repository

### LinkedIn one-liner

> Built an end-to-end QA portfolio on a real React Native app — 11 manual test cases, 57 automated tests (API, BDD/Gherkin, Appium POM on BrowserStack), Postman collection, 7 defect reports, ADO traceability, and a GitHub Actions CI pipeline with Codecov coverage gate.

### Platform coverage — how to frame it

**Android:** Fully executed. All 10 applicable test cases recorded on Android API 28 emulator with real `adb screenrecord` evidence, verified frame by frame.

**iOS:** Test cases fully designed and structured (TC001–TC006, TC008–TC009) and mirroring the Android suite. Execution and recording are pending access to a macOS environment or physical iOS device. The `evidence/ios/` folder contains placeholder GIFs (the Android recording with a "Pending macOS environment" banner) rather than empty entries — kept as a visible marker of what's missing, not deleted or passed off as real. The iOS-specific case (TC006: Safari PDF integration) is documented based on iOS platform behavior documentation but was never executed.

**In an interview:** *"The Android coverage is complete with verified recordings. The iOS test cases are fully designed — I need a Mac or physical device to record them, which is the next step."*

---

## Contact

**Author:** Jonathan Verdun  
**LinkedIn:** [linkedin.com/in/jonathan-verdun](https://linkedin.com/in/jonathan-verdun)  
**Location:** Paraguay (remote-friendly)

---
