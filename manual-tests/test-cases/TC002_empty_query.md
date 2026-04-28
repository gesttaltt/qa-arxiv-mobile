# TC002 – Search with empty query

**Objective:**  
Verify that the app handles empty search submissions gracefully.

**Preconditions:**  
- App is open on Android **or** iOS.  
- No text has been entered in the search field.

**Test Steps:**  
1. Tap the search button without entering any keyword.  

**Expected Result:**  
- The app displays a warning or validation message:  
  *“Please enter a search term.”*  
- No API request is made.  
- No crash occurs.

| Step | Expected Outcome                    | Pass/Fail |
|------|------------------------------------|-----------|
| 1    | Validation prevents empty search   |           |
| 1    | No crash or blank screen appears   |           |

---

**Platform Notes:**

| Platform | Specific behaviour to verify |
|---|---|
| Android | Toast or inline error message is announced by TalkBack if enabled |
| iOS | Validation message is readable via VoiceOver; keyboard dismiss does not submit |
