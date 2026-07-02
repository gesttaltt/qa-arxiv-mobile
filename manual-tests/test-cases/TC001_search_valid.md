# TC001 – Search with valid keyword

**Objective:**  
Verify that the user can successfully search for academic papers using a valid keyword.

**Preconditions:**  
- App is installed and running on an Android emulator/device **or** iOS simulator/device.  
- User has internet connection.  

**Test Steps:**  
1. Launch the app.  
2. Tap on the search input field.  
3. Type the keyword: `quantum`.  
4. Tap the “Search” button.  
5. Observe the results list.  

**Expected Result:**  
- At least one result appears in the list.  
- Each result displays title, authors, and publication date.  
- No crash or error message is shown.

| Step | Expected Outcome                  | Pass/Fail |
|------|----------------------------------|-----------|
| 1    | App loads without errors         |           |
| 3    | Input accepts the keyword        |           |
| 5    | Results are shown successfully   |           |

---

**Platform Notes:**

| Platform | Specific behaviour to verify |
|---|---|
| Android | Back button returns to home without crashing |
| iOS | Keyboard dismiss via swipe-down works; results remain visible after keyboard hides |
| Both | Landscape orientation retains results without layout breaking |

---

**Automation Coverage:**

| Layer | File | What it validates |
|---|---|---|
| API integration | `automation/tests/test_search_api.py` — `TestArxivSearchAPI` | Valid keyword returns HTTP 200, non-empty results, correct Content-Type |
| API integration | `automation/tests/test_search_valid.py` — `TestValidSearchQueries` | Multiple academic keywords all return ≥1 result; max_results param respected |
| API — pagination | `automation/tests/test_advanced_search.py` — `TestPagination` | start=0 and start=5 return non-overlapping IDs; opensearch:startIndex matches offset; totalResults stable across pages |
| API — author search | `automation/tests/test_advanced_search.py` — `TestAuthorSearch` | au: prefix returns results; au: is more specific than all: (EP — distinct query class); author name present in results |
| BDD / Gherkin | `automation/features/search.feature` — `Valid keyword returns results` + Scenario Outline | Gherkin-readable version of TC001 across 3 academic domains |
