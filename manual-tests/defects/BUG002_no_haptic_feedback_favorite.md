# BUG002 – No haptic or animation feedback when toggling favorite

**Defect ID:** BUG002
**Linked Test Case:** TC003 – Toggle paper as favorite
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

When the user taps the star icon to add or remove a paper from Favorites, the icon switches between outlined and filled states instantly with no haptic feedback and no transition animation. On both platforms the state change is abrupt — there is no tactile or motion cue to confirm the action was registered.

---

## Severity / Priority

| Field | Value |
|---|---|
| **Severity** | Minor |
| **Priority** | Low |
| **Type** | UX / Polish |

**Severity rationale:** Core functionality works correctly (state toggles and persists). The gap is in feedback quality, not function. However, the lack of tactile confirmation increases uncertainty on first use and feels inconsistent with platform norms on both Android and iOS.

---

## Steps to Reproduce

1. Launch arXiv Papers Mobile (version 1.2.0) on Android 13 or iOS 17.2.
2. Search for any keyword (e.g., "deep learning") and wait for results.
3. Locate the star icon on any result card (top-right corner).
4. Tap the star icon to add the paper to Favorites.
5. Observe feedback at the moment of the tap.
6. Tap the star again to remove the paper from Favorites.
7. Observe feedback at the moment of the second tap.

**Actual result:**
The star icon changes from outline (grey) to filled (yellow/gold) or back instantly. No haptic pulse is emitted on either platform. No scale, fade, or color-transition animation is played. The icon simply swaps between two static images.

**Expected result:**
- **Haptic:** A short, light haptic tap (e.g., `UIImpactFeedbackGenerator.impactOccurred()` on iOS, `Vibrator.vibrate(50ms)` or `HapticFeedbackConstants.VIRTUAL_KEY` on Android) should fire at the moment of the state change.
- **Animation:** A subtle scale pulse (e.g., icon scales to 1.3× then returns to 1×) or a brief color transition (grey → yellow over ~150 ms) would make the state change feel intentional.

---

## Evidence

| Type | Reference |
|---|---|
| Screen recording (Android) | `evidence/android/TC003_TogglePaperasFavorite_Android_Pass.gif` |
| Screen recording (iOS) | `evidence/ios/TC003_TogglePaperasFavorite_iOS_Pass.gif` |
| Before screenshot | `evidence/screenshots/TC003_before_favorite.png` |
| After screenshot | `evidence/screenshots/TC003_after_favorite.png` |

---

## Root Cause (hypothesis)

The favorite toggle handler updates React Native state and persists to AsyncStorage but does not call any platform feedback API. The component likely uses a simple `onPress` handler without a `Vibration` or `Haptics` call, and the icon swap is a direct conditional render (`isFavorite ? filledStar : outlineStar`) with no transition style.

**Suggested fix:**
- Add `ReactNativeHapticFeedback.trigger('impactLight')` (via `react-native-haptic-feedback`) on toggle.
- Wrap the star icon in an `Animated.View` with a scale sequence (`Animated.sequence([Animated.timing(scale, {toValue: 1.3}), Animated.timing(scale, {toValue: 1})])`).

---

## Regression Risk

Low — change is additive (no existing logic altered). Smoke-retest TC003 after the fix to confirm haptic fires and animation plays without introducing state persistence regressions.
