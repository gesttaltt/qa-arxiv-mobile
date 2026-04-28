# TC008 – Bulk favorite operations

**User Story:** US002 – Manage Favorite Papers  
**ISTQB Design Technique:** Boundary Value Analysis (0, 1, many favorites)  
**Priority:** Low  
**Platform:** Both (Android / iOS)  
**Test Type:** Functional

---

**Objective:**  
Verify that the Favorites feature behaves correctly at its boundary states:
empty list, a single item, and multiple items — and that removing all items
returns the list to a clean empty state.

**Preconditions:**  
- App is installed and running.  
- Favorites list is empty (fresh install or manually cleared).  
- Internet connectivity is active.

---

**Boundary Values:**

| Boundary | Value | Rationale |
|---|---|---|
| Below minimum | 0 favorites | Empty state — UI must not crash or show stale data |
| Minimum | 1 favorite | Single item — add and remove without list breaking |
| Multiple | 3+ favorites | Tests list rendering and persistence for a set |

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | Open the Favorites tab with no items added | Empty-state message or illustration is shown (no crash, no leftover items) | |
| 2 | Search for `machine learning` and mark the **first** result as a favorite | Star icon toggles to filled/active state | |
| 3 | Open the Favorites tab | Exactly **1 item** is listed | |
| 4 | Remove that single item from Favorites (tap star again) | Favorites tab returns to empty-state (0 items) | |
| 5 | Mark **3 different papers** as favorites across two separate searches | All 3 appear in the Favorites tab | |
| 6 | Force-close the app and reopen it | All 3 favorites are still present (data persistence check) | |
| 7 | Remove all 3 favorites one by one | After each removal the count decreases; after the last removal the empty-state is shown | |

---

**Expected Result:**  
- Step 1: Empty-state is displayed; no residual data.  
- Step 3: Count = 1; no duplicates.  
- Step 5–6: Count = 3 and persists after app restart.  
- Step 7: Count correctly reaches 0 and empty-state returns.

**Notes:**  
- If the app allows a "Remove all favorites" bulk action, add a step to test it with 3 items
  and verify the list empties in one action.
