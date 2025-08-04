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
manual-tests/         # All manual test cases and traceability matrix
automation/           # Basic automation scripts + CI mock
README.md             # This file
```

## Manual Test Cases

Located in `manual-tests/test-cases/`

| ID    | Title                        | Status      |
|-------|------------------------------|-------------|
| TC001 | Search with valid keyword    | ✅ Done     |
| TC002 | Search with empty input      | ✅ Done     |
| TC003 | Toggle paper as favorite     | ✅ Done     |
| TC004 | Attempt search while offline | ⏳ Planned  |
| TC005 | Download and open PDF        | ⏳ Planned  |

📝 Each test case includes objective, steps, expected results, edge case considerations, and pass/fail field.

🔗 **Traceability Matrix:** Located at `manual-tests/traceability-matrix.csv`

This document links:

- User Stories (US001, US002, …)
- Manual Test Cases (TC001, …)
- Automation Test Scripts (if any)

## Automation Layer

Located in `automation/tests/`

A few selected user flows are scripted using pytest, simulating how automation might extend QA coverage in collaboration with manual testers.

Also includes:

- `qa-pipeline.yml`: Example of CI integration via GitHub Actions or Azure DevOps pipeline.

## Documentation and Testability Feedback

Found under:

- `manual-tests/testability_notes.md`
- `manual-tests/wiki/coverage_summary.md`

These emulate how feedback and progress would be captured in a live ADO Wiki environment.

## For Recruiters / Hiring Teams

This repo was created to demonstrate:

- Hands-on manual QA on a mobile app
- SDLC-aware testing strategies
- Test case coverage and traceability
- CI/automation collaboration awareness

All tests were written and organized independently for evaluation purposes, not sponsored or affiliated with the app authors.

## Contact

**Author:** Jonathan Verdun  
**LinkedIn:** [linkedin.com/in/jonathan-verdun](https://linkedin.com/in/jonathan-verdun)  
**Location:** Paraguay (remote-friendly)


---