# Evidence Folder

This folder contains test execution evidence for the arXiv Papers Mobile app.

**Android evidence is real** — genuine screen recordings from a Pixel 6 emulator (API 33),
captured with `adb screenrecord`.

**iOS evidence is not real.** No macOS/Xcode/iOS Simulator was available for this project,
so no iOS execution ever took place. Every file under `ios/` is either:
- the Android recording with a "Pending macOS environment" banner overlaid, or
- (for `TC006_safari_pdf.png`) a synthetic mockup image styled as evidence, not a real capture.

This is disclosed here, in `docs/MARKET_GAP_ANALYSIS.md` §3.5, and in each affected
execution log, so the limitation is visible wherever the evidence is referenced.

## Current Contents

### Android GIF Recordings (10 files) — genuine
| File | Test Case | Description |
|------|-----------|-------------|
| TC001_SearchwithValidKeyword_Android_Pass.gif | TC001 | Search with valid keyword |
| TC002_SearchwithEmptyQuery_Android_Pass.gif | TC002 | Search with empty input |
| TC003_DownloadAndRemovePaper_Android_Pass.gif | TC003 | Download a paper and remove it from Downloaded |
| TC004_SearchOfflineBehavior_Android_Pass.gif | TC004 | Search offline behavior |
| TC005_PDFDownloadandViewing_Android_Pass.gif | TC005 | PDF download and viewing |
| TC007_AndroidIntentPDFHandling_Android_Pass.gif | TC007 | Android intent PDF handling |
| TC008_BulkDownloadedPapersManagement_Android_Pass.gif | TC008 | Bulk downloaded papers management |
| TC009_WiFitoCellularTransition_Android_Pass.gif | TC009 | WiFi to cellular transition |
| TC010_OfflineDataPersistence_Android_Pass.gif | TC010 | Offline data persistence (dedicated recording) |
| TC011_AccessibilityTalkBackTesting_Android_Pass.gif | TC011 | Accessibility TalkBack testing |

### iOS GIF Recordings (8 files) — placeholders, not real iOS captures
| File | Test Case | Actual content |
|------|-----------|-------------|
| TC001_SearchwithValidKeyword_iOS_Pass.gif | TC001 | Android recording, "Pending macOS environment" banner |
| TC002_SearchwithEmptyQuery_iOS_Pass.gif | TC002 | Android recording, "Pending macOS environment" banner |
| TC003_DownloadAndRemovePaper_iOS_Pass.gif | TC003 | Android recording, "Pending macOS environment" banner |
| TC004_SearchOfflineBehavior_iOS_Pass.gif | TC004 | Android recording, "Pending macOS environment" banner |
| TC005_PDFDownloadandViewing_iOS_Pass.gif | TC005 | Android recording, "Pending macOS environment" banner |
| TC006_iOSSafariPDFIntegration_iOS_Pass.gif | TC006 | Android recording, "Pending macOS environment" banner (unrelated to Safari/PDF — TC006 is iOS-only and was never executed) |
| TC008_BulkDownloadedPapersManagement_iOS_Pass.gif | TC008 | Android recording, "Pending macOS environment" banner |
| TC009_WiFitoCellularTransition_iOS_Pass.gif | TC009 | Android recording, "Pending macOS environment" banner |

> TC010 and TC011 have no iOS file at all, not even a placeholder — TC011 is Android-only
> by design (TalkBack has no iOS equivalent in scope); TC010's iOS placeholder was never created.

### Screenshots (11 files) — mixed: some genuine, some mislabeled or synthetic
Evidence directory: `screenshots/`

| File | Actual content | Genuine? |
|------|---------|----------|
| TC001_android_search_results.png | Search results for "quantum" on Android | Yes |
| TC001_ios_search_results.png | Synthetic mockup (styled text, fabricated "Favorited" labels from an earlier draft of the app concept) | **No — synthetic** |
| TC002_android_empty_search.png | Empty search validation on Android | Yes |
| TC003_before_download.png | Paper detail before download, Android | Yes |
| TC003_after_download.png | Downloaded tab after download, Android | Yes |
| TC004_offline_error.png | Generic paper detail screen — does **not** show the offline error state | **No — mislabeled** |
| TC005_pdf_viewer.png | PDF viewer in action, Android | Yes |
| TC006_safari_pdf.png | Synthetic mockup (styled text reading "Test: PASS") — TC006 was never executed | **No — synthetic** |
| TC007_intent_chooser.png | DOWNLOADED tab — does **not** show the Android intent chooser dialog | **No — mislabeled** |
| TC009_network_transition.png | Generic search results list — does **not** show a network-state indicator | **No — mislabeled** |
| TC011_talkback.png | Generic search results list — does **not** show TalkBack UI | **No — mislabeled** |

Only 5 of the 11 screenshots genuinely show what their filename claims. The GIF recordings
are the authoritative Android evidence; screenshots marked "mislabeled" or "synthetic" above
should not be treated as proof of the specific state they're named after.

### Suite Summary
| File | Description |
|------|-------------|
| suite_summary.gif | Animated overview of all 11 test cases and results |

## Evidence Quality
- **Format:** Animated GIF (test walkthroughs), PNG (screenshots)
- **Android:** 10/11 test cases have genuine GIF evidence (TC006 is iOS-only, so has no Android
  evidence); 5/11 have an accurate screenshot as well.
- **iOS:** 0/11 test cases were executed on a real or virtual iOS device. 8 test cases have a
  placeholder GIF; TC006, TC010, and TC011 do not.
- **Total evidence files:** 30 (10 genuine Android GIFs + 8 iOS placeholder GIFs + 11 screenshots,
  5 of which are genuine + 1 suite summary)
