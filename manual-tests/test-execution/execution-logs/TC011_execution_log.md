# TC011 Execution Log - Accessibility: TalkBack Screen Reader (Android)

**Test Case ID:** TC011
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
- **TalkBack Version:** Android Accessibility Suite 13.0
- **Network:** WiFi

---

## Test Objective
Verify that the core user journeys (search, view result, toggle favourite) are fully operable using the Android TalkBack screen reader without requiring sighted interaction.

---

## Test Steps Execution

### Step 1: App launches with TalkBack
**Action:** Open the app with TalkBack enabled
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- TalkBack announced app name on launch
- First focusable element highlighted
- No delay in TalkBack initialization

### Step 2: Navigate to search field
**Action:** Swipe right to move focus to search input field
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- TalkBack announced: "Search arXiv papers, text field"
- Focus movement logical (top-to-bottom)
- No "unlabelled" announcements

### Step 3: Type search query via keyboard
**Action:** Double-tap to activate field; type "robotics"
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- Characters announced as typed
- Field accepted input correctly
- Keyboard accessible via TalkBack

### Step 4: Submit search
**Action:** Move focus to Search button; double-tap to submit
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- TalkBack announced: "Search button"
- Search executed successfully
- Results loaded and announced

### Step 5: Navigate through results
**Action:** Swipe right through result list
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- Each result's title and authors announced
- No generic "image" or "button" announcements
- Focus order follows visual layout correctly

### Step 6: Open result detail
**Action:** Double-tap first result to open detail view
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- Detail screen opened
- TalkBack announced the paper title
- All metadata accessible

### Step 7: Toggle favorite via TalkBack
**Action:** Locate and tap favorite/star button
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- TalkBack announced: "Add to favourites, double-tap to activate"
- After activation: "Remove from favourites"
- Meaningful label changes -- no "unlabelled"

### Step 8: Navigate back
**Action:** Use TalkBack back gesture
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A [ ] Fail
**Notes:**
- App returned to results list
- TalkBack announced the results screen
- Navigation smooth with TalkBack gestures

---

## Expected Results Verification

| Criterion | Android | Notes |
|-----------|---------|-------|
| Search field has descriptive label | [x] Pass [ ] Fail | "Search arXiv papers, text field" |
| Search button announced correctly | [x] Pass [ ] Fail | "Search button" |
| Result titles announced (not "image") | [x] Pass [ ] Fail | Titles + authors read clearly |
| Favorite button has label | [x] Pass [ ] Fail | "Add to/Remove from favourites" |
| Focus follows logical order | [x] Pass [ ] Fail | Top-to-bottom, left-to-right |
| No "unlabelled" elements encountered | [x] Pass [ ] Fail | All elements properly labeled |
| WCAG 1.1.1 Non-text content | [x] Pass [ ] Fail | Icons have text alternatives |
| WCAG 1.3.1 Info and relationships | [x] Pass [ ] Fail | List structure conveyed |
| WCAG 2.1.1 Keyboard (touch equivalent) | [x] Pass [ ] Fail | All features reachable via gestures |
| WCAG 4.1.2 Name, Role, Value | [x] Pass [ ] Fail | All components have name + role |

---

## Evidence Collected

### Video Recordings:
- **Android:** [x] Completed - `TC011_AccessibilityTalkBackTesting_Android_Pass.gif`

### Screenshots:
- **TalkBack in use:** [x] Captured -- `evidence/screenshots/TC011_talkback.png`

### Evidence Location:
- **Android:** `evidence/android/TC011_AccessibilityTalkBackTesting_Android_Pass.gif`

---

## Issues Found

### Issue 1:
**Platform:** Android
**Severity:** Low
**Description:** Search results do not have a "heading" role -- TalkBack treats each result as a generic list item. WCAG 1.3.1 would be better satisfied with result cards announced as "heading level 3" or similar.
**Recommendation:** Add `accessibilityRole="header"` (or appropriate level) to result card titles in React Native components.

---

## Overall Test Result

**Android Platform:** [x] PASS [ ] FAIL
**Overall Test Status:** [x] PASS [ ] FAIL

**Summary Notes:**
The app demonstrates good accessibility baseline for TalkBack. All core user journeys are navigable with the screen reader, all interactive elements have descriptive labels, and no "unlabelled" elements were encountered. Minor improvement suggestion for result card heading roles. Meets WCAG 2.1 Level AA success criteria checked.

---

## Follow-up Actions

- [x] Upload video evidence to traceability documentation
- [x] Update traceability matrix with results
- [ ] Create low-severity defect for heading role enhancement
- [x] Document accessibility findings for product team
- [ ] Recommend creating TC012 for iOS VoiceOver coverage (companion test case)

---

**Execution Completed:** 2026-05-21 13:15
**Review Required:** No
**Next Steps:** TC010 dedicated evidence recording (pending) / iOS VoiceOver coverage (future TC012)
