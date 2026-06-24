# BUG003 – No cancel option during in-progress PDF download

**Defect ID:** BUG003
**Linked Test Case:** TC005 – PDF download and viewing
**User Story:** US003 – Download and View PDFs
**Reported by:** Jonathan Verdun
**Date reported:** 2026-05-21
**Status:** Open

---

## Environment

| Field | Value |
|---|---|
| App version | 1.2.0 (build 45) |
| Platform | Android (reproduced; iOS download modal not tested for cancel) |
| OS version | Android 13 (API 33) |
| Device | Pixel 6 Emulator |
| Network | WiFi (download time ~4 s) |
| Test environment | Local emulator |

---

## Summary

Once a PDF download is initiated, the download progress indicator (percentage bar) is displayed but offers no cancel or dismiss control. The user has no way to abort an in-progress download — they must wait for it to complete or force-close the app.

---

## Severity / Priority

| Field | Value |
|---|---|
| **Severity** | Minor |
| **Priority** | Medium |
| **Type** | UX / Missing control |

**Severity rationale:** This does not cause a crash or data loss. However, downloads over slow connections (or large PDFs) can take 15–30 seconds. Tapping download accidentally or changing your mind leaves the user with no recovery path short of a force-close, which is a poor experience.

---

## Steps to Reproduce

1. Launch arXiv Papers Mobile (version 1.2.0) on Android 13.
2. Search for "quantum entanglement" and wait for results.
3. Tap the first result to open the paper detail view.
4. Tap the **Download PDF** button.
5. Observe the progress indicator while the download is in progress.
6. Attempt to cancel or dismiss the download.

**Actual result:**
A progress bar showing download percentage appears. There is no cancel button, close icon, or back-navigation affordance that aborts the download. Pressing the system back button navigates away from the screen but the download continues (or its status becomes unknown to the user).

**Expected result:**
A cancel (×) button or "Cancel" link should be displayed alongside the progress indicator. Tapping it should abort the network request and return the button to its initial "Download PDF" state.

---

## Evidence

| Type | Reference |
|---|---|
| Screen recording (Android) | `evidence/android/TC005_PDFDownloadandViewing_Android_Pass.gif` |
| PDF viewer screenshot | `evidence/screenshots/TC005_pdf_viewer.png` |

---

## Root Cause (hypothesis)

The download is likely initiated with a `fetch()` or `react-native-fs` download call with no `AbortController` attached. The UI only renders the progress value and does not pass a cancel callback to the download component.

**Suggested fix:**
Attach an `AbortController` to the fetch call before starting. Render a cancel button in the download progress UI that calls `controller.abort()` and resets the download state to idle.

---

## Regression Risk

Low — add cancel path alongside existing download path. Retest TC005 steps 3–4 after the fix. Also verify TC009 (download over cellular) to confirm the cancel path works across network types.
