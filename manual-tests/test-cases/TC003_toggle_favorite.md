# TC003 – Toggle paper as favorite

**Objective:**  
Verify that the user can mark and unmark a paper as favorite.

**Preconditions:**  
- At least one paper is shown in the results list.  
- Internet is connected.  
- Testing on Android **and** iOS (run steps on each platform independently).  

**Test Steps:**  
1. Perform a valid search (`deep learning`).  
2. Tap the star/favorite icon on the first result.  
3. Navigate to the “Favorites” tab.  
4. Confirm that the paper appears.  
5. Tap the star again to remove it.  
6. Refresh the list or revisit Favorites.  

**Expected Result:**  
- Star icon toggles between filled/outlined.  
- Paper appears in Favorites after marking.  
- Paper disappears after unmarking.

| Step | Expected Outcome                  | Pass/Fail |
|------|----------------------------------|-----------|
| 2    | Favorite icon toggled             |           |
| 4    | Paper appears in favorites list   |           |
| 6    | Paper removed from favorites list |           |

---

**Platform Notes:**

| Platform | Specific behaviour to verify |
|---|---|
| Android | Favorite persists after pressing the Android back button and returning to the tab |
| iOS | Favorite persists after swiping back via navigation gesture; no duplicate entries after fast taps |
| Both | Force-close and reopen the app — favourite state must survive (local persistence check) |
