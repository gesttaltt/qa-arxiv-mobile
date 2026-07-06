import os
from datetime import datetime
from pathlib import Path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

USE_BROWSERSTACK = os.environ.get("BROWSERSTACK", "false").lower() == "true"

APPIUM_SERVER = os.environ.get("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
ANDROID_APK = os.environ.get(
    "ARXIV_APK_PATH",
    "/tmp/arxiv-mobile-testing/arxiv-papers-mobile/android/app/build/outputs/apk/debug/app-debug.apk",
)
DEVICE_NAME = os.environ.get("ANDROID_DEVICE_NAME", "Android Emulator")

BS_SERVER = "https://hub-cloud.browserstack.com/wd/hub"
BS_USERNAME = os.environ.get("BROWSERSTACK_USERNAME", "")
BS_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY", "")
BS_APP_ID = os.environ.get("BROWSERSTACK_APP_ID", "")

SCREENSHOTS_DIR = Path("test-results/screenshots")


@pytest.fixture(scope="session")
def android_driver():
    options = UiAutomator2Options()

    if USE_BROWSERSTACK:
        options.set_capability(
            "bstack:options",
            {
                "userName": BS_USERNAME,
                "accessKey": BS_ACCESS_KEY,
                "projectName": "qa-arxiv-mobile",
                "buildName": os.environ.get("GITHUB_SHA", "local")[:8],
                "sessionName": "Appium Smoke Tests",
                "networkLogs": True,
            },
        )
        options.set_capability("app", BS_APP_ID)
        options.set_capability("deviceName", "Samsung Galaxy S22")
        options.set_capability("platformVersion", "12.0")
        options.set_capability("automationName", "UiAutomator2")
        options.set_capability("newCommandTimeout", 120)
        server = BS_SERVER
    else:
        options.platform_name = "Android"
        options.device_name = DEVICE_NAME
        options.app = os.path.abspath(ANDROID_APK)
        options.automation_name = "UiAutomator2"
        options.no_reset = False
        options.auto_grant_permissions = True
        options.new_command_timeout = 120
        server = APPIUM_SERVER

    driver = webdriver.Remote(server, options=options)
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
