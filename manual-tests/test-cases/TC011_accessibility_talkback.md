# TC011 – Accessibility: TalkBack screen reader (Android)

**User Story:** US001 / US002 / US003 (cross-feature accessibility baseline)  
**ISTQB Design Technique:** Platform-Specific Integration Testing  
**Standard:** WCAG 2.1 Level AA – Success Criteria 1.1.1, 1.3.1, 2.1.1, 4.1.2  
**Priority:** Low–Medium (differentiator for health-tech employers)  
**Platform:** Android only  
**Test Type:** Non-functional – Accessibility

---

**Objective:**  
Verify that the core user journeys (search, view result, toggle favourite) are fully
operable using the Android TalkBack screen reader without requiring sighted interaction.

**Preconditions:**  
- Physical Android device or emulator running Android 9+.  
- TalkBack is enabled: **Settings → Accessibility → TalkBack → On**.  
- App is installed and running.  
- Tester is familiar with basic TalkBack gestures (swipe right = next element,
  double-tap = activate, swipe up then right = back).

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | With TalkBack on, open the app | TalkBack announces the app name or first focusable element | |
| 2 | Swipe right to move focus to the search input field | TalkBack announces *"Search field"* or the field's accessibility label | |
| 3 | Double-tap to activate the field; type `robotics` via keyboard | Characters are announced as typed; field accepts input | |
| 4 | Move focus to the Search button; double-tap to submit | TalkBack announces the button label (e.g., *"Search button"*); search executes | |
| 5 | Swipe right through the result list | TalkBack announces each result's title and author(s) — not a generic *"image"* or *"button"* | |
| 6 | Double-tap the first result to open its detail view | Detail screen opens; TalkBack announces the title | |
| 7 | Locate the favourite/star button by swiping; double-tap | TalkBack announces a meaningful label (e.g., *"Add to favourites"* or *"Remove from favourites"*) — not *"unlabelled"* | |
| 8 | Navigate back to the results list using TalkBack back gesture | App returns to results; TalkBack announces the screen | |

---

**Expected Result:**  
- All interactive elements (search field, search button, result cards, favourite button,
  navigation tabs) have descriptive accessibility labels — no element is announced as
  *"unlabelled"* or *"image"*.  
- Focus order follows a logical reading sequence (top-to-bottom, left-to-right).  
- No feature requires simultaneous multi-finger gestures not supported by TalkBack.

---

**WCAG Criteria Checked:**

| Criterion | Description | Pass/Fail |
|---|---|---|
| 1.1.1 Non-text content | All icons/images have text alternatives | |
| 1.3.1 Info and relationships | List structure is conveyed to screen reader | |
| 2.1.1 Keyboard (touch equivalent) | All functionality reachable via TalkBack gestures alone | |
| 4.1.2 Name, Role, Value | All UI components have name + role announced | |

---

**Notes:**  
- If an element is announced as *"unlabelled"*, the React Native component is missing an
  `accessibilityLabel` or `accessibilityRole` prop. Log each occurrence as a separate
  low-severity defect referencing the screen and element position.  
- For iOS VoiceOver coverage, a companion TC (TC012) should be created targeting
  VoiceOver with equivalent steps.
