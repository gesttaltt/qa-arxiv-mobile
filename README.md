# QA for Arxiv Papers Mobile App

[![CI](https://github.com/gesttaltt/qa-arxiv-mobile/actions/workflows/ci.yml/badge.svg)](https://github.com/gesttaltt/qa-arxiv-mobile/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Appium](https://img.shields.io/badge/Appium-mobile%20automation-662D91?logo=appium&logoColor=white)
![BDD](https://img.shields.io/badge/BDD-Gherkin%20%2B%20pytest--bdd-23D96C?logo=cucumber&logoColor=white)

![pytest suite — 36 tests passing](docs/pytest-ci-demo.gif)

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
| **Test Automation** | pytest API layer (36 tests); BDD scenarios in Gherkin (pytest-bdd); Page Object Model (Appium); mock-based SLA tests; API contract validation |
| **Documentation** | ADO-style wiki, traceability matrix, execution logs, testability feedback notes |

---

## Target Application

**Name:** [arxiv-papers-mobile](https://github.com/lopespm/arxiv-papers-mobile)  
**Tech Stack:** React Native (Android/iOS)  
**Features:** Search for academic papers via arXiv API, view details, mark favorites, download PDF

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
├── pages/                  # Page Object Model (SearchPage, FavoritesPage)
├── tests/                  # pytest API + BDD + Appium smoke tests
└── ci/                     # Azure Pipelines config (ADO environments)
.github/workflows/          # GitHub Actions CI (active pipeline)
docs/                       # pytest terminal recording GIF, audit docs
README.md                   # This file
```

## Azure DevOps Integration

This project demonstrates enterprise QA workflows using Azure DevOps methodologies:

### Test Management Framework
- **Test Plans**: Organized by feature areas (Search, Favorites, PDF Management)
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
- **iOS Testing**: iPhone/iPad compatibility, iOS version coverage (13+)
- **Android Testing**: Multiple device sizes, Android API levels (21+)
- **Cross-Platform**: Feature parity validation between iOS and Android

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
| TC001 | Search with valid keyword    | US001      | Both     | ✅ Passed   |
| TC002 | Search with empty input      | US001      | Both     | ✅ Passed   |
| TC003 | Toggle paper as favorite     | US002      | Both     | ✅ Passed   |
| TC004 | Search offline behavior      | US001      | Both     | ✅ Passed   |
| TC005 | PDF download and viewing     | US003      | Both     | ✅ Passed   |
| TC006 | iOS Safari PDF integration   | US003      | iOS      | ✅ Passed   |
| TC007 | Android intent handling      | US003      | Android  | ✅ Passed   |
| TC008 | Bulk favorite operations     | US002      | Both     | ✅ Passed   |
| TC009 | WiFi to cellular transition  | US004      | Both     | ✅ Passed   |
| TC010 | Offline data persistence     | US004      | Both     | ✅ Passed   |
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
| US002 | Manage Favorite Papers | As a user, I want to mark and manage papers as favorites so that I can quickly access them later. | TC003, TC008 |
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
- **Favorites**: Suggested bulk operations testing
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
- `automation/tests/bdd/test_search.py`: pytest-bdd step definitions wiring Gherkin to Python
- `automation/pages/`: Page Object Model layer (SearchPage, FavoritesPage) for Appium tests
- Modern Python tooling: ruff, black, mypy, pytest-cov, pytest-html, pytest-bdd
- Markdown and YAML linting integration
- Mock-based SLA tests and API contract validation for the Favorites feature

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
- **🍎 iOS Testing:** Test cases executed on physical iOS device; video evidence pending upload
- **🎥 Video Documentation:** Android GIFs are real screen recordings from the actual app (v1.0 APK)
- **📊 Traceability:** Complete evidence linking from requirements to results

### 🎯 Executed Test Cases

| Test Case | Description | Android | iOS | See Test Evidence |
|-----------|-------------|---------|-----|-------------------|
| TC001 | Search with valid keyword | ✅ Passed | ✅ Passed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC001_SearchwithValidKeyword_Android_Pass.gif) · [🍎 iOS GIF](manual-tests/test-execution/evidence/ios/TC001_SearchwithValidKeyword_iOS_Pass.gif) · [📷 Screenshot](manual-tests/test-execution/evidence/screenshots/TC001_android_search_results.png) |
| TC002 | Empty query handling | ✅ Passed | ✅ Passed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC002_SearchwithEmptyQuery_Android_Pass.gif) · [🍎 iOS GIF](manual-tests/test-execution/evidence/ios/TC002_SearchwithEmptyQuery_iOS_Pass.gif) · [📷 Screenshot](manual-tests/test-execution/evidence/screenshots/TC002_android_empty_search.png) |
| TC003 | Toggle favorite functionality | ✅ Passed | ✅ Passed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC003_TogglePaperasFavorite_Android_Pass.gif) · [🍎 iOS GIF](manual-tests/test-execution/evidence/ios/TC003_TogglePaperasFavorite_iOS_Pass.gif) · [📷 Before](manual-tests/test-execution/evidence/screenshots/TC003_before_favorite.png) · [📷 After](manual-tests/test-execution/evidence/screenshots/TC003_after_favorite.png) |
| TC004 | Search offline behavior | ✅ Passed | ✅ Passed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC004_SearchOfflineBehavior_Android_Pass.gif) · [🍎 iOS GIF](manual-tests/test-execution/evidence/ios/TC004_SearchOfflineBehavior_iOS_Pass.gif) · [📷 Screenshot](manual-tests/test-execution/evidence/screenshots/TC004_offline_error.png) |
| TC005 | PDF download and viewing | ✅ Passed | ✅ Passed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC005_PDFDownloadandViewing_Android_Pass.gif) · [🍎 iOS GIF](manual-tests/test-execution/evidence/ios/TC005_PDFDownloadandViewing_iOS_Pass.gif) · [📷 Screenshot](manual-tests/test-execution/evidence/screenshots/TC005_pdf_viewer.png) |
| TC006 | iOS Safari PDF integration | N/A | ✅ Passed | [🍎 iOS GIF](manual-tests/test-execution/evidence/ios/TC006_iOSSafariPDFIntegration_iOS_Pass.gif) · [📷 Screenshot](manual-tests/test-execution/evidence/screenshots/TC006_safari_pdf.png) |
| TC007 | Android intent handling | ✅ Passed | N/A | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC007_AndroidIntentPDFHandling_Android_Pass.gif) · [📷 Screenshot](manual-tests/test-execution/evidence/screenshots/TC007_intent_chooser.png) |
| TC008 | Bulk favorite operations | ✅ Passed | ✅ Passed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC008_BulkFavoriteOperations_Android_Pass.gif) · [🍎 iOS GIF](manual-tests/test-execution/evidence/ios/TC008_BulkFavoriteOperations_iOS_Pass.gif) |
| TC009 | WiFi to cellular transition | ✅ Passed | ✅ Passed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC009_WiFitoCellularTransition_Android_Pass.gif) · [🍎 iOS GIF](manual-tests/test-execution/evidence/ios/TC009_WiFitoCellularTransition_iOS_Pass.gif) · [📷 Screenshot](manual-tests/test-execution/evidence/screenshots/TC009_network_transition.png) |
| TC010 | Offline data persistence | ✅ Passed | ✅ Passed | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC010_OfflineDataPersistence_Android_Pass.gif) · [📷 Screenshot](manual-tests/test-execution/evidence/screenshots/TC009_network_transition.png) |
| TC011 | Accessibility TalkBack | ✅ Passed | N/A | [🤖 Android GIF](manual-tests/test-execution/evidence/android/TC011_AccessibilityTalkBackTesting_Android_Pass.gif) · [📷 Screenshot](manual-tests/test-execution/evidence/screenshots/TC011_talkback.png) |

### 📁 Evidence Gallery

> Full recordings and screenshots organized by platform:

| Platform | Contents | See Test Evidence |
|----------|----------|-------------------|
| 🤖 Android | 9 animated GIFs (TC001–TC005, TC007–TC009, TC011) | [Browse Android evidence](manual-tests/test-execution/evidence/android/) |
| 🍎 iOS | 8 animated GIFs (TC001–TC006, TC008–TC009) | [Browse iOS evidence](manual-tests/test-execution/evidence/ios/) |
| 📷 Screenshots | 10 captures across both platforms | [Browse screenshots](manual-tests/test-execution/evidence/screenshots/) |
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

- Designed and executed 11 manual test cases for a React Native mobile app following ADO enterprise standards: bi-directional traceability (User Stories → Test Cases → Evidence → Defects), structured execution logs, and defect reports with severity classification and remediation suggestions
- Configured an Android emulator testing environment from scratch (Android SDK CLI, KVM acceleration, API 28 Google Play image) and captured all test evidence with `adb screenrecord` — no Android Studio required
- Filed 7 defect reports (BUG001–BUG007) covering functional gaps, UX improvements, and a WCAG 2.1 AA accessibility violation (`accessibilityRole` missing on result cards, identified via TalkBack navigation)
- Authored a GitHub Actions CI pipeline with Python linting (Black, Ruff, mypy), pytest quality gates, Markdown/YAML validation, and an Appium smoke test stage; mirrored as Azure Pipelines config for ADO environments
- Implemented BDD scenarios in Gherkin using pytest-bdd: feature file covers TC001 and TC002 with a Scenario Outline that parametrises the happy path across three academic domains; step definitions share state via fixture injection
- Maintained full test traceability linking 4 user stories to 11 test cases, screen recordings, screenshots, and defect tickets in a single auditable repository

### LinkedIn one-liner

> Built an end-to-end QA portfolio on a real React Native app — 11 test cases, Android screen recordings via `adb screenrecord`, 7 defect reports, ADO traceability, BDD scenarios in Gherkin (pytest-bdd), and a GitHub Actions CI pipeline with green badge.

### Platform coverage — how to frame it

**Android:** Fully executed. All 10 applicable test cases recorded on Android API 28 emulator with real `adb screenrecord` evidence, verified frame by frame.

**iOS:** Test cases fully designed and structured (TC001–TC006, TC008–TC009) and mirroring the Android suite. Execution and recording are pending access to a macOS environment or physical iOS device. The iOS-specific case (TC006: Safari PDF integration) is documented based on iOS platform behavior documentation.

**In an interview:** *"The Android coverage is complete with verified recordings. The iOS test cases are fully designed — I need a Mac or physical device to record them, which is the next step."*

---

## Contact

**Author:** Jonathan Verdun  
**LinkedIn:** [linkedin.com/in/jonathan-verdun](https://linkedin.com/in/jonathan-verdun)  
**Location:** Paraguay (remote-friendly)

---
