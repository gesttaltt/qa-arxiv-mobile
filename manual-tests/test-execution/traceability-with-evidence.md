# 📊 Test Traceability Matrix with Evidence Links

This document provides complete traceability from requirements to test execution with verifiable evidence.

## 🎯 Real Execution Status Overview

| Test Case ID | Description | Android Status | iOS Status | Evidence Collected |
|--------------|-------------|----------------|------------|-------------------|
| TC001 | Search with valid keyword | ✅ Passed | ✅ Passed | GIF + Screenshots |
| TC002 | Search with empty input | ✅ Passed | ✅ Passed | GIF + Screenshots |
| TC003 | Download a paper and remove it from Downloaded | ✅ Passed | ✅ Passed | GIF + Before/After screenshots |
| TC004 | Search offline behavior | ✅ Passed | ✅ Passed | GIF + Screenshot |
| TC005 | PDF download and viewing | ✅ Passed | ✅ Passed | GIF + Screenshot |
| TC006 | iOS Safari PDF integration | N/A | ✅ Passed | GIF + Screenshot |
| TC007 | Android intent handling | ✅ Passed | N/A | GIF + Screenshot |
| TC008 | Bulk downloaded papers management | ✅ Passed | ✅ Passed | GIF |
| TC009 | WiFi to cellular transition | ✅ Passed | ✅ Passed | GIF + Screenshot |
| TC010 | Offline data persistence | ✅ Passed | ✅ Passed | Dedicated Android GIF; iOS shares TC004 evidence |
| TC011 | Accessibility TalkBack | ✅ Passed | N/A | GIF + Screenshot |

---

## 📱 Test Execution Evidence

### TC001 - Search with Valid Keyword

**Requirement:** US001 - Search for Academic Papers  
**Priority:** High  
**Platforms:** Android + iOS

#### Evidence Links:
- **Android Execution:** [evidence/android/TC001_SearchwithValidKeyword_Android_Pass.gif](evidence/android/TC001_SearchwithValidKeyword_Android_Pass.gif)
- **iOS Execution:** [evidence/ios/TC001_SearchwithValidKeyword_iOS_Pass.gif](evidence/ios/TC001_SearchwithValidKeyword_iOS_Pass.gif)
- **Screenshots:**
  - Android search results: `evidence/screenshots/TC001_android_search_results.png`
  - iOS search results: `evidence/screenshots/TC001_ios_search_results.png`

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass
- **Notes:** Search returns relevant results; cards display title, authors, and date. Verified on Android and iOS.

---

### TC002 - Search with Empty Input

**Requirement:** US001 - Search for Academic Papers  
**Priority:** High  
**Platforms:** Android + iOS

#### Evidence Links:
- **Android Execution:** [evidence/android/TC002_SearchwithEmptyQuery_Android_Pass.gif](evidence/android/TC002_SearchwithEmptyQuery_Android_Pass.gif)
- **iOS Execution:** [evidence/ios/TC002_SearchwithEmptyQuery_iOS_Pass.gif](evidence/ios/TC002_SearchwithEmptyQuery_iOS_Pass.gif)
- **Screenshots:**
  - Android empty search: `evidence/screenshots/TC002_android_empty_search.png`
  - iOS empty search: `evidence/screenshots/TC002_ios_empty_search.png`

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass
- **Notes:** Validation message shown when search attempted with empty field. No app crash observed. API layer also validated.

---

### TC003 - Download a Paper and Remove It from Downloaded

**Requirement:** US002 - Manage Downloaded Papers  
**Priority:** High  
**Platforms:** Android + iOS

#### Evidence Links:
- **Android Execution:** [evidence/android/TC003_DownloadAndRemovePaper_Android_Pass.gif](evidence/android/TC003_DownloadAndRemovePaper_Android_Pass.gif)
- **iOS Execution:** [evidence/ios/TC003_DownloadAndRemovePaper_iOS_Pass.gif](evidence/ios/TC003_DownloadAndRemovePaper_iOS_Pass.gif)
- **Screenshots:**
  - Before download: `evidence/screenshots/TC003_before_download.png`
  - After download: `evidence/screenshots/TC003_after_download.png`

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass
- **Notes:** Download and removal work correctly. Item appears in the DOWNLOADED tab after download and disappears after tapping the trash icon.

### TC004 - Search Offline Behavior

**Requirement:** US001 - Search for Academic Papers
**Priority:** Medium
**Platforms:** Android + iOS

#### Evidence Links:
- **Android Execution:** [evidence/android/TC004_SearchOfflineBehavior_Android_Pass.gif](evidence/android/TC004_SearchOfflineBehavior_Android_Pass.gif)
- **iOS Execution:** [evidence/ios/TC004_SearchOfflineBehavior_iOS_Pass.gif](evidence/ios/TC004_SearchOfflineBehavior_iOS_Pass.gif)
- **Screenshots:**
  - Offline error state: `evidence/screenshots/TC004_offline_error.png`

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass
- **Notes:** App displays "No internet connection" error, remains interactive, recovers after network restore without restart.

---

### TC005 - PDF Download and Viewing

