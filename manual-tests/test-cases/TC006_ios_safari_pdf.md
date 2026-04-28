# TC006 – iOS Safari PDF integration

**User Story:** US003 – Download and View PDFs  
**ISTQB Design Technique:** Platform-Specific Integration Testing  
**Priority:** Medium  
**Platform:** iOS only  
**Test Type:** Integration

---

**Objective:**  
Verify that on iOS, tapping "Open in Safari" (or equivalent) for a paper's PDF
correctly hands off to Safari and opens the document, without leaving the app in
a broken state on return.

**Preconditions:**  
- Test device or simulator: iPhone running iOS 15 or later.  
- Safari is installed (default, cannot be removed).  
- App is installed and running.  
- Internet connectivity is active.

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | Search for `neural networks` and open the first result's detail view | Detail screen is shown | |
| 2 | Locate the **Open in Safari** button (or long-press a PDF link) | Button/option is visible | |
| 3 | Tap **Open in Safari** | iOS prompts *"Open in Safari?"* or navigates directly | |
| 4 | Confirm / allow the handoff | Safari opens with the arXiv PDF URL | |
| 5 | Verify the PDF renders in Safari | First page of the paper is visible; no blank page | |
| 6 | Use the iOS gesture (swipe from left edge or tap **< Back**) to return to the app | App resumes on the same detail screen without reloading from scratch | |
| 7 | Navigate back to the search results | Results list is intact; no data loss | |

---

**Expected Result:**  
- Safari opens the correct PDF URL.  
- The app resumes normally after the user returns; no crash on background/foreground transition.

**Notes:**  
- On older iOS (< 13) the PDF may open inline in a `WKWebView` rather than launching Safari.
  Document which behaviour the app uses on the tested iOS version.  
- If the arXiv link requires a redirect (`arxiv.org/pdf/xxxx`), verify Safari follows it
  without an SSL or certificate error.
