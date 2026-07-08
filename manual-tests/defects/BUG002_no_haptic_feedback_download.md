# BUG002 – No haptic or animation feedback when downloading a paper

**Defect ID:** BUG002
**Linked Test Case:** TC003 – Download a paper and remove it from Downloaded
**User Story:** US002 – Manage Downloaded Papers
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

When the user taps the download icon on a paper's detail screen, the item is added to the DOWNLOADED tab with no haptic feedback and no transition animation. On both platforms the state change is abrupt — there is no tactile or motion cue confirming the download started or completed.

---

## Severity / Priority

| Field | Value |
|---|---|
| **Severity** | Minor |
| **Priority** | Low |
| **Type** | UX / Polish |

**Severity rationale:** Core functionality works correctly (the paper downloads and persists in the DOWNLOADED tab). The gap is in feedback quality, not function. However, the lack of tactile or visual confirmation increases uncertainty on first use and feels inconsistent with platform norms on both Android and iOS.

---

## Steps to Reproduce

1. Launch arXiv Papers Mobile (version 1.2.0) on Android 13 or iOS 17.2.
2. Search for any keyword (e.g., "deep learning") and open the first result's detail view.
3. Locate the download icon (bottom-right of the detail screen).
4. Tap the download icon.
5. Observe feedback at the moment of the tap.
6. Navigate to the DOWNLOADED tab and tap the trash icon to remove the item.
7. Observe feedback at the moment of the second tap.

**Actual result:**
The item is added to (or removed from) the DOWNLOADED tab with no visible transition. No haptic pulse is emitted on either platform. No scale, fade, or progress animation is played during or after the download.

**Expected result:**
- **Haptic:** A short, light haptic tap (e.g., `UIImpactFeedbackGenerator.impactOccurred()` on iOS, `Vibrator.vibrate(50ms)` or `HapticFeedbackConstants.VIRTUAL_KEY` on Android) should fire when the download starts and completes.
- **Animation:** A determinate or indeterminate progress indicator during download, followed by a brief success confirmation (e.g., icon swap with a ~150 ms transition), would make the state change feel intentional.

---

## Evidence

| Type | Reference |
|---|---|
| Screen recording (Android) | `evidence/android/TC003_DownloadAndRemovePaper_Android_Pass.gif` |
| Screen recording (iOS) | `evidence/ios/TC003_DownloadAndRemovePaper_iOS_Pass.gif` |
| Before screenshot | `evidence/screenshots/TC003_before_download.png` |
| After screenshot | `evidence/screenshots/TC003_after_download.png` |

---

## Root Cause (hypothesis)

The download handler fetches the PDF, persists it to local storage, and updates the DOWNLOADED list state, but does not call any platform feedback API. The component likely uses a simple `onPress` handler without a `Vibration`/`Haptics` call or a progress `Animated.View`.

**Suggested fix:**
- Add `ReactNativeHapticFeedback.trigger('impactLight')` (via `react-native-haptic-feedback`) when the download starts and again on completion.
- Show a progress indicator (`ActivityIndicator` or a determinate bar) on the download icon while the fetch is in flight.

---

## Regression Risk

Low — change is additive (no existing logic altered). Smoke-retest TC003 after the fix to confirm haptic fires and the progress indicator displays without introducing state persistence regressions.
