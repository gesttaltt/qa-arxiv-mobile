# TC010 – Offline data persistence

**User Story:** US004 – Network Connectivity
**ISTQB Design Technique:** State Transition Testing + Error Guessing
**Priority:** High
**Platform:** Both (Android / iOS)
**Test Type:** Functional – Negative

---

**Objective:**
Verify that the app preserves previously loaded data (search results, favorites)
when the device goes offline, and displays appropriate offline indicators rather
than empty or broken states.

**Preconditions:**
- App is installed and running on a device with internet connectivity.
- At least one search has been performed successfully (results are cached locally).
- At least one paper has been marked as a favorite.

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | Perform a search for `quantum computing`; confirm results are displayed | Results list is populated with papers | |
| 2 | Tap the favorite icon on the first two results | Favorites are toggled on successfully | |
| 3 | Disable WiFi and mobile data on the device | No crash; app UI remains stable | |
| 4 | Open the Favorites tab | Previously favorited papers are displayed with a note indicating offline mode | |
| 5 | Tap on a favorited paper to open its detail view | Paper title, authors, and abstract are shown (from local cache) | |
| 6 | Attempt a new search for `machine learning` | App shows an offline error message (e.g., "No internet connection") OR displays cached results with an "offline" indicator | |
| 7 | Re-enable WiFi or mobile data | Network indicator restores | |
| 8 | Repeat the search from step 6 | New results load successfully; app recovers without restart | |

---

**Expected Result:**
- Steps 3–6: Cached favorites and results remain accessible offline.
- Step 6: New searches either show cached data with an offline indicator or display a clear error message.
- Step 8: Full functionality is restored without requiring an app restart.

**Notes:**
- This test relates to TC004 (offline search) but focuses on data persistence
  rather than error messaging.
- If the app clears its cache on force-close, document this behavior as a
  finding (it affects the user experience for offline reading).
