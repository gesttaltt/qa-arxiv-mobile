# TC004 – Search offline behavior

**User Story:** US001 – Search for Academic Papers  
**ISTQB Design Technique:** State Transition Testing + Error Guessing  
**Priority:** Medium  
**Platform:** Both (Android / iOS)  
**Test Type:** Functional – Negative

---

**Objective:**  
Verify that the app responds gracefully when the user attempts a search with no
network connectivity, showing a clear error state instead of crashing or hanging
indefinitely.

**Preconditions:**  
- App is installed and running.  
- At least one previous search has been performed (results may be cached).  
- Device network (WiFi and mobile data) is **disabled** before step 1.

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | Disable WiFi and mobile data on the device | No crash; app UI remains stable | |
| 2 | Tap the search field and type `machine learning` | Text is accepted in the field | |
| 3 | Tap the Search button | App shows an offline/network error message (e.g., *"No internet connection"* or *"Unable to reach server"*) | |
| 4 | Confirm no crash or blank screen is displayed | App is still interactive and navigable | |
| 5 | Re-enable WiFi or mobile data | Network indicator restores | |
| 6 | Repeat the same search | Results load successfully | |

---

**Expected Result:**  
- Steps 1–4: App displays a descriptive error message; no crash, no infinite spinner.  
- Step 6: App recovers automatically and returns valid results once connectivity is restored.

**Notes:**  
- If the app caches previous results, confirm the cached list is shown with a visible
  "offline" indicator rather than a live result set.  
- Relates to TC010 (Offline data persistence) which tests cached data behaviour in depth.
