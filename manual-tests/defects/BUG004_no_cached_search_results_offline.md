# BUG004 – Cached search results not shown when going offline

**Defect ID:** BUG004
**Linked Test Cases:** TC004 – Search offline behavior; TC010 – Offline data persistence
**User Story:** US001 – Search for Academic Papers; US004 – Network Connectivity
**Reported by:** Jonathan Verdun
**Date reported:** 2026-05-21
**Status:** Open

---

## Environment

| Field | Value |
|---|---|
| App version | 1.2.0 (build 45) |
| Platform | Both (Android + iOS) |
| OS version (Android) | Android 13 (API 33) |
| OS version (iOS) | iOS 17.2 |
| Device (Android) | Pixel 6 Emulator |
| Device (iOS) | iPhone 15 Simulator |
| Test environment | Local emulator / simulator |

---

## Summary

After the user performs a successful search online, if the device loses network connectivity and the user attempts the same (or a new) search, the app displays a "No internet connection" error and shows an empty screen. Previously loaded results are not served from a local cache. Only Favorites data survives offline; search results do not.

---

## Severity / Priority

| Field | Value |
|---|---|
| **Severity** | Minor |
| **Priority** | Medium |
| **Type** | UX / Offline experience |

**Severity rationale:** The current behavior is not a crash — the error message is clear and the app remains interactive. However, the lack of a cached-result fallback means users in transit (underground, airplane mode, poor signal) lose access to results they just had on screen. Favorites are correctly cached, so the infrastructure for local persistence exists; search results are simply not included in it.

---

## Steps to Reproduce

1. Launch arXiv Papers Mobile (version 1.2.0) on Android 13 or iOS 17.2 with WiFi active.
2. Search for "quantum computing" — confirm results are displayed (12 results).
3. Note the titles of the first 3 results.
4. Disable WiFi and mobile data.
5. Tap the search field and type "quantum computing" (same query).
6. Tap the Search button.

**Actual result:**
The app shows an error message ("No internet connection"). The results from step 2 are not displayed. The screen is empty except for the error state.

**Expected result (aspirational):**
The app should display the results from the last successful search for this query, with a clearly visible "Offline — showing cached results" banner. This is consistent with the behavior of apps like Google Scholar and standard RSS readers.

**Acceptable minimum alternative:**
If full result caching is out of scope, at minimum the error screen should offer a "View saved favorites" shortcut so the user has a navigation path to offline-accessible content.

---

## Evidence

| Type | Reference |
|---|---|
| Screen recording (offline error — Android) | `evidence/android/TC004_SearchOfflineBehavior_Android_Pass.gif` |
| Screen recording (offline error — iOS) | `evidence/ios/TC004_SearchOfflineBehavior_iOS_Pass.gif` |
| Screenshot (offline error state) | `evidence/screenshots/TC004_offline_error.png` |
| Execution log (TC010 — Issue 1) | `manual-tests/test-execution/execution-logs/TC010_execution_log.md` |

---

## Root Cause (hypothesis)

The search results are fetched from the arXiv API and rendered directly from the API response, with no write-through to AsyncStorage or SQLite. When the network is unavailable, no local data source is consulted. The `Favorites` feature uses AsyncStorage, confirming the app already has a persistence layer — it is simply not used for search result caching.

**Suggested fix:**
After a successful API response, serialize the results array and store it in AsyncStorage keyed by the query string. On network failure, check AsyncStorage for the query key before rendering the error state. Clear stale cache entries after 24 hours or on each successful fresh load.

---

## Regression Risk

Medium — change touches the search data flow (TC001, TC004) and the offline handling path (TC004, TC009, TC010). Retest TC001, TC004, TC009, and TC010 after any caching layer is added to verify no regressions in result freshness or state consistency.
