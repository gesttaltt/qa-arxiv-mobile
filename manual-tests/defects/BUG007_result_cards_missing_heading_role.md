# BUG007 – Search result cards lack heading role for screen readers

**Defect ID:** BUG007
**Linked Test Case:** TC011 – Accessibility TalkBack screen reader
**User Story:** US001 – Search for Academic Papers
**Reported by:** Jonathan Verdun
**Date reported:** 2026-05-21
**Status:** Open

---

## Environment

| Field | Value |
|---|---|
| App version | 1.2.0 (build 45) |
| Platform | Android |
| OS version | Android 13 (API 33) |
| Device | Pixel 6 Emulator |
| TalkBack version | Android Accessibility Suite 13.0 |
| Test environment | Local emulator |

---

## Summary

When navigating the search results list with TalkBack, each result card is announced as a generic list item. The paper title within each card does not carry a heading role, so users cannot use the TalkBack "navigate by heading" gesture (`Alt+H` in web equivalence) to jump between results. This makes scanning a long list of results significantly slower for screen reader users and is a partial gap against WCAG 2.1 Success Criterion 1.3.1 (Info and Relationships).

---

## Severity / Priority

| Field | Value |
|---|---|
| **Severity** | Minor |
| **Priority** | Medium |
| **Type** | Accessibility — WCAG 1.3.1 |

**Severity rationale:** Screen reader users can still reach every result by swiping right repeatedly — all required information is announced and no element is inaccessible. However, for lists with 10+ results (the app returns 12 per page), swiping through every element to reach a specific result is tedious. Heading navigation is a standard screen reader shortcut that improves usability significantly for blind users. Given that accessibility is an explicit test area (TC011), this gap should be tracked and addressed.

---

## Steps to Reproduce

1. Enable TalkBack on the Android device (Settings → Accessibility → TalkBack → On).
2. Launch arXiv Papers Mobile (version 1.2.0).
3. Perform a search for "robotics".
4. When results appear, attempt the TalkBack "navigate by heading" gesture (swipe up then right, or use the local context menu → Headings).
5. Observe whether TalkBack jumps between result card titles.

**Actual result:**
TalkBack announces each result as a list item. The "navigate by heading" gesture either does nothing or falls through to the next screen section (e.g., the bottom tab bar). Paper titles are read correctly when swiping through sequentially, but they are not landmarks for heading-based navigation.

**Expected result:**
Each result card title should be exposed as a heading (e.g., heading level 3 or an equivalent accessible landmark) so that screen reader users can skip to the next result without swiping through the authors and publication date of each card.

---

## Evidence

| Type | Reference |
|---|---|
| Screen recording (TalkBack in use) | `evidence/android/TC011_AccessibilityTalkBackTesting_Android_Pass.gif` |
| Screenshot (TalkBack active) | `evidence/screenshots/TC011_talkback.png` |
| Execution log (Issue 1) | `manual-tests/test-execution/execution-logs/TC011_execution_log.md` |

---

## Root Cause (hypothesis)

The result card title text element in the React Native component tree likely uses a `<Text>` element without an `accessibilityRole` prop, or the card itself uses `accessible={true}` which merges child content into a single announcement without heading semantics.

**Suggested fix:**
Add `accessibilityRole="header"` to the `<Text>` component that renders the paper title within each result card:

```jsx
<Text accessibilityRole="header" style={styles.title}>
  {paper.title}
</Text>
```

On Android, this maps to `AccessibilityNodeInfoCompat.setHeadingLevel()` and enables heading navigation in TalkBack. Verify the announcement with TalkBack after the change — the title should be announced with "heading" appended.

---

## Regression Risk

Low — `accessibilityRole` is an additive prop with no effect on sighted rendering. Retest TC011 (TalkBack navigation) after the fix. Also verify TC001 to ensure the change does not inadvertently alter sighted search result layout.

---

## WCAG Reference

| Criterion | Level | Status |
|---|---|---|
| 1.3.1 Info and Relationships | A | Partial pass — structure not fully conveyed to screen reader |
| 4.1.2 Name, Role, Value | A | Pass — all elements have names and roles; heading role not applied to titles |
