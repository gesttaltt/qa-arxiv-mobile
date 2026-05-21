# TC005 Execution Log - PDF Download and Viewing

**Test Case ID:** TC005
**Test Date:** 2026-05-21
**Tester:** QA Team
**Application:** arXiv Papers Mobile
**Version:** 1.2.0 (build 45)
**Environment:** Android 13 (emulator) / iOS 17.2 (simulator)

---

## Test Environment Details

### Android Execution:
- **Device/Emulator:** Pixel 6 Emulator, Android 13 (API 33)
- **App Version:** 1.2.0 (build 45)
- **Build:** Debug
- **Network:** WiFi
- **Storage Available:** >1 GB free

### iOS Execution:
- **Device/Simulator:** iPhone 15 Simulator, iOS 17.2
- **App Version:** 1.2.0 (build 45)
- **Build:** Debug
- **Network:** WiFi
- **Storage Available:** >2 GB free

---

## Test Objective
Verify that the app correctly downloads and opens a paper's PDF, and handles the case where no PDF is available without crashing or showing misleading UI.

---

## Test Steps Execution

### Step 1: Search for a paper
**Action:** Search for "quantum entanglement" and wait for results
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Results displayed: 12 (Android), 12 (iOS)
- First result has a PDF link visible

### Step 2: Open paper detail view
**Action:** Tap on first result
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Detail screen shows: title, authors, abstract
- Download PDF button clearly visible
- arXiv ID and publication date shown

### Step 3: Initiate PDF download
**Action:** Tap Download PDF / View PDF button
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Loading indicator appeared immediately
- Download progress shown: Yes (percentage indicator)
- Time to complete: 4s (Android), 3s (iOS) -- depends on arXiv server

### Step 4: Open and view PDF
**Action:** Wait for download to complete; PDF opens
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- PDF opened in in-app viewer (Android), default iOS PDF viewer (iOS)
- First page rendered correctly
- All text and equations visible

### Step 5: Scroll through PDF
**Action:** Scroll to page 2
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Page transition smooth
- No blank pages or rendering artifacts
- Text reflow not needed (PDF is fixed layout)

### Step 6: Navigate back to results
**Action:** Navigate back to results list
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Back navigation worked correctly
- Search results intact, no data loss
- No crash on return

### Step 7: Handle paper without PDF
**Action:** Find or navigate to an abstract-only paper
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Papers without PDF have Download button absent or disabled
- No misleading UI shown

### Step 8: Tap missing PDF button (if present)
**Action:** Tap disabled/absent Download PDF button
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Where button is disabled, no action occurs (correct)
- No crash or error when interacting with disabled state

---

## Expected Results Verification

| Criterion | Android | iOS | Notes |
|-----------|---------|-----|-------|
| PDF downloads successfully | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Download time: 4s / 3s |
| PDF renders correctly (pages 1-2) | [x] Pass [ ] Fail | [x] Pass [ ] Fail | No rendering issues |
| Back navigation works after PDF view | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Returned to same position in results |
| Abstract-only paper handled gracefully | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Button disabled/absent |
| No crash during download or viewing | [x] Pass [ ] Fail | [x] Pass [ ] Fail | No crashes observed |
| Download progress indicator shown | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Percentage shown |

---

## Evidence Collected

### Video Recordings:
- **Android:** [x] Completed - `TC005_PDFDownloadandViewing_Android_Pass.gif`
- **iOS:** [x] Completed - `TC005_PDFDownloadandViewing_iOS_Pass.gif`

### Screenshots:
- **PDF Viewer:** [x] Captured -- `evidence/screenshots/TC005_pdf_viewer.png`

### Evidence Location:
- **Android:** `evidence/android/TC005_PDFDownloadandViewing_Android_Pass.gif`
- **iOS:** `evidence/ios/TC005_PDFDownloadandViewing_iOS_Pass.gif`

---

## Issues Found

### Issue 1:
**Platform:** Android
**Severity:** Low
**Description:** PDF download progress indicator is shown as a percentage but does not include a cancel/dismiss button. If user taps download accidentally, there is no way to abort.
**Steps to Reproduce:** Tap Download PDF, observe no cancel option during progress.
**Expected vs Actual:** Expected cancel/X button vs progress bar only.

---

## Overall Test Result

**Android Platform:** [x] PASS [ ] FAIL
**iOS Platform:** [x] PASS [ ] FAIL
**Overall Test Status:** [x] PASS [ ] FAIL

**Summary Notes:**
PDF download and viewing works correctly on both platforms. The download completes reliably, rendering is accurate, and navigation back to results is smooth. Edge case handling for abstract-only papers is graceful. Minor UX suggestion around download cancellation noted.

---

## Follow-up Actions

- [x] Upload video evidence to traceability documentation
- [x] Update traceability matrix with results
- [ ] Create defect reports for any issues found -- none critical
- [x] Compare platform behaviors for consistency -- consistent
- [x] Document any platform-specific differences in PDF viewer behavior

---

**Execution Completed:** 2026-05-21 11:45
**Review Required:** No
**Next Steps:** Proceed to TC006 (iOS Safari PDF integration)
