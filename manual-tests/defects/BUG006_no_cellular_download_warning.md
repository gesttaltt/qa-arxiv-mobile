# BUG006 – No warning before downloading PDF over cellular data

**Defect ID:** BUG006
**Linked Test Case:** TC009 – WiFi to Cellular network transition
**User Story:** US003 – Download and View PDFs; US004 – Network Connectivity
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
| Device (Android) | Pixel 6 Emulator (cellular simulated via emulator network settings) |
| Device (iOS) | iPhone 15 Simulator (cellular simulated via Network Link Conditioner) |
| Test environment | Local emulator / simulator |

---

## Summary

When the device is on a mobile/cellular connection (WiFi disabled) and the user taps "Download PDF", the download starts immediately with no prompt or warning. Users on metered data plans can unknowingly consume significant data — arXiv PDFs typically range from 500 KB to 5 MB — without being informed.

---

## Severity / Priority

| Field | Value |
|---|---|
| **Severity** | Minor |
| **Priority** | Low |
| **Type** | UX / Data awareness |

**Severity rationale:** No crash, data corruption, or functional failure occurs. The concern is user awareness: downloading academic papers over a metered cellular plan is a deliberate choice that should be surfaced. This pattern is established by the App Store, Netflix, and Podcast apps on both platforms. The impact is higher for users in regions where mobile data is expensive or capped.

---

## Steps to Reproduce

1. Launch arXiv Papers Mobile (version 1.2.0) on Android 13 or iOS 17.2.
2. Disable WiFi; ensure only mobile/cellular data is active.
3. Search for any keyword (e.g., "robotics") and wait for results.
4. Open a paper detail view.
5. Tap the **Download PDF** button.

**Actual result:**
The download starts immediately. No dialog, alert, or inline message warns the user that the download will consume cellular data. The download progress indicator appears without any prior consent prompt.

**Expected result:**
Before initiating a download over cellular, the app should display an alert such as:
*"You are not connected to WiFi. Downloading this PDF may use mobile data. Continue?"*
with **Download** and **Cancel** options. Alternatively, provide a Settings toggle: "Download over cellular: On/Off" that users can set once.

---

## Evidence

| Type | Reference |
|---|---|
| Screen recording (network transition — Android) | `evidence/android/TC009_WiFitoCellularTransition_Android_Pass.gif` |
| Screen recording (network transition — iOS) | `evidence/ios/TC009_WiFitoCellularTransition_iOS_Pass.gif` |
| Screenshot (network state) | `evidence/screenshots/TC009_network_transition.png` |

---

## Root Cause (hypothesis)

The download handler does not check `NetInfo.type` before starting the request. The component likely calls the PDF URL directly without consulting the network type. No `NetInfo` event listener is wired to gate downloads.

**Suggested fix:**
Before initiating any download, call `NetInfo.fetch()` (from `@react-native-community/netinfo`). If `state.type === 'cellular'`, display an `Alert.alert()` with Cancel/Download options. Store the user's preference in AsyncStorage so they are not prompted on every download if they chose "always allow".

---

## Regression Risk

Low — change is isolated to the download initiation flow. Retest TC005 (PDF download on WiFi — should not trigger the alert) and TC009 (download on cellular — should trigger the alert) after the fix.
