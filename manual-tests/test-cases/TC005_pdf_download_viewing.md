# TC005 – PDF download and viewing

**User Story:** US003 – Download and View PDFs  
**ISTQB Design Technique:** Equivalence Partitioning (paper with PDF / paper without PDF)  
**Priority:** High  
**Platform:** Both (Android / iOS)  
**Test Type:** Functional – Positive + Negative

---

**Objective:**  
Verify that the app correctly downloads and opens a paper's PDF, and handles the
case where no PDF is available without crashing or showing misleading UI.

**Preconditions:**  
- App is installed and running.  
- Device has internet connectivity.  
- Device has sufficient storage (≥ 50 MB free).  
- A search result is visible on screen.

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | Search for `quantum entanglement` and wait for results | At least one paper listed | |
| 2 | Tap on the first result to open its detail view | Detail screen shows title, authors, abstract, and a **Download PDF** or **View PDF** button | |
| 3 | Tap the **Download PDF** / **View PDF** button | A loading indicator appears; download begins | |
| 4 | Wait for the download to complete | PDF opens in the in-app viewer or the device's default PDF viewer | |
| 5 | Scroll through the PDF to page 2 | Pages render correctly; no blank pages or rendering errors | |
| 6 | Navigate back to the results list | App returns to the search results without crashing | |
| 7 | Find or navigate to a paper that has no PDF link (arXiv abstract-only) | The **Download PDF** button is either absent or visibly disabled | |
| 8 | If the button is present, tap it | App shows an informative message (e.g., *"PDF not available for this paper"*); no crash | |

---

**Expected Result:**  
- Steps 2–6: PDF is downloaded and rendered; back navigation works correctly.  
- Steps 7–8: App handles the no-PDF state gracefully without crashing or silently failing.

**Notes (EP partitions):**  
| Partition | Input | Expected behaviour |
|---|---|---|
| Valid PDF available | Standard arXiv paper with PDF | Downloads and opens successfully |
| No PDF available | Abstract-only or preprint without PDF | Disabled/hidden button or clear error message |
| Network drops mid-download | Kill WiFi after tapping download | Shows download-failed error; no partial/corrupt file left |
