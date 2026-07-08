# TC002 Execution Log - Search with Empty Input

**Test Case ID:** TC002
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

### iOS Execution:
**Not executed.** No macOS/Xcode/iOS Simulator was available for this project. The "iOS"
GIF referenced below is the Android recording with a "Pending macOS environment" banner
overlaid — a placeholder, not a real iOS capture.

---

## Test Objective
Verify that the application properly handles empty search queries with appropriate user feedback and error handling.

---

## Test Steps Execution

### Step 1: Launch the app
**Action:** Tap app icon to launch
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Notes:**
- App launches to main screen: Yes
- Search interface visible: Yes

### Step 2: Navigate to search field
**Action:** Tap on search input field
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Notes:**
- Field becomes active: Yes
- Cursor appears: Yes
- Keyboard displays: Yes

### Step 3: Leave search field empty
**Action:** Ensure search field contains no text
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Notes:**
- Field is completely empty: Yes
- Placeholder text visible: Yes ("Search arXiv papers...")
- Keyboard's Search key state: Enabled (app does not intercept it when the field is empty)

### Step 4: Attempt to search
**Action:** Tap the keyboard's Search key with an empty field (there is no separate in-app Search button)
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Notes:**
- Key responds to tap: Yes
- Any loading indicators: No (immediate validation)
- Immediate feedback given: Yes

### Step 5: Observe application response
**Action:** Check for error messages, validation, or default behavior
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Notes:**
- Error message displayed: Yes
- Message content: "Please enter a search term"
- Message disappears after: 3 seconds (auto-dismiss)
- App remains stable: Yes

---

## Expected Results Verification

| Criterion | Android | iOS | Notes |
|-----------|---------|-----|-------|
| Search prevented or validation shown | [x] Pass [ ] Fail | N/A | Method: Inline validation message |
| Clear error/validation message | [x] Pass [ ] Fail | N/A | Message: "Please enter a search term" |
| No app crash or freeze | [x] Pass [ ] Fail | N/A | Stability confirmed |
| User can retry with valid input | [x] Pass [ ] Fail | N/A | Recovery possible |
| Consistent behavior between platforms | N/A | N/A | iOS not executed — nothing to compare |

---

## Detailed Behavior Analysis

### Validation Method Observed (Android):
- [ ] Submission blocked when field empty
- [x] Error message on search attempt
- [x] Toast/snackbar notification
- [ ] Inline field validation
- [ ] Modal dialog warning
- [ ] No validation (search proceeds)

### Error Message Analysis:
**Android Message:** "Please enter a search term"
**Message Type:** Toast (Android)
**Duration:** 3 seconds
**Dismissible:** Auto

### User Experience Notes:
- **Clarity:** Message is clear and tells user what to do
- **Guidance:** Tells user to enter a search term
- **Accessibility:** Message is visible but screen reader compatibility not verified
- **Design:** Fits the app's design language

---

## Evidence Collected

### Video Recordings:
- **Android:** [x] Completed - `TC002_SearchwithEmptyQuery_Android_Pass.gif`
- **iOS:** [ ] Not executed - `TC002_SearchwithEmptyQuery_iOS_Pass.gif` is a placeholder (Android recording, "Pending macOS environment" banner)

### Screenshots:
- **Android Empty Field State:** [x] Captured
- **Android Error/Validation State:** [x] Captured -- `evidence/screenshots/TC002_android_empty_search.png`

### Evidence Location:
- **Android:** `evidence/android/TC002_SearchwithEmptyQuery_Android_Pass.gif`
- **iOS (placeholder only):** `evidence/ios/TC002_SearchwithEmptyQuery_iOS_Pass.gif`

---

## Issues Found

### Issue 1:
**Platform:** Android
**Severity:** Low
**Description:** The app does not intercept an empty submission before it reaches the validation layer — since there is no in-app Search button to disable, the only mitigation would be to no-op silently on the keyboard's Search key when the field is empty, rather than showing a toast/alert every time.
**Steps to Reproduce:**
1. Launch app
2. Tap the keyboard's Search key without typing anything
3. Validation message appears
**Expected vs Actual:** Submission could be silently ignored when empty vs currently showing a validation message every time

### Issue 2:
**Platform:** Android
**Severity:** Low
**Description:** No server-side validation documented. The arXiv API returns 400 for empty queries, which the app gracefully handles, but the API test layer also validates this behavior.
**Impact:** Low -- app handles it correctly.

---

## Additional Test Variations

### Variation 1: Whitespace Only
**Test:** Enter only spaces in search field
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Behavior:** Treated as empty -- validation message shown

### Variation 2: Clear Field After Typing
**Test:** Type text, then clear field, then search
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Behavior:** Treated as empty -- validation message shown

---

## Overall Test Result

**Android Platform:** [x] PASS [ ] FAIL
**iOS Platform:** Not Executed — no iOS device/simulator available
**Overall Test Status:** [x] PASS (Android only) [ ] FAIL

**Platform Consistency:** N/A — iOS not executed, nothing to compare against

**Summary Notes:**
Empty query handling works correctly on Android. Validation message is clear and helpful. The app remains stable and no crashes occur. Showing a validation message on every empty submission (rather than silently ignoring it) is a minor UX concern but does not affect functionality. API-layer validation also confirms the backend handles empty queries correctly. iOS was not executed — see Evidence Collected for the placeholder status of the "iOS" GIF.

---

## Follow-up Actions

- [x] Upload video evidence to traceability documentation
- [x] Update traceability matrix with results
- [x] Document iOS as not executed (hardware unavailable)
- [x] Create recommendations for improved error handling
- [ ] Test additional edge cases if needed

---

**Execution Completed:** 2026-05-21 11:15
**Review Required:** No
**Recommendations:** Consider silently ignoring the keyboard's Search key when the field is empty, instead of showing a validation message every time, as a proactive UX improvement.
