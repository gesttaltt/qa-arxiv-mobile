# TC007 – Android intent handling for PDF

**User Story:** US003 – Download and View PDFs  
**ISTQB Design Technique:** Platform-Specific Integration Testing + Decision Table  
**Priority:** Medium  
**Platform:** Android only  
**Test Type:** Integration

---

**Objective:**  
Verify that on Android the app correctly fires an implicit intent to open a
downloaded PDF, and that the intent chooser (or default handler) behaves correctly
under the three decision-table scenarios below.

**Preconditions:**  
- Test device or emulator: Android API 21 or later.  
- App is installed; internet connectivity is active.  
- At least one PDF viewer is installed (e.g., Google Drive PDF Viewer, Adobe Acrobat).

---

**Decision Table — Intent Scenarios:**

| # | PDF viewer installed | User sets a default | Expected outcome |
|---|---|---|---|
| A | Yes | Yes | PDF opens directly in default viewer |
| B | Yes | No | Android intent chooser appears; user selects a viewer; PDF opens |
| C | No | N/A | App shows *"No PDF viewer found"* or prompts to install one |

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | Search for `deep learning` and open the first result detail view | Detail screen loads | |
| 2 | Tap **Download PDF** and wait for download to complete | Download completes (progress bar reaches 100 % or confirmation shown) | |
| 3 | Tap **Open PDF** (or equivalent) | Scenario A or B: intent chooser appears or default viewer opens directly | |
| 4 | (Scenario B) Select a viewer from the chooser | PDF renders in the selected viewer | |
| 5 | Scroll through at least 2 pages | Pages render without blank content | |
| 6 | Press the Android back button | App returns to the correct detail screen | |
| 7 | Uninstall all PDF viewers and repeat step 3 | Scenario C: app handles missing viewer gracefully — no crash | |

---

**Expected Result:**  
- Scenarios A and B: PDF opens in a viewer; back navigation returns to the app cleanly.  
- Scenario C: App shows a user-friendly error; does not crash with an unhandled `ActivityNotFoundException`.

**Notes:**  
- On Android 11+ (API 30+), apps must declare `<queries>` in `AndroidManifest.xml` to resolve
  intents. If Scenario C triggers unexpectedly on API 30+, this is likely the root cause —
  log it as a defect referencing the manifest.
