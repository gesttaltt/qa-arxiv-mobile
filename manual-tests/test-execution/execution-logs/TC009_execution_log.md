# TC009 Execution Log - WiFi to Cellular Network Transition

**Test Case ID:** TC009
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
- **Network:** WiFi + simulated cellular (emulator network settings)

### iOS Execution:
- **Device/Simulator:** iPhone 15 Simulator, iOS 17.2
- **App Version:** 1.2.0 (build 45)
- **Build:** Debug
- **Network:** WiFi + Network Link Conditioner (cellular simulation)

---

## Test Objective
Verify that the app continues to function without crashing or data loss when the device switches from WiFi to mobile data (and back) during active use.

---

## Test Steps Execution

### Step 1: Search with WiFi
**Action:** With WiFi active, search for "computer vision"
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Results loaded successfully: 12 (Android), 12 (iOS)
- Baseline established for comparison

### Step 2: Transition to cellular while results displayed
**Action:** Disable WiFi (leave cellular on)
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- App detected transition; no crash
- Brief connectivity indicator shown (~1s)
- Results remained visible throughout transition

### Step 3: Perform new search over cellular
**Action:** Search for "robotics"
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Results loaded over cellular
- Loading time: 3s (Android), 2.5s (iOS) -- slightly slower than WiFi (expected)
- No crash or timeout

### Step 4: Download PDF over cellular
**Action:** Open paper detail and tap Download PDF
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Download started over cellular
- Progress indicator shown
- No warning about "large download over cellular" -- potential UX consideration

### Step 5: Re-enable WiFi during/after download
**Action:** Re-enable WiFi while download is in progress
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Download completed without error
- No duplicate download started
- App switched to WiFi seamlessly after restore

### Step 6: Go fully offline
**Action:** Disable both WiFi and cellular data
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- App entered offline state
- Appropriate message on new search attempt
- Previously loaded results still accessible

### Step 7: Recover from offline
**Action:** Re-enable WiFi
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- App recovered without restart
- New search works
- Full functionality restored

---

## Expected Results Verification

| Criterion | Android | iOS | Notes |
|-----------|---------|-----|-------|
| No crash during WiFi->cellular transition | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Smooth transition |
| Search works over cellular | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Slightly slower, acceptable |
| Download works over cellular | [x] Pass [ ] Fail | [x] Pass [ ] Fail | No additional warnings |
| No duplicate download on WiFi restore | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Handled correctly |
| Offline state shown correctly | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Consistent with TC004 |
| Recovery works after re-enabling | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Full functionality restored |

---

## Evidence Collected

### Video Recordings:
- **Android:** [x] Completed - `TC009_WiFitoCellularTransition_Android_Pass.gif`
- **iOS:** [x] Completed - `TC009_WiFitoCellularTransition_iOS_Pass.gif`

### Screenshots:
- **Network Transition:** [x] Captured -- `evidence/screenshots/TC009_network_transition.png`

### Evidence Location:
- **Android:** `evidence/android/TC009_WiFitoCellularTransition_Android_Pass.gif`
- **iOS:** `evidence/ios/TC009_WiFitoCellularTransition_iOS_Pass.gif`

---

## Issues Found

### Issue 1:
**Platform:** Both
**Severity:** Low
**Description:** No "Downloading over cellular" warning is shown. Users on metered cellular connections may incur data charges without awareness.
**Recommendation:** Add a toggle in Settings: "Warn before downloading over cellular" similar to App Store behavior.

---

## Overall Test Result

**Android Platform:** [x] PASS [ ] FAIL
**iOS Platform:** [x] PASS [ ] FAIL
**Overall Test Status:** [x] PASS [ ] FAIL

**Summary Notes:**
Network transition handling is stable across both platforms. The app survives WiFi->cellular->offline->WiFi transitions without crashing or data loss. Searches and downloads work on cellular. Some UX improvements (cellular download warning) would benefit metered users.

---

## Follow-up Actions

- [x] Upload video evidence to traceability documentation
- [x] Update traceability matrix with results
- [ ] Create defect reports for any issues found -- none critical
- [x] Compare with TC004 offline behavior for consistency -- consistent
- [x] Document cellular data usage considerations for product team

---

**Execution Completed:** 2026-05-21 12:45
**Review Required:** No
**Next Steps:** Proceed to TC010 (offline data persistence)
