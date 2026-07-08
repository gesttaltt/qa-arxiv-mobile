# TC002 Execution Log - Search with Empty Input

**Test Case ID:** TC002
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

### iOS Execution:
- **Device/Simulator:** iPhone 15 Simulator, iOS 17.2
- **App Version:** 1.2.0 (build 45)
- **Build:** Debug
- **Network:** WiFi

---

## Test Objective
Verify that the application properly handles empty search queries with appropriate user feedback and error handling.

---

## Test Steps Execution

### Step 1: Launch the app
**Action:** Tap app icon to launch
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- App launches to main screen: Yes
- Search interface visible: Yes

### Step 2: Navigate to search field
**Action:** Tap on search input field
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Field becomes active: Yes
- Cursor appears: Yes
- Keyboard displays: Yes

### Step 3: Leave search field empty
**Action:** Ensure search field contains no text
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Field is completely empty: Yes
- Placeholder text visible: Yes ("Search arXiv papers...")
- Keyboard's Search key state: Enabled (app does not intercept it when the field is empty)

### Step 4: Attempt to search
**Action:** Tap the keyboard's Search key with an empty field (there is no separate in-app Search button)
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Key responds to tap: Yes
- Any loading indicators: No (immediate validation)
- Immediate feedback given: Yes

### Step 5: Observe application response
**Action:** Check for error messages, validation, or default behavior
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Error message displayed: Yes
- Message content: "Please enter a search term"
- Message disappears after: 3 seconds (auto-dismiss)
- App remains stable: Yes

---

## Expected Results Verification

| Criterion | Android | iOS | Notes |
|-----------|---------|-----|-------|
| Search prevented or validation shown | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Method: Inline validation message |
| Clear error/validation message | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Message: "Please enter a search term" |
| No app crash or freeze | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Stability confirmed |
| User can retry with valid input | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Recovery possible |
| Consistent behavior between platforms | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Platform differences: None |

---

## Detailed Behavior Analysis

### Validation Method Observed:
- [ ] Submission blocked when field empty
- [x] Error message on search attempt
- [x] Toast/snackbar notification
- [ ] Inline field validation
- [ ] Modal dialog warning
- [ ] No validation (search proceeds)

### Error Message Analysis:
**Android Message:** "Please enter a search term"
**iOS Message:** "Please enter a search term"
**Message Type:** Toast (Android) / Inline alert (iOS)
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
- **iOS:** [x] Completed - `TC002_SearchwithEmptyQuery_iOS_Pass.gif`

### Screenshots:
- **Android Empty Field State:** [x] Captured
- **Android Error/Validation State:** [x] Captured -- `evidence/screenshots/TC002_android_empty_search.png`
- **iOS Empty Field State:** [ ] Captured (covered in GIF)
- **iOS Error/Validation State:** [ ] Captured (covered in GIF)

### Evidence Location:
- **Android:** `evidence/android/TC002_SearchwithEmptyQuery_Android_Pass.gif`
- **iOS:** `evidence/ios/TC002_SearchwithEmptyQuery_iOS_Pass.gif`

---

## Issues Found

### Issue 1:
**Platform:** Both
**Severity:** Low
**Description:** The app does not intercept an empty submission before it reaches the validation layer — since there is no in-app Search button to disable, the only mitigation would be to no-op silently on the keyboard's Search key when the field is empty, rather than showing a toast/alert every time.
**Steps to Reproduce:**
1. Launch app
2. Tap the keyboard's Search key without typing anything
3. Validation message appears
**Expected vs Actual:** Submission could be silently ignored when empty vs currently showing a validation message every time

### Issue 2:
**Platform:** Both
**Severity:** Low
**Description:** No server-side validation documented. The arXiv API returns 400 for empty queries, which the app gracefully handles, but the API test layer also validates this behavior.
**Impact:** Low -- app handles it correctly on both sides.

---

## Additional Test Variations

### Variation 1: Whitespace Only
**Test:** Enter only spaces in search field
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Behavior:** Treated as empty -- validation message shown

### Variation 2: Clear Field After Typing
**Test:** Type text, then clear field, then search
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Behavior:** Treated as empty -- validation message shown

---

## Overall Test Result

**Android Platform:** [x] PASS [ ] FAIL
**iOS Platform:** [x] PASS [ ] FAIL
**Overall Test Status:** [x] PASS [ ] FAIL

**Platform Consistency:** [x] Consistent [ ] Different behaviors noted

**Summary Notes:**
Empty query handling is consistent across both platforms. Validation message is clear and helpful. The app remains stable and no crashes occur. Showing a validation message on every empty submission (rather than silently ignoring it) is a minor UX concern but does not affect functionality. API-layer validation also confirms the backend handles empty queries correctly.

---

## Follow-up Actions

- [x] Upload video evidence to traceability documentation
- [x] Update traceability matrix with results
- [x] Document platform differences if any -- none found
- [x] Create recommendations for improved error handling
- [ ] Test additional edge cases if needed

---

**Execution Completed:** 2026-05-21 11:15
**Review Required:** No
**Recommendations:** Consider silently ignoring the keyboard's Search key when the field is empty, instead of showing a validation message every time, as a proactive UX improvement.
