# TC012 – Cancel an in-progress PDF download

**User Story:** US003 – Download and View PDFs
**ISTQB Design Technique:** Error Guessing
**Priority:** Medium
**Platform:** Both (Android / iOS)
**Test Type:** Functional – Negative
**Status:** Designed — Not Executed (added 2026-08-07)

---

**Objective:**
Verify that the user can cancel a PDF download while it is in progress, and that
cancelling leaves no partial/corrupt file behind and returns the UI to its initial
"Download PDF" state.

**Preconditions:**
- App is installed and running.
- iOS testing: iPhone simulator or device running iOS 15 or later (Xcode 15+ if using Simulator).
- Internet connectivity is active (WiFi or cellular).
- A search result with an available PDF is open in its detail view.

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | Search for `quantum entanglement` and open the first result's detail view | Detail screen shows a **Download PDF** button | |
| 2 | Tap **Download PDF** | A progress indicator appears | |
| 3 | While the download is in progress, look for a cancel/stop control (× icon, "Cancel" text, or similar) and tap it | Download stops immediately; the button resets to its initial "Download PDF" state | |
| 4 | If no such control is visible, attempt to abort by navigating back to the previous screen | Underlying download request is also aborted, not left running invisibly | |
| 5 | Navigate to the DOWNLOADED tab | No partial or corrupt entry for this paper appears | |
| 6 | Re-attempt the download from a clean state | Download completes normally, with no leftover state from the cancelled attempt | |

---

**Expected Result:**
- Step 3: A visible, working cancel control stops the download and leaves no partial file.
- Step 4: If no cancel control exists, this step is expected to **fail** — see Notes.
- Step 6: A fresh download attempt succeeds with no interference from the prior cancellation.

**Notes:**
- This test case formalizes a gap already reported as **BUG003** (`manual-tests/defects/BUG003_no_download_cancel_button.md`,
  found 2026-05-21 via ad hoc exploration during TC005 execution): no cancel/dismiss control
  exists on the progress indicator, and the system back button does not visibly abort the
  underlying request. Expected initial result on a real run: **Fail on step 3** until BUG003 is
  fixed — this TC is kept to make that gap formally re-testable, not because the control is
  assumed to exist.
- Relates to TC005 (PDF download and viewing), TC009 (download over cellular — verify the cancel
  path once implemented works across network types, per BUG003's regression-risk note).

---

**Automation Coverage:**

None feasible without the cancel control existing in the UI (Appium can only interact with
elements that are actually rendered).
