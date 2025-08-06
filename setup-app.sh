#!/bin/bash

# arXiv Mobile App Setup Script
# This script helps set up the arXiv Papers Mobile app for manual testing

echo "arXiv Papers Mobile App Setup for Manual Testing"
echo "================================================"

# Create a temporary directory for the app
TEMP_DIR="/tmp/arxiv-mobile-testing"
APP_DIR="$TEMP_DIR/arxiv-papers-mobile"

echo ""
echo "Setting up test environment..."

# Create temp directory if it doesn't exist
if [ ! -d "$TEMP_DIR" ]; then
    mkdir -p "$TEMP_DIR"
    echo "Created temporary directory: $TEMP_DIR"
fi

cd "$TEMP_DIR"

# Clone the repository if not already present
if [ ! -d "$APP_DIR" ]; then
    echo ""
    echo "Cloning arXiv Papers Mobile repository..."
    git clone https://github.com/lopespm/arxiv-papers-mobile.git
    if [ $? -eq 0 ]; then
        echo "Repository cloned successfully"
    else
        echo "ERROR: Failed to clone repository"
        exit 1
    fi
else
    echo "Repository already exists, updating..."
    cd "$APP_DIR"
    git pull origin main
fi

cd "$APP_DIR"

echo ""
echo "Installing dependencies..."

# Check if Node.js is available
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed. Please install Node.js first."
    echo "   Visit: https://nodejs.org/"
    exit 1
fi

# Check if npm is available
if ! command -v npm &> /dev/null; then
    echo "ERROR: npm is not installed. Please install npm first."
    exit 1
fi

# Install npm dependencies
echo "Installing npm packages..."
npm install
if [ $? -eq 0 ]; then
    echo "npm dependencies installed"
else
    echo "ERROR: Failed to install npm dependencies"
    exit 1
fi

# Check for iOS setup if on macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo ""
    echo "iOS Setup (macOS detected)..."
    
    # Check if CocoaPods is installed
    if command -v pod &> /dev/null; then
        echo "Installing iOS dependencies..."
        cd ios
        pod install
        if [ $? -eq 0 ]; then
            echo "iOS pods installed successfully"
        else
            echo "WARNING: Failed to install iOS pods - you may need to run 'pod install' manually"
        fi
        cd ..
    else
        echo "WARNING: CocoaPods not found. Install with: sudo gem install cocoapods"
    fi
fi

echo ""
echo "Android Setup Instructions:"
echo "1. Ensure Android Studio is installed with SDK"
echo "2. Set up Android emulator or connect physical device"
echo "3. Enable USB debugging on physical device"
echo "4. Verify adb connection with: adb devices"

echo ""
echo "Ready to Test!"
echo "=============="
echo "App location: $APP_DIR"
echo ""
echo "To run on Android:"
echo "  cd $APP_DIR"
echo "  npx react-native run-android"
echo ""
if [[ "$OSTYPE" == "darwin"* ]]; then
echo "To run on iOS:"
echo "  cd $APP_DIR"
echo "  npx react-native run-ios"
echo ""
fi
echo "Don't forget to:"
echo "  1. Start screen recording before testing"
echo "  2. Execute test cases from manual-tests/test-execution/"
echo "  3. Update execution logs with results"
echo "  4. Upload videos and update traceability matrix"
echo ""
echo "Test execution guide: manual-tests/test-execution/README.md"
echo ""
echo "Happy Testing!"
