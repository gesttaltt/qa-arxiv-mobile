import os
from datetime import datetime
from pathlib import Path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

APPIUM_SERVER = os.environ.get("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
ANDROID_APK = os.environ.get(
    "ARXIV_APK_PATH",
    "/tmp/arxiv-mobile-testing/arxiv-papers-mobile/android/app/build/outputs/apk/debug/app-debug.apk",
)
DEVICE_NAME = os.environ.get("ANDROID_DEVICE_NAME", "Android Emulator")
SCREENSHOTS_DIR = Path("test-results/screenshots")


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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("android_driver")
        if driver is None:
            return

        SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = (
            SCREENSHOTS_DIR
            / f"{item.nodeid.replace('/', '_').replace('::', '__')}_{timestamp}.png"
        )
        driver.save_screenshot(str(filename))
        report.sections.append(("Screenshot", str(filename)))
