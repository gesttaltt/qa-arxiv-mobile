# TC013 – PDF download with device storage full

**User Story:** US003 – Download and View PDFs
**ISTQB Design Technique:** Error Guessing
**Priority:** Medium
**Platform:** Both (Android / iOS)
**Test Type:** Functional – Negative
**Status:** Designed — Not Executed (added 2026-08-07)

---

**Objective:**
Verify that attempting to download a PDF while device storage is at or near capacity
produces a clear, user-facing error rather than a crash, an infinite spinner, or a
silently-discarded tap.

**Preconditions:**
- App is installed and running.
- iOS testing: iPhone simulator or device running iOS 15 or later (Xcode 15+ if using Simulator).
- Device storage filled to leave **< 50 MB free** (Android: a dummy-file app or
  `adb shell fallocate`; iOS: the Files app large-file trick or a filler app from the App Store —
  document the exact method used in the execution log, methods differ per platform).
- A search result with an available PDF is open in its detail view.

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | Fill device storage to < 50 MB free; record the exact free space in the execution log | Storage is confirmed near-full via device Settings | |
| 2 | Search for `quantum entanglement` and open the first result's detail view | Detail screen shows a **Download PDF** button | |
| 3 | Tap **Download PDF** | Attempt begins | |
| 4 | Observe app behavior during and after the failed write | A clear message is shown (e.g., "Not enough storage space"); no crash, no indefinite spinner, no silent no-op | |
| 5 | Open the DOWNLOADED tab | No corrupt or partial entry for this paper appears | |
| 6 | Free up storage space (remove the dummy file) | Storage is confirmed available again | |
| 7 | Retry the same download | Download completes normally | |

---

**Expected Result:**
- Step 4: The app surfaces a specific, actionable error rather than failing silently.
- Step 5: No partial file or broken list entry results from the failed write.
- Step 7: Once storage is freed, the download succeeds without needing an app restart.

**Notes:**
- Not yet observed on a real device or simulator. Low-storage simulation differs significantly
  between Android and iOS — the execution log must record which method was used, since a
  filesystem-level fill (`fallocate`) and an app-level fill (large media file) can surface
  different failure modes.
- Relates to TC005 (PDF download and viewing), TC003 (download and remove), TC012 (cancel
  in-progress download — a storage-full failure is a different trigger for the same "download
  did not complete cleanly" state).

---

**Automation Coverage:**

None — requires real device storage manipulation, not reproducible via the API layer or mocks.
