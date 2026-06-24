# BUG005 – No bulk "Remove all" action in Favorites

**Defect ID:** BUG005
**Linked Test Case:** TC008 – Bulk favorite operations
**User Story:** US002 – Manage Favorite Papers
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

The Favorites tab provides no way to remove all saved papers at once. Users must tap the star icon on each paper individually, one at a time. There is no "Clear all" menu option, long-press selection mode, or swipe-to-delete gesture.

---

## Severity / Priority

| Field | Value |
|---|---|
| **Severity** | Minor |
| **Priority** | Low |
| **Type** | UX / Missing feature |

**Severity rationale:** The workaround (removing items one by one) works and does not cause data loss or crashes. The issue only becomes meaningfully tedious at scale — a user who has saved 20+ papers during a research session faces significant friction to clear their list. For a typical session with 1–5 favorites it is an acceptable limitation.

---

## Steps to Reproduce

1. Launch arXiv Papers Mobile (version 1.2.0).
2. Perform multiple searches and mark at least 5 papers as favorites.
3. Navigate to the Favorites tab.
4. Look for a "Clear all", "Remove all", long-press selection, or swipe-to-delete control.

**Actual result:**
No bulk action control exists. The only removal path is tapping the star icon on each individual paper. There is no context menu, no multi-select mode, and no "Edit" affordance in the Favorites tab navigation bar.

**Expected result:**
A "Clear all" option accessible from the Favorites tab (e.g., a three-dot menu in the header → "Clear all favorites") with a confirmation dialog to prevent accidental deletion. Optionally, long-press selection mode to remove a subset of favorites.

---

## Evidence

| Type | Reference |
|---|---|
| Screen recording (Android) | `evidence/android/TC008_BulkFavoriteOperations_Android_Pass.gif` |
| Screen recording (iOS) | `evidence/ios/TC008_BulkFavoriteOperations_iOS_Pass.gif` |

---

## Root Cause (hypothesis)

The Favorites screen likely renders a `FlatList` with per-item toggle controls, but no header-level action or long-press handler to enter a selection mode. AsyncStorage persistence is per-item keyed, so a "Clear all" would require iterating all known keys and removing them, or storing the full list under a single key for a single-call delete.

**Suggested fix:**
Add a "Clear all" option to the Favorites screen header menu. Wrap the `AsyncStorage.removeItem` calls in a `Promise.all` over all favorited-paper keys, and show a confirmation `Alert` before executing. For multi-select support, track a `Set<string>` of selected IDs in component state and show a delete toolbar when the set is non-empty.

---

## Regression Risk

Low — additive feature addition. Retest TC003 (single toggle), TC008 (boundary values), and the new clear-all path after any implementation. Verify that clearing all favorites does not affect other app state (search results, cached data).