**Requirement:** US003 - Download and View PDFs
**Priority:** High
**Platforms:** Android + iOS

#### Evidence Links:
- **Android Execution:** [evidence/android/TC005_PDFDownloadandViewing_Android_Pass.gif](evidence/android/TC005_PDFDownloadandViewing_Android_Pass.gif)
- **iOS Execution:** [evidence/ios/TC005_PDFDownloadandViewing_iOS_Pass.gif](evidence/ios/TC005_PDFDownloadandViewing_iOS_Pass.gif)
- **Screenshots:**
  - PDF viewer: `evidence/screenshots/TC005_pdf_viewer.png`

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass
- **Notes:** PDF downloads and renders correctly. Back navigation restores search results. Abstract-only papers handled gracefully (button absent/disabled).

---

### TC006 - iOS Safari PDF Integration

**Requirement:** US003 - Download and View PDFs
**Priority:** Medium
**Platform:** iOS only

#### Evidence Links:
- **iOS Execution:** [evidence/ios/TC006_iOSSafariPDFIntegration_iOS_Pass.gif](evidence/ios/TC006_iOSSafariPDFIntegration_iOS_Pass.gif)
- **Screenshots:**
  - Safari PDF view: `evidence/screenshots/TC006_safari_pdf.png`

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass
- **Notes:** Safari opens correct arXiv PDF URL. App resumes on same detail screen with full state preservation. No crash on return.

---

### TC007 - Android Intent Handling for PDF

**Requirement:** US003 - Download and View PDFs
**Priority:** Medium
**Platform:** Android only

#### Evidence Links:
- **Android Execution:** [evidence/android/TC007_AndroidIntentPDFHandling_Android_Pass.gif](evidence/android/TC007_AndroidIntentPDFHandling_Android_Pass.gif)
- **Screenshots:**
  - Intent chooser: `evidence/screenshots/TC007_intent_chooser.png`

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
**Platforms:** Android + iOS

#### Evidence Links:
- **Android Execution:** [evidence/android/TC008_BulkDownloadedPapersManagement_Android_Pass.gif](evidence/android/TC008_BulkDownloadedPapersManagement_Android_Pass.gif)
- **iOS Execution:** [evidence/ios/TC008_BulkDownloadedPapersManagement_iOS_Pass.gif](evidence/ios/TC008_BulkDownloadedPapersManagement_iOS_Pass.gif)

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass
- **Notes:** Boundary values (0, 1, 3) all pass. Persistence confirmed after force-close. Sequential removal correctly returns to empty-state.

---

### TC009 - WiFi to Cellular Network Transition

**Requirement:** US004 - Network Connectivity
**Priority:** Medium
**Platforms:** Android + iOS

#### Evidence Links:
- **Android Execution:** [evidence/android/TC009_WiFitoCellularTransition_Android_Pass.gif](evidence/android/TC009_WiFitoCellularTransition_Android_Pass.gif)
- **iOS Execution:** [evidence/ios/TC009_WiFitoCellularTransition_iOS_Pass.gif](evidence/ios/TC009_WiFitoCellularTransition_iOS_Pass.gif)
- **Screenshots:**
  - Network transition state: `evidence/screenshots/TC009_network_transition.png`

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass
- **Notes:** Transitions across all 4 network states (WiFi, cellular, offline, recovery) cause no crashes. Searches and downloads work over cellular. No duplicate downloads on WiFi reconnection.

---

### TC010 - Offline Data Persistence

**Requirement:** US004 - Network Connectivity
**Priority:** High
**Platforms:** Android + iOS

#### Evidence Links:
- **Android Execution (dedicated):** [evidence/android/TC010_OfflineDataPersistence_Android_Pass.gif](evidence/android/TC010_OfflineDataPersistence_Android_Pass.gif)
- **iOS (shared offline-state evidence):** [evidence/ios/TC004_SearchOfflineBehavior_iOS_Pass.gif](evidence/ios/TC004_SearchOfflineBehavior_iOS_Pass.gif) — dedicated iOS recording still pending

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass
- **Notes:** Downloaded papers and their details are accessible offline from cache (verified both platforms). New searches while offline show error — cached result fallback not implemented (see BUG004). Full recovery on network restore without app restart. Dedicated GIF evidence captured for Android; iOS still pending.

---

### TC011 - Accessibility: TalkBack (Android)

**Requirement:** US001/US002/US003 - Cross-feature accessibility
**Priority:** Low
**Platform:** Android only

#### Evidence Links:
- **Android Execution:** [evidence/android/TC011_AccessibilityTalkBackTesting_Android_Pass.gif](evidence/android/TC011_AccessibilityTalkBackTesting_Android_Pass.gif)
- **Screenshots:**
  - TalkBack active: `evidence/screenshots/TC011_talkback.png`

#### Execution Summary:
- **Test Date:** 2026-05-21
- **Tester:** QA Team
- **Environment:** arXiv Papers Mobile (React Native)
- **Result:** Pass
- **Notes:** All WCAG 2.1 AA criteria checked pass. No "unlabelled" elements encountered. Search, results, detail view, and download/remove actions all fully operable via TalkBack gestures.

---
