# BUG005 – No bulk "Remove all" action in the DOWNLOADED tab

**Defect ID:** BUG005
**Linked Test Case:** TC008 – Bulk downloaded papers management
**User Story:** US002 – Manage Downloaded Papers
**Reported by:** Jonathan Verdun
**Date reported:** 2026-05-21
**Status:** Open

---

## Environment

| Field | Value |
|---|---|
| App version | 1.2.0 (build 45) |
| Platform | Android (reproduced; iOS not tested — no device available) |
| OS version (Android) | Android 13 (API 33) |
| Device (Android) | Pixel 6 Emulator |
| Test environment | Local emulator |

---

## Summary

The DOWNLOADED tab provides no way to remove all downloaded papers at once. Users must tap the trash icon on each item individually, one at a time. There is no "Clear all" menu option, long-press selection mode, or swipe-to-delete gesture.

---

## Severity / Priority

| Field | Value |
|---|---|
| **Severity** | Minor |
| **Priority** | Low |
| **Type** | UX / Missing feature |

**Severity rationale:** The workaround (removing items one by one) works and does not cause data loss or crashes. The issue only becomes meaningfully tedious at scale — a user who has downloaded 20+ papers during a research session faces significant friction to clear their list. For a typical session with 1–5 downloaded papers it is an acceptable limitation.

---

## Steps to Reproduce

1. Launch arXiv Papers Mobile (version 1.2.0).
2. Perform multiple searches and download at least 5 papers.
3. Navigate to the DOWNLOADED tab.
4. Look for a "Clear all", "Remove all", long-press selection, or swipe-to-delete control.

**Actual result:**
No bulk action control exists. The only removal path is tapping the trash icon on each individual item. There is no context menu, no multi-select mode, and no "Edit" affordance in the DOWNLOADED tab navigation bar.

**Expected result:**
A "Clear all" option accessible from the DOWNLOADED tab (e.g., a three-dot menu in the header → "Clear all downloads") with a confirmation dialog to prevent accidental deletion. Optionally, long-press selection mode to remove a subset of downloaded papers.

---

## Evidence

| Type | Reference |
|---|---|
| Screen recording (Android) | `evidence/android/TC008_BulkDownloadedPapersManagement_Android_Pass.gif` |
| Screen recording (iOS) | Not tested — no real iOS evidence exists |

---

## Root Cause (hypothesis)

The DOWNLOADED screen likely renders a `FlatList` with per-item delete controls, but no header-level action or long-press handler to enter a selection mode. Local storage is per-item keyed, so a "Clear all" would require iterating all known keys and removing them, or storing the full list under a single key for a single-call delete.

**Suggested fix:**
Add a "Clear all" option to the DOWNLOADED tab header menu. Wrap the per-item delete calls in a `Promise.all` over all downloaded-paper keys, and show a confirmation `Alert` before executing. For multi-select support, track a `Set<string>` of selected IDs in component state and show a delete toolbar when the set is non-empty.

---

## Regression Risk

Low — additive feature addition. Retest TC003 (single download/remove) and TC008 (boundary values) and the new clear-all path after any implementation. Verify that clearing all downloads does not affect other app state (search results, cached data).
