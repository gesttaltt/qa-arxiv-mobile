# TC007 Execution Log - Android Intent Handling for PDF

**Test Case ID:** TC007
**Test Date:** 2026-05-21
**Tester:** QA Team
**Application:** arXiv Papers Mobile
**Version:** 1.2.0 (build 45)
**Environment:** Android 13 (emulator)

---

## Test Environment Details

### Android Execution:
- **Device/Emulator:** Pixel 6 Emulator, Android 13 (API 33)
- **App Version:** 1.2.0 (build 45)
- **Build:** Debug
- **Network:** WiFi
- **PDF Viewer Installed:** Google Drive PDF Viewer (Scenario A/B testing)

---

## Test Objective
Verify that on Android the app correctly fires an implicit intent to open a downloaded PDF, and that the intent chooser (or default handler) behaves correctly under the three decision-table scenarios.

---

## Test Steps Execution

### Step 1: Open paper detail view
**Action:** Search for "deep learning" and open the first result detail
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- Detail screen loaded correctly
- Download PDF button visible

### Step 2: Download PDF
**Action:** Tap Download PDF and wait for completion
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- Download completed successfully (progress: 0% -> 100%)
- Confirmation shown: "Download complete"
- File location: app-specific storage

### Step 3: Open PDF via intent
**Action:** Tap Open PDF
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- Scenario A/B tested: Intent chooser appeared with available PDF viewers
- Google Drive PDF Viewer, Chrome, and Samsung PDF Viewer listed
- Chrome set as default for subsequent tests

### Step 4: View PDF in selected app
**Action:** Select viewer from chooser
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- PDF opened correctly in Chrome
- All content rendered
- URL redirected correctly

### Step 5: Scroll through PDF
**Action:** Scroll through at least 2 pages
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- Scrolling smooth
- Pages 1-2 rendered without issues
- Equations and figures visible

### Step 6: Return to app
**Action:** Press Android back button
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- App returned to detail screen
- No state loss
- No crash or freeze

### Step 7: Test no PDF viewer (Scenario C)
**Action:** Uninstall all PDF viewers and repeat step 3
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- App showed message: "No PDF viewer found"
- No crash or ActivityNotFoundException
- User-friendly prompt to install a viewer
- Successful graceful degradation

---

## Expected Results Verification

| Criterion | Android | Notes |
|-----------|---------|-------|
| Scenario A: PDF opens in default viewer | [x] Pass [ ] Fail | Worked with Chrome as default |
| Scenario B: Intent chooser appears | [x] Pass [ ] Fail | Listed all available PDF apps |
| Scenario C: Graceful handling without viewer | [x] Pass [ ] Fail | User-friendly error, no crash |
| Back navigation returns to app cleanly | [x] Pass [ ] Fail | Same detail screen, stable |
| PDF renders correctly in external viewer | [x] Pass [ ] Fail | Content accurate |
| No crash during any scenario | [x] Pass [ ] Fail | Stable across all 3 scenarios |

---

## Evidence Collected

### Video Recordings:
- **Android:** [x] Completed - `TC007_AndroidIntentPDFHandling_Android_Pass.gif`

### Screenshots:
- **Intent Chooser:** [x] Captured -- `evidence/screenshots/TC007_intent_chooser.png`

### Evidence Location:
- **Android:** `evidence/android/TC007_AndroidIntentPDFHandling_Android_Pass.gif`

---

## Issues Found

### Issue 1:
**Platform:** Android
**Severity:** Info
**Description:** On Android 11+ (API 30+), apps must declare `<queries>` in AndroidManifest.xml to resolve intents. No issue observed on API 33, but older API 30+ devices may need manifest verification.
**Recommendation:** Verify AndroidManifest.xml includes `<queries>` for PDF viewer intent resolution.

---

## Overall Test Result

**Android Platform:** [x] PASS [ ] FAIL
**Overall Test Status:** [x] PASS [ ] FAIL

**Summary Notes:**
All three intent scenarios (A, B, C) pass correctly. PDF intents are properly fired, chooser/app opens the PDF, back navigation returns cleanly, and the missing-viewer case is handled gracefully without crash.

---

## Follow-up Actions

- [x] Upload video evidence to traceability documentation
- [x] Update traceability matrix with results
- [ ] Create defect reports for any issues found -- none critical
- [x] Document Android API level considerations for intent queries

---

**Execution Completed:** 2026-05-21 12:15
**Review Required:** No
**Next Steps:** Proceed to TC008 (bulk favorite operations)
