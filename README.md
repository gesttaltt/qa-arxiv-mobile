# QA for Arxiv Papers Mobile App

> Fully documented testing emphasizing **manual QA** and **ADO-style traceability** over a real mobile application.

This repository contains a QA overlay for the open-source [arxiv-papers-mobile](https://github.com/lopespm/arxiv-papers-mobile) app.  
It demonstrates a full workflow of manual test case creation, traceability to user stories, automation alignment, and documentation —  
as expected in modern Azure DevOps–based QA environments.

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
├── test-cases/              # Comprehensive test case documentation
├── ado-integration/         # Azure DevOps workflow examples
├── testability-feedback/    # Requirement analysis and feedback
├── wiki/                   # ADO-style documentation
└── traceability-matrix.csv # Requirements-to-tests mapping
automation/
├── tests/                  # Automation collaboration examples
└── ci/                    # Pipeline integration
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
| TC004 | Search offline behavior      | US001      | Both     | 🔄 Testing  |
| TC005 | PDF download and viewing     | US003      | Both     | ⏳ Planned  |
| TC006 | iOS Safari PDF integration   | US003      | iOS      | ⏳ Planned  |
| TC007 | Android intent handling      | US003      | Android  | ⏳ Planned  |

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

- `azure-pipelines.yml`: Comprehensive Azure DevOps pipeline with linting and quality gates
- Modern Python dependencies with linting tools (ruff, black, mypy)
- Markdown and YAML linting integration
- Code coverage reporting and HTML test reports

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
- **🤖 Android Testing:** Executed on real devices/emulators with video evidence
- **🍎 iOS Testing:** Executed on iPhone/simulator with video evidence  
- **🎥 Video Documentation:** All test executions recorded and linked
- **📊 Traceability:** Complete evidence linking from requirements to results

### 🎯 Executed Test Cases
| Test Case | Description | Android | iOS | Evidence |
|-----------|-------------|---------|-----|----------|
| TC001 | Search with valid keyword | ✅ Verified | ✅ Verified | 🎥 [Video Evidence](manual-tests/test-execution/traceability-with-evidence.md) |
| TC002 | Empty query handling | ✅ Verified | ✅ Verified | 🎥 [Video Evidence](manual-tests/test-execution/traceability-with-evidence.md) |
| TC003 | Toggle favorite functionality | ✅ Verified | ✅ Verified | 🎥 [Video Evidence](manual-tests/test-execution/traceability-with-evidence.md) |

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

## Contact

**Author:** Jonathan Verdun  
**LinkedIn:** [linkedin.com/in/jonathan-verdun](https://linkedin.com/in/jonathan-verdun)  
**Location:** Paraguay (remote-friendly)


---