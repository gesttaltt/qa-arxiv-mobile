# TC008 – Bulk downloaded papers management

**User Story:** US002 – Manage Downloaded Papers  
**ISTQB Design Technique:** Boundary Value Analysis (0, 1, many downloaded papers)  
**Priority:** Low  
**Platform:** Both (Android / iOS)  
**Test Type:** Functional

---

**Objective:**  
Verify that the DOWNLOADED tab behaves correctly at its boundary states:
empty list, a single item, and multiple items — and that removing all items
returns the list to a clean empty state.

**Preconditions:**  
- App is installed and running.  
- DOWNLOADED tab is empty (fresh install or manually cleared).  
- Internet connectivity is active.

---

**Boundary Values:**

| Boundary | Value | Rationale |
|---|---|---|
| Below minimum | 0 downloaded papers | Empty state — UI must not crash or show stale data |
| Minimum | 1 downloaded paper | Single item — add and remove without list breaking |
| Multiple | 3+ downloaded papers | Tests list rendering and persistence for a set |

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | Open the DOWNLOADED tab with no items added | Empty-state message or illustration is shown (no crash, no leftover items) | |
| 2 | Search for `machine learning`, open the first result, and tap the download icon | Download completes without error | |
| 3 | Open the DOWNLOADED tab | Exactly **1 item** is listed | |
| 4 | Remove that single item (tap the trash icon) | DOWNLOADED tab returns to empty-state (0 items) | |
| 5 | Download **3 different papers** across two separate searches | All 3 appear in the DOWNLOADED tab | |
| 6 | Force-close the app and reopen it | All 3 downloaded items are still present (data persistence check) | |
| 7 | Remove all 3 items one by one (trash icon) | After each removal the count decreases; after the last removal the empty-state is shown | |

---

**Expected Result:**  
- Step 1: Empty-state is displayed; no residual data.  
- Step 3: Count = 1; no duplicates.  
- Step 5–6: Count = 3 and persists after app restart.  
- Step 7: Count correctly reaches 0 and empty-state returns.

**Notes:**  
- If the app allows a "Remove all" bulk action, add a step to test it with 3 items
  and verify the list empties in one action.

---

**Automation Coverage:**

| Layer | File | What it validates |
|---|---|---|
| BDD / Gherkin | `automation/features/article_data_contract.feature` — scenario 2 | Fetches 5 results and asserts every paper has a unique ID, non-empty title, and no duplicate IDs — data-layer equivalent of the bulk uniqueness check in steps 3 and 5 |
