# TC002 – Search with empty query

**Objective:**  
Verify that the app handles empty search submissions gracefully.

**Preconditions:**  
- App is open on Android **or** iOS.  
- iOS testing: iPhone simulator or device running iOS 15 or later (Xcode 15+ if using Simulator).  
- No text has been entered in the search field.

**Test Steps:**  
1. Tap the search field, leave it empty, and tap the keyboard's Search key.  

**Expected Result:**  
- The app displays a warning or validation message:  
  *“Please enter a search term.”*  
- No API request is made.  
- No crash occurs.

| Step | Expected Outcome                    | Pass/Fail |
|------|------------------------------------|-----------|
| 1    | Validation prevents empty search   |           |
| 2    | No crash or blank screen appears   |           |

---

**Accessibility Validation (WCAG 2.1 AA):**

| # | Check | Expected Outcome | Pass/Fail |
|---|---|---|---|
| A1 | Enable TalkBack/VoiceOver and repeat the empty-search submission | The validation message is announced automatically without extra navigation (live-region / assertive announcement) — WCAG 2.1 SC 4.1.3 |  |

---

**Platform Notes:**

| Platform | Specific behaviour to verify |
|---|---|
| Android | Toast or inline error message is announced by TalkBack if enabled |
| iOS | Validation message is readable via VoiceOver; keyboard dismiss does not submit |
