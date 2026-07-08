# 📊 Test Traceability Matrix with Evidence Links

This document provides complete traceability from requirements to test execution with verifiable evidence.

**iOS was never executed** on a real or virtual device (no macOS/Xcode/iOS Simulator
available). Where an "iOS Execution" link appears below, it points to a placeholder — the
Android recording with a "Pending macOS environment" banner overlaid — not real iOS
evidence. See [`evidence/README.md`](evidence/README.md) for the full breakdown, including
which screenshots are genuine vs. mislabeled/synthetic.

## 🎯 Real Execution Status Overview

| Test Case ID | Description | Android Status | iOS Status | Evidence Collected |
|--------------|-------------|----------------|------------|-------------------|
| TC001 | Search with valid keyword | ✅ Passed | ⏸ Not Executed | Android GIF + Screenshot |
| TC002 | Search with empty input | ✅ Passed | ⏸ Not Executed | Android GIF + Screenshot |
| TC003 | Download a paper and remove it from Downloaded | ✅ Passed | ⏸ Not Executed | Android GIF + Before/After screenshots |
| TC004 | Search offline behavior | ✅ Passed | ⏸ Not Executed | Android GIF (screenshot is generic, not the error state) |
| TC005 | PDF download and viewing | ✅ Passed | ⏸ Not Executed | Android GIF + Screenshot |
| TC006 | iOS Safari PDF integration | N/A | ⏸ Not Executed | None — placeholder GIF, synthetic mockup screenshot |
| TC007 | Android intent handling | ✅ Passed | N/A | Android GIF (screenshot is generic, not the intent chooser) |
| TC008 | Bulk downloaded papers management | ✅ Passed | ⏸ Not Executed | Android GIF |
| TC009 | WiFi to cellular transition | ✅ Passed | ⏸ Not Executed | Android GIF (screenshot is generic, not the transition state) |
| TC010 | Offline data persistence | ✅ Passed | ⏸ Not Executed | Dedicated Android GIF; no iOS evidence at all |
| TC011 | Accessibility TalkBack | ✅ Passed | N/A | Android GIF (screenshot is generic, not TalkBack-specific) |

---

## 📱 Test Execution Evidence

### TC001 - Search with Valid Keyword

**Requirement:** US001 - Search for Academic Papers  
**Priority:** High  
**Platforms:** Android (executed) + iOS (designed, not executed)

#### Evidence Links:
- **Android Execution:** [evidence/android/TC001_SearchwithValidKeyword_Android_Pass.gif](evidence/android/TC001_SearchwithValidKeyword_Android_Pass.gif)
- **iOS Execution:** Not executed — `evidence/ios/TC001_SearchwithValidKeyword_iOS_Pass.gif` is a placeholder, not real evidence
- **Screenshots:**
  - Android search results: `evidence/screenshots/TC001_android_search_results.png`
  - "iOS search results": `evidence/screenshots/TC001_ios_search_results.png` is a synthetic mockup, not a real capture

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass (Android only)
- **Notes:** Search returns relevant results; cards display title, authors, and date. Verified on Android only.

---

### TC002 - Search with Empty Input

**Requirement:** US001 - Search for Academic Papers  
**Priority:** High  
**Platforms:** Android (executed) + iOS (designed, not executed)

#### Evidence Links:
- **Android Execution:** [evidence/android/TC002_SearchwithEmptyQuery_Android_Pass.gif](evidence/android/TC002_SearchwithEmptyQuery_Android_Pass.gif)
- **iOS Execution:** Not executed — `evidence/ios/TC002_SearchwithEmptyQuery_iOS_Pass.gif` is a placeholder, not real evidence
- **Screenshots:**
  - Android empty search: `evidence/screenshots/TC002_android_empty_search.png`

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass (Android only)
- **Notes:** Validation message shown when search attempted with empty field. No app crash observed. API layer also validated.

---

### TC003 - Download a Paper and Remove It from Downloaded

**Requirement:** US002 - Manage Downloaded Papers  
**Priority:** High  
**Platforms:** Android (executed) + iOS (designed, not executed)

#### Evidence Links:
- **Android Execution:** [evidence/android/TC003_DownloadAndRemovePaper_Android_Pass.gif](evidence/android/TC003_DownloadAndRemovePaper_Android_Pass.gif)
- **iOS Execution:** Not executed — `evidence/ios/TC003_DownloadAndRemovePaper_iOS_Pass.gif` is a placeholder, not real evidence
- **Screenshots:**
  - Before download: `evidence/screenshots/TC003_before_download.png`
  - After download: `evidence/screenshots/TC003_after_download.png`

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass (Android only)
- **Notes:** Download and removal work correctly. Item appears in the DOWNLOADED tab after download and disappears after tapping the trash icon.

### TC004 - Search Offline Behavior

**Requirement:** US001 - Search for Academic Papers
**Priority:** Medium
**Platforms:** Android (executed) + iOS (designed, not executed)

#### Evidence Links:
- **Android Execution:** [evidence/android/TC004_SearchOfflineBehavior_Android_Pass.gif](evidence/android/TC004_SearchOfflineBehavior_Android_Pass.gif)
- **iOS Execution:** Not executed — `evidence/ios/TC004_SearchOfflineBehavior_iOS_Pass.gif` is a placeholder, not real evidence
- **Screenshots:**
  - `evidence/screenshots/TC004_offline_error.png` is mislabeled — it shows a normal paper detail screen, not the offline error state. The GIF is the only accurate evidence of the error message.

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass (Android only)
- **Notes:** App displays "No internet connection" error, remains interactive, recovers after network restore without restart.

---

### TC005 - PDF Download and Viewing

**Requirement:** US003 - Download and View PDFs
**Priority:** High
**Platforms:** Android (executed) + iOS (designed, not executed)

