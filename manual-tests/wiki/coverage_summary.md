# QA Coverage Summary

This document reflects current QA coverage for the arxiv-papers-mobile app.

## 📌 Stats

- Total User Stories: **3**
- Manual Test Cases: **3**
- Automated Test Cases: **2**
- Traceability Matrix: ✅ Present (`traceability-matrix.csv`)
- CI Pipeline: ✅ Functional (`azure-pipelines.yml`)
- Test Results: ✅ Published in `.trx` format (`results.trx`)

## ✅ Coverage Map

| User Story       | Manual Test Case | Automated | Notes                       |
|------------------|------------------|-----------|-----------------------------|
| US001 – Search valid | TC001             | ✅ Yes     | Passed                      |
| US002 – Empty query  | TC002             | ✅ Yes     | Validation failed (bug)     |
| US003 – Toggle fav   | TC003             | ❌ No      | Needs automation support    |

## 🔍 Observations

- Manual QA coverage covers the core functional flows (search, input validation, state change)
- Automated testing covers the most critical regression cases
- CI pipeline produces `.trx` results compatible with Azure Test Plans

---

This documentation simulates an ADO Wiki QA Summary page that would be updated during each sprint or test cycle.
