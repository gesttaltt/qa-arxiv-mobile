# TC010 Execution Log - Offline Data Persistence

**Test Case ID:** TC010
**Test Date:** 2026-05-21
**Tester:** QA Team
**Application:** arXiv Papers Mobile
**Version:** 1.2.0 (build 45)
**Environment:** Android 13 (emulator)

---

## Test Environment Details

### Android Execution:
- **Device/Emulator:** Pixel 6 Emulator, Android 13 (API 33)
- **App Version:** 1.2.0 (build 45)
- **Build:** Debug
- **Network:** WiFi (toggled off/on during test)

### iOS Execution:
**Not executed.** No macOS/Xcode/iOS Simulator was available for this project. Unlike other
test cases, there is no placeholder GIF for TC010 on iOS at all — this test case has zero
iOS evidence, not even a watermarked stand-in.

---

## Test Objective
Verify that the app preserves previously loaded data (search results, downloaded papers) when the device goes offline, and displays appropriate offline indicators rather than empty or broken states.

---

## Test Steps Execution

### Step 1: Load results with network
**Action:** Perform search for "quantum computing"; confirm results displayed
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Notes:**
- Results loaded: 12 (Android)
- Baseline established

### Step 2: Download two papers
**Action:** Open the first two results and tap the download icon on each
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Notes:**
- Both downloads completed successfully
- Items appeared in the DOWNLOADED tab

### Step 3: Go offline
**Action:** Disable WiFi and mobile data
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Notes:**
- No crash
- UI remained stable
- No error state yet (no action attempted)

### Step 4: Access downloaded papers offline
**Action:** Open the DOWNLOADED tab
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Notes:**
- Previously downloaded papers displayed
- Offline indicator shown (subtle banner)
- All metadata visible (title, authors)

### Step 5: Open downloaded paper detail offline
**Action:** Tap on a downloaded paper
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Notes:**
- Paper title, authors, and abstract shown from cache
- No loading spinner (data from local storage)
- Images may be missing (no network to load thumbnails) -- expected

### Step 6: Attempt new search while offline
**Action:** Attempt a new search for "machine learning"
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Notes:**
- Offline error message displayed: "No internet connection"
- Cached results not shown as fallback (app shows error instead)
- Consistent with TC004 behavior

### Step 7: Re-enable network
**Action:** Re-enable WiFi or mobile data
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Notes:**
- Network restored without restart
- Indicator updated

### Step 8: Verify recovery
**Action:** Repeat search from step 6
**Android Result:** [x] Pass [ ] Fail
**iOS Result:** N/A — Not Executed
**Notes:**
- New results loaded successfully
- App recovered without restart
- Full functionality restored

---

## Expected Results Verification

| Criterion | Android | iOS | Notes |
|-----------|---------|-----|-------|
| Downloaded papers accessible offline | [x] Pass [ ] Fail | N/A | From local cache |
| Paper details accessible offline | [x] Pass [ ] Fail | N/A | Title/authors/abstract cached |
| Offline indicator shown | [x] Pass [ ] Fail | N/A | Banner-style indicator |
| New search shows error (not crash) | [x] Pass [ ] Fail | N/A | Consistent with TC004 |
| Recovery after network restore | [x] Pass [ ] Fail | N/A | No restart needed |
| No data corruption during offline | [x] Pass [ ] Fail | N/A | All cached data intact |

---

## Evidence Collected

### Video Recordings:
- **Android:** [x] Completed - `TC010_OfflineDataPersistence_Android_Pass.gif` (genuine recording, no watermark)
- **iOS:** [ ] Not executed - no file exists, not even a placeholder

### Evidence Location:
- **Android:** `evidence/android/TC010_OfflineDataPersistence_Android_Pass.gif`
- **iOS:** None — not executed, no evidence of any kind

---

## Issues Found

### Issue 1:
**Platform:** Android
**Severity:** Medium
**Description:** Cached search results are NOT shown when going offline and performing a NEW search. Only downloaded papers survive offline. Users who want to re-read previous results cannot access them from search.
**Recommendation:** Consider showing last successful search results with an "offline" banner when network is unavailable, rather than only showing an error message.

---

## Overall Test Result

**Android Platform:** [x] PASS [ ] FAIL
**iOS Platform:** Not Executed — no iOS device/simulator available
**Overall Test Status:** [x] PASS (Android only) [ ] FAIL

**Summary Notes:**
Offline data persistence works for downloaded papers on Android (they are cached and accessible). Search results are not cached for offline reuse -- new searches while offline show an error rather than cached results. This is consistent behavior but represents a UX gap compared to apps that show cached search results with offline indicators. TC004 and TC010 together provide full offline coverage on Android. iOS was not executed at all for this test case.

---

## Follow-up Actions

- [x] Create dedicated TC010 Android video evidence showing downloaded-papers-access-offline flow
- [ ] Execute TC010 on iOS when a real device or simulator is available
- [x] Update traceability matrix with results
- [ ] Report issue regarding lack of cached search result fallback
- [x] Cross-reference findings with TC004 for consistency
- [x] Document caching behavior for product team consideration

---

**Execution Completed:** 2026-05-21 13:00
**Review Required:** Yes (for Issue 1 severity assessment)
**Next Steps:** Proceed to TC011 (Accessibility TalkBack)
