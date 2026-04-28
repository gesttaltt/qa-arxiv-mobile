# BUG001 – Infinite spinner on search when network is unavailable

**Defect ID:** BUG001  
**Linked Test Case:** TC004 – Search offline behavior  
**User Story:** US001 – Search for Academic Papers  
**Reported by:** QA Tester  
**Date reported:** 2026-04-01  
**Status:** Open

---

## Environment

| Field | Value |
|---|---|
| App version | 1.2.0 (build 45) |
| Platform | Android |
| OS version | Android 13 (API 33) |
| Device | Pixel 6 Emulator |
| Network state | WiFi disabled, Mobile data disabled |
| Appium version | 2.4.1 |
| Test environment | Local emulator |

---

## Summary

When the user submits a search with no internet connection, the app shows a loading
spinner that never resolves. No error message is displayed and the UI becomes
unresponsive — the user cannot dismiss the spinner or navigate away without
force-closing the app.

---

## Severity / Priority

| Field | Value |
|---|---|
| **Severity** | Major |
| **Priority** | High |
| **Type** | Functional – Negative scenario not handled |

**Severity rationale:** The app is effectively frozen; the only recovery is a force-close,
which means loss of any unsaved state. Users on unreliable connections will hit this often.

---

## Steps to Reproduce

1. Install version 1.2.0 on a Pixel 6 emulator (Android 13).
2. Disable WiFi and mobile data via **Settings → Network & internet**.
3. Open the app.
4. Tap the search field and type `machine learning`.
5. Tap the **Search** button.

**Actual result:**  
A circular loading spinner appears and never disappears. The search field and all
navigation controls become unresponsive. The app must be force-closed to recover.

**Expected result:**  
Within 10 seconds the app should display an error message such as:
*"No internet connection. Please check your network and try again."*
The search field and navigation remain interactive.

---

## Evidence

| Type | Reference |
|---|---|
| Screen recording | `manual-tests/test-execution/evidence/BUG001_spinner_offline.mp4` *(placeholder)* |
| Screenshot | `manual-tests/test-execution/evidence/BUG001_spinner_screenshot.png` *(placeholder)* |
| Logcat output | Network timeout logged at `NetworkModule.js:87` — no catch block for `ENOTFOUND` |

---

## Root Cause (hypothesis)

The search function dispatches a `fetch()` call with no timeout configured and no
`.catch()` handler for network errors. When the request hangs, the loading state is
never reset to `false`, leaving the spinner permanently visible.

**Suggested fix:** Add a `timeout` option to the `fetch` call (e.g., 10 s via
`AbortController`) and handle `network request failed` errors by dispatching an
error state that renders a user-facing message.

---

## Regression Risk

Medium — any change to the search network layer could affect TC001 (valid search)
and TC009 (WiFi-to-cellular transition). Re-run TC001, TC004, and TC009 after the fix.
