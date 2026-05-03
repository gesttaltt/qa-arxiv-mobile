import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

APPIUM_SERVER = os.environ.get("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
ANDROID_APK = os.environ.get(
    "ARXIV_APK_PATH",
    "/tmp/arxiv-mobile-testing/arxiv-papers-mobile/android/app/build/outputs/apk/debug/app-debug.apk",
)
DEVICE_NAME = os.environ.get("ANDROID_DEVICE_NAME", "Android Emulator")


@pytest.fixture(scope="session")
def android_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = DEVICE_NAME
    options.app = os.path.abspath(ANDROID_APK)
    options.automation_name = "UiAutomator2"
    options.no_reset = False
    options.auto_grant_permissions = True
    options.new_command_timeout = 120

    driver = webdriver.Remote(APPIUM_SERVER, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
