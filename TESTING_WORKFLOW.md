# 📋 Real Mobile Testing Workflow

This is your step-by-step guide to execute real manual testing on the arXiv Papers Mobile app and update this repository with verifiable evidence.

## 🎯 Overview
You'll be testing the actual React Native app from https://github.com/lopespm/arxiv-papers-mobile and documenting everything with video evidence.

---

## Phase 1: Environment Setup (15-20 minutes)

### Step 1: Run the Setup Script
```bash
# From the qa-arxiv-mobile directory
./setup-app.sh
```

### Step 2: Verify App Installation
```bash
# Navigate to the app directory (from setup script output)
cd /tmp/arxiv-mobile-testing/arxiv-papers-mobile

# Test Android build (if you have Android setup)
npx react-native run-android

# OR Test iOS build (if you have macOS/iOS setup)
npx react-native run-ios
```

### Step 3: Choose Your Recording Method
**Option A: Loom (Recommended)**
- Install Loom: https://loom.com
- Test screen recording functionality

**Option B: OBS Studio**
- Install OBS Studio for professional recording
- Configure screen capture

**Option C: Device Native**
- Android: Use built-in screen recording
- iOS: Use Control Center screen recording

---

## Phase 2: Test Execution (45-60 minutes)

### Priority Test Cases to Execute:

#### TC001: Search with Valid Keyword
1. **Start Recording** - State "Executing TC001 - Search Valid Keyword"
2. Launch the arXiv app
3. Tap search field
4. Type "quantum"
5. Execute search
6. Show results clearly
7. **Stop Recording** - Save as `TC001_SearchValid_[Platform]_[Result].mp4`

#### TC002: Empty Query Handling
1. **Start Recording** - State "Executing TC002 - Empty Query Handling"
2. Launch app (or continue from previous test)
3. Clear/ensure empty search field
4. Attempt to search with empty field
5. Document error handling/validation
6. **Stop Recording** - Save as `TC002_EmptyQuery_[Platform]_[Result].mp4`

#### TC003: Toggle Favorite Functionality
1. **Start Recording** - State "Executing TC003 - Toggle Favorite"
2. From search results, find favorite button/icon
3. Toggle favorite ON (show visual change)
4. Navigate away and back to verify persistence
5. Toggle favorite OFF
6. **Stop Recording** - Save as `TC003_ToggleFavorite_[Platform]_[Result].mp4`

### Execution Notes:
- Test on **both Android AND iOS** if possible (or document which platform you tested)
- **Narrate your actions** during recording for clarity
- **Show any errors or unexpected behavior** clearly
- **Capture key screenshots** during testing

---

## Phase 3: Documentation Update (30-45 minutes)

### Step 1: Upload Videos
1. Upload videos to Loom/Google Drive/YouTube (unlisted)
2. Ensure videos are publicly accessible or properly shared
3. Test links in incognito mode to verify access

### Step 2: Update Execution Logs
For each test case, update the corresponding log:

```bash
# Edit these files with your results:
manual-tests/test-execution/execution-logs/TC001_execution_log.md
manual-tests/test-execution/execution-logs/TC002_execution_log.md
manual-tests/test-execution/execution-logs/TC003_execution_log.md
```

**Fill in:**
- Test date and environment details
- Mark Pass/Fail for each step
- Add your video links
- Document any issues found
- Note platform differences

### Step 3: Update Traceability Matrix
Edit: `manual-tests/test-execution/traceability-with-evidence.md`

**Replace placeholders with:**
- Your actual video links
- Test execution dates
- Results (Pass/Fail)
- Your name as tester
- Any issues discovered

### Step 4: Complete Execution Summary
Edit: `manual-tests/test-execution/execution-summary.md`

**Update:**
- Platform coverage completed
- Overall test results
- Key findings and issues
- Quality assessment ratings
- Evidence verification section

---

## Phase 4: Final Repository Update (15 minutes)

### Step 1: Update Main README
The README already has a section for real testing evidence. Update:
- Test execution status (✅ Completed)
- Links to your evidence files
- Any additional notes about your testing

### Step 2: Commit Your Changes
```bash
git add .
git commit -m "Add real mobile test execution evidence for arXiv Papers app

- Executed TC001, TC002, TC003 on [Android/iOS/Both]
- Added video evidence with links to execution documentation
- Updated traceability matrix with verifiable test results
- Completed execution logs with detailed findings"

git push origin main
```

---

## 🎯 Success Criteria

Your testing is complete when:
- [ ] App successfully built and tested on at least one platform
- [ ] All 3 priority test cases executed with video evidence
- [ ] Videos uploaded and links are working
- [ ] Execution logs completed with Pass/Fail results
- [ ] Traceability matrix updated with evidence links
- [ ] Execution summary completed
- [ ] All changes committed to repository

---

## 🆘 Troubleshooting

### App Won't Build:
- Check Node.js version (should be 14+)
- Try `npm install` again
- Check Android SDK/Xcode setup
- Look for specific error messages in terminal

### Recording Issues:
- Test recording software before starting
- Ensure sufficient disk space
- Use lower resolution if file sizes too large

### App Crashes:
- Document the crash in your execution log
- Note what caused it
- Try to reproduce the crash
- This is valuable test evidence!

---

## 📞 Ready to Start?

1. **Time needed:** 2-3 hours total
2. **Prerequisites:** Android Studio OR Xcode + recording software
3. **Output:** Professional QA repository with real testing evidence

**Start with:** `./setup-app.sh`

**Questions during testing?** Document everything - even problems are valuable QA evidence!

---

**Good luck! This will create a powerful demonstration of real mobile QA work.** 🚀
