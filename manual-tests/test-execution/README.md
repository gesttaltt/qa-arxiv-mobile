# 🎯 Real Mobile Test Execution Guide

This guide will help you execute real manual tests on the actual arXiv Papers Mobile app and collect verifiable evidence.

## 📱 Target Application
**Repository:** https://github.com/lopespm/arxiv-papers-mobile  
**Tech Stack:** React Native (Android/iOS)  
**Features:** Search arXiv papers, view details, download papers for offline access

---

## ✅ Phase 1: Environment Setup

### 1. Clone and Install the App

```bash
# Clone the target application
git clone https://github.com/lopespm/arxiv-papers-mobile.git
cd arxiv-papers-mobile

# Install dependencies
npm install

# Install iOS dependencies (if testing on iOS)
cd ios && pod install && cd ..
```

### 2. Launch on Android

```bash
# Make sure you have an Android emulator running or device connected
npx react-native run-android
```

**📋 Manual Setup Checklist:**
- [ ] Android Studio installed with emulator (Pixel 5, Android 13+ recommended)
- [ ] USB debugging enabled if using physical device
- [ ] App successfully builds and launches

### 3. Launch on iOS (if available)

```bash
# Install iOS pods
cd ios && pod install && cd ..

# Run on iOS simulator
npx react-native run-ios

# Or run on physical iPhone
npx react-native run-ios --device "iPhone 15"
```

**📋 Manual Setup Checklist:**
- [ ] Xcode installed with iOS simulator
- [ ] iPhone connected and developer mode enabled (for physical device)
- [ ] App successfully builds and launches

---

## ✅ Phase 2: Test Execution & Evidence Collection

### Recording Setup Options

Choose one of these recording methods:

#### Option A: Screen Recording Software
- **Loom** (browser/desktop): Easy sharing and automatic upload
- **OBS Studio**: Professional recording with multiple sources
- **Scrcpy**: For Android devices (computer display)

#### Option B: Device Native Recording
- **Android**: Pull down notification panel → Screen Record
- **iOS**: Control Center → Screen Recording

### Test Execution Protocol

1. **Start Recording** before beginning each test case
2. **State the test case ID** clearly at the beginning
3. **Execute all test steps** methodically
4. **Show results clearly** on screen
5. **Stop recording** and save with descriptive filename

**Filename Convention:**
```
TestCase_[ID]_[Description]_[Platform]_[Result].mp4
```

Example: `TestCase_TC001_SearchValidKeyword_Android_Pass.mp4`

---

## 📊 Test Cases for Real Execution

### Priority 1: Core Functionality

#### TC001 - Search with Valid Keyword
- **Platform:** Android + iOS
- **Focus:** Basic search functionality
- **Evidence:** Screen recording showing search flow

#### TC002 - Empty Query Handling  
- **Platform:** Android + iOS
- **Focus:** Error handling and user feedback
- **Evidence:** Screen recording showing empty search behavior

#### TC003 - Download a Paper and Remove It
- **Platform:** Android + iOS  
- **Focus:** State management and persistence
- **Evidence:** Screen recording showing download + removal from Downloaded tab

### Priority 2: Platform-Specific

#### TC006 - iOS Safari Integration
- **Platform:** iOS only
- **Focus:** PDF viewing in Safari
- **Evidence:** Screen recording showing PDF opening flow

#### TC007 - Android Intent Handling
- **Platform:** Android only
- **Focus:** Share/external app integration
- **Evidence:** Screen recording showing share functionality

---

## 📂 Evidence Organization

Create this folder structure in your test execution:

```
manual-tests/test-execution/
├── README.md (this file)
├── evidence/
│   ├── android/
│   │   ├── TC001_SearchValid_Android_Pass.mp4
│   │   ├── TC002_EmptyQuery_Android_Pass.mp4
│   │   └── TC003_DownloadAndRemovePaper_Android_Pass.mp4
│   ├── ios/
│   │   ├── TC001_SearchValid_iOS_Pass.mp4
│   │   ├── TC002_EmptyQuery_iOS_Pass.mp4
│   │   └── TC003_DownloadAndRemovePaper_iOS_Pass.mp4
│   └── screenshots/
│       ├── android_home_screen.png
│       ├── ios_search_results.png
│       └── TC003_before_download.png
├── execution-logs/
│   ├── TC001_execution_log.md
│   ├── TC002_execution_log.md
│   └── TC003_execution_log.md
└── traceability-with-evidence.md
```

---

## 🎥 Video Upload & Sharing

### Recommended Platforms:
1. **Loom** - Automatic upload, easy sharing, good for quick demos
2. **Google Drive** - Reliable storage, shareable links
3. **YouTube (Unlisted)** - Good video quality, permanent hosting

### Link Generation:
- Ensure links are **publicly accessible** or properly shared
- Test links in incognito mode to verify access
- Use descriptive titles for easy identification

---

## 📋 Execution Checklist

Before marking tests as complete, ensure:

- [ ] Video clearly shows app launch
- [ ] All test steps are visible and executed
- [ ] Results are clearly demonstrated
- [ ] Video quality is sufficient for review
- [ ] Links are working and accessible
- [ ] Test case documentation is updated with results

---

## 🔄 Next Steps After Execution

1. Update traceability matrix with evidence links
2. Create execution summary report
3. Update README.md with real test execution section
4. Document any discovered issues or improvements
5. Prepare test results for stakeholder review

---

**Remember:** The goal is to demonstrate real, verifiable testing on an actual mobile application with clear evidence of execution and results.
