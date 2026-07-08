# TC010 Execution Log - Offline Data Persistence

**Test Case ID:** TC010
**Test Date:** 2026-05-21
**Tester:** QA Team
**Application:** arXiv Papers Mobile
**Version:** 1.2.0 (build 45)
**Environment:** Android 13 (emulator) / iOS 17.2 (simulator)

---

## Test Environment Details

### Android Execution:
- **Device/Emulator:** Pixel 6 Emulator, Android 13 (API 33)
- **App Version:** 1.2.0 (build 45)
- **Build:** Debug
- **Network:** WiFi (toggled off/on during test)

### iOS Execution:
- **Device/Simulator:** iPhone 15 Simulator, iOS 17.2
- **App Version:** 1.2.0 (build 45)
- **Build:** Debug
- **Network:** WiFi (toggled off/on during test)

---

## Test Objective
Verify that the app preserves previously loaded data (search results, downloaded papers) when the device goes offline, and displays appropriate offline indicators rather than empty or broken states.

---

## Test Steps Execution

### Step 1: Load results with network
**Action:** Perform search for "quantum computing"; confirm results displayed
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Results loaded: 12 (Android), 12 (iOS)
- Baseline established

### Step 2: Download two papers
**Action:** Open the first two results and tap the download icon on each
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Both downloads completed successfully
- Items appeared in the DOWNLOADED tab

### Step 3: Go offline
**Action:** Disable WiFi and mobile data
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- No crash
- UI remained stable
- No error state yet (no action attempted)

### Step 4: Access downloaded papers offline
**Action:** Open the DOWNLOADED tab
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Previously downloaded papers displayed
- Offline indicator shown (subtle banner)
- All metadata visible (title, authors)

### Step 5: Open downloaded paper detail offline
**Action:** Tap on a downloaded paper
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Paper title, authors, and abstract shown from cache
- No loading spinner (data from local storage)
- Images may be missing (no network to load thumbnails) -- expected

### Step 6: Attempt new search while offline
**Action:** Attempt a new search for "machine learning"
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Offline error message displayed: "No internet connection"
- Cached results not shown as fallback (app shows error instead)
- Consistent with TC004 behavior

### Step 7: Re-enable network
**Action:** Re-enable WiFi or mobile data
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- Network restored without restart
- Indicator updated

### Step 8: Verify recovery
**Action:** Repeat search from step 6
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** [x] Pass [ ] Fail
**Notes:**
- New results loaded successfully
- App recovered without restart
- Full functionality restored

---

## Expected Results Verification

| Criterion | Android | iOS | Notes |
|-----------|---------|-----|-------|
| Downloaded papers accessible offline | [x] Pass [ ] Fail | [x] Pass [ ] Fail | From local cache |
| Paper details accessible offline | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Title/authors/abstract cached |
| Offline indicator shown | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Banner-style indicator |
| New search shows error (not crash) | [x] Pass [ ] Fail | [x] Pass [ ] Fail | Consistent with TC004 |
| Recovery after network restore | [x] Pass [ ] Fail | [x] Pass [ ] Fail | No restart needed |
| No data corruption during offline | [x] Pass [ ] Fail | [x] Pass [ ] Fail | All cached data intact |

---

## Evidence Collected

### Video Recordings:
- **Android:** [ ] Pending - Combined with TC004 evidence covers offline flow
- **iOS:** [ ] Pending - Combined with TC004 evidence covers offline flow

### Evidence Location:
- **Note:** TC010 shares offline context with TC004; TC004 GIF evidence demonstrates the error-handling portion. A dedicated TC010 recording should capture the downloaded-papers-access-offline flow specifically.

---

## Issues Found

### Issue 1:
**Platform:** Both
**Severity:** Medium
**Description:** Cached search results are NOT shown when going offline and performing a NEW search. Only downloaded papers survive offline. Users who want to re-read previous results cannot access them from search.
**Recommendation:** Consider showing last successful search results with an "offline" banner when network is unavailable, rather than only showing an error message.

---

## Overall Test Result

**Android Platform:** [x] PASS [ ] FAIL
**iOS Platform:** [x] PASS [ ] FAIL
**Overall Test Status:** [x] PASS [ ] FAIL

**Summary Notes:**
Offline data persistence works for downloaded papers (they are cached and accessible). Search results are not cached for offline reuse -- new searches while offline show an error rather than cached results. This is consistent behavior but represents a UX gap compared to apps that show cached search results with offline indicators. TC004 and TC010 together provide full offline coverage.

---

## Follow-up Actions

- [ ] Create dedicated TC010 video evidence showing downloaded-papers-access-offline flow
- [x] Update traceability matrix with results
- [ ] Report issue regarding lack of cached search result fallback
- [x] Cross-reference findings with TC004 for consistency
- [x] Document caching behavior for product team consideration

---

**Execution Completed:** 2026-05-21 13:00
**Review Required:** Yes (for Issue 1 severity assessment)
**Next Steps:** Proceed to TC011 (Accessibility TalkBack)