#### Evidence Links:
- **Android Execution:** [evidence/android/TC005_PDFDownloadandViewing_Android_Pass.gif](evidence/android/TC005_PDFDownloadandViewing_Android_Pass.gif)
- **iOS Execution:** Not executed — `evidence/ios/TC005_PDFDownloadandViewing_iOS_Pass.gif` is a placeholder, not real evidence
- **Screenshots:**
  - PDF viewer: `evidence/screenshots/TC005_pdf_viewer.png`

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass (Android only)
- **Notes:** PDF downloads and renders correctly. Back navigation restores search results. Abstract-only papers handled gracefully (button absent/disabled).

---

### TC006 - iOS Safari PDF Integration

**Requirement:** US003 - Download and View PDFs
**Priority:** Medium
**Platform:** iOS only

#### Evidence Links:
- **iOS Execution:** **Not executed.** `evidence/ios/TC006_iOSSafariPDFIntegration_iOS_Pass.gif` is an unrelated Android recording with a "Pending macOS environment" banner, and `evidence/screenshots/TC006_safari_pdf.png` is a synthetic mockup (styled text reading "Test: PASS"). Neither is real evidence.

#### Execution Summary:
- **Test Date:** N/A — not executed
- **Tester:** N/A
- **Environment:** N/A — no iOS device/simulator available
- **Result:** **Not Executed**
- **Notes:** This test case is iOS-only and has no Android equivalent, so it was never run against any real or virtual device. The app's actual Safari/PDF handoff behavior on iOS is unverified. The closest verification this project has is `test_pdf_contract.py`, which validates the abstract-link URL pattern that iOS Safari would consume.

---

### TC007 - Android Intent Handling for PDF

**Requirement:** US003 - Download and View PDFs
**Priority:** Medium
**Platform:** Android only

#### Evidence Links:
- **Android Execution:** [evidence/android/TC007_AndroidIntentPDFHandling_Android_Pass.gif](evidence/android/TC007_AndroidIntentPDFHandling_Android_Pass.gif)
- **Screenshots:**
  - `evidence/screenshots/TC007_intent_chooser.png` is mislabeled — it shows the DOWNLOADED tab, not the Android intent chooser dialog. The GIF is the only accurate evidence of that scenario.

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass
- **Notes:** All 3 decision-table scenarios pass: direct open with default, chooser with multiple viewers, and graceful error with no viewer installed.

---

### TC008 - Bulk Downloaded Papers Management

**Requirement:** US002 - Manage Downloaded Papers
**Priority:** Low
**Platforms:** Android (executed) + iOS (designed, not executed)

#### Evidence Links:
- **Android Execution:** [evidence/android/TC008_BulkDownloadedPapersManagement_Android_Pass.gif](evidence/android/TC008_BulkDownloadedPapersManagement_Android_Pass.gif)
- **iOS Execution:** Not executed — `evidence/ios/TC008_BulkDownloadedPapersManagement_iOS_Pass.gif` is a placeholder, not real evidence

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass (Android only)
- **Notes:** Boundary values (0, 1, 3) all pass. Persistence confirmed after force-close. Sequential removal correctly returns to empty-state.

---

### TC009 - WiFi to Cellular Network Transition

**Requirement:** US004 - Network Connectivity
**Priority:** Medium
**Platforms:** Android (executed) + iOS (designed, not executed)

#### Evidence Links:
- **Android Execution:** [evidence/android/TC009_WiFitoCellularTransition_Android_Pass.gif](evidence/android/TC009_WiFitoCellularTransition_Android_Pass.gif)
- **iOS Execution:** Not executed — `evidence/ios/TC009_WiFitoCellularTransition_iOS_Pass.gif` is a placeholder, not real evidence
- **Screenshots:**
  - `evidence/screenshots/TC009_network_transition.png` is mislabeled — it shows a generic search results list, with no network-state indicator visible. The GIF is the only accurate evidence of the transition.

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass (Android only)
- **Notes:** Transitions across all 4 network states (WiFi, cellular, offline, recovery) cause no crashes. Searches and downloads work over cellular. No duplicate downloads on WiFi reconnection.

---

### TC010 - Offline Data Persistence

**Requirement:** US004 - Network Connectivity
**Priority:** High
**Platforms:** Android (executed) + iOS (designed, not executed)

#### Evidence Links:
- **Android Execution (dedicated, genuine):** [evidence/android/TC010_OfflineDataPersistence_Android_Pass.gif](evidence/android/TC010_OfflineDataPersistence_Android_Pass.gif)
- **iOS:** Not executed — and unlike other test cases, TC010 has no iOS file at all, not even a placeholder.

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass (Android only)
- **Notes:** Downloaded papers and their details are accessible offline from cache on Android. New searches while offline show error — cached result fallback not implemented (see BUG004). Full recovery on network restore without app restart. iOS was not executed for this test case.

---

### TC011 - Accessibility: TalkBack (Android)

**Requirement:** US001/US002/US003 - Cross-feature accessibility
**Priority:** Low
**Platform:** Android only

#### Evidence Links:
- **Android Execution:** [evidence/android/TC011_AccessibilityTalkBackTesting_Android_Pass.gif](evidence/android/TC011_AccessibilityTalkBackTesting_Android_Pass.gif)
- **Screenshots:**
  - `evidence/screenshots/TC011_talkback.png` is mislabeled — it shows a generic search results list with no TalkBack UI visible. The GIF is the only evidence of TalkBack behavior.

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass
- **Notes:** All WCAG 2.1 AA criteria checked pass. No "unlabelled" elements encountered. Search, results, detail view, and download/remove actions all fully operable via TalkBack gestures.

---
