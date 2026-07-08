# TC003 – Download a paper and remove it from Downloaded

**Objective:**  
Verify that the user can download a paper for offline access and remove it from the Downloaded tab.

**Preconditions:**  
- At least one paper is shown in the results list.  
- Internet is connected.  
- Testing on Android **and** iOS (run steps on each platform independently).  

**Test Steps:**  
1. Perform a valid search (`deep learning`).  
2. Open the first result's detail view.  
3. Tap the download icon (bottom-right button on the detail screen).  
4. Navigate to the "DOWNLOADED" tab.  
5. Confirm that the paper appears.  
6. Tap the trash/delete icon on the item to remove it.  
7. Refresh the list or revisit the DOWNLOADED tab.  

**Expected Result:**  
- Paper appears in the DOWNLOADED tab after downloading.  
- Paper disappears from the DOWNLOADED tab after deleting it.

| Step | Expected Outcome                     | Pass/Fail |
|------|---------------------------------------|-----------|
| 3    | Download starts, no crash             |           |
| 5    | Paper appears in DOWNLOADED tab       |           |
| 7    | Paper removed from DOWNLOADED tab     |           |

---

**Platform Notes:**

| Platform | Specific behaviour to verify |
|---|---|
| Android | Downloaded item persists after pressing the Android back button and returning to the tab |
| iOS | Downloaded item persists after swiping back via navigation gesture; no duplicate entries after fast taps |
| Both | Force-close and reopen the app — downloaded item must survive (local persistence check) |

---

**Automation Coverage:**

| Layer | File | What it validates |
|---|---|---|
| API contract | `automation/tests/test_search_api.py` — `TestArticleDataContract` | arXiv API returns all 4 fields required to display an article (`id`, `title`, `authors`, `published`) — used by both search results and downloaded articles |
| BDD / Gherkin | `automation/features/article_data_contract.feature` — scenario 1 | Same contract expressed as a Gherkin scenario; mapped to this TC |
