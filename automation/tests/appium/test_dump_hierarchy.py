"""
Diagnostic test — dumps the Android view hierarchy after a search.

Run this on BrowserStack to capture the real element tree and identify
correct locators for search result cards. Not part of the regular suite.

Usage:
    BROWSERSTACK=true pytest automation/tests/appium/test_dump_hierarchy.py \
        -m appium -s -v

Output: /tmp/page_source_home.xml and /tmp/page_source_results.xml
These are uploaded as CI artifacts so they can be downloaded and inspected.
"""

import time
import os

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.appium
def test_dump_view_hierarchy(android_driver) -> None:
    """Dump the view hierarchy before and after a search. Always passes."""
    driver = android_driver
    out_dir = "/tmp"

    # --- Home screen: capture initial state ---
    time.sleep(4)
    home_source = driver.page_source
    _save(os.path.join(out_dir, "page_source_home.xml"), home_source)
    print("\n\n=== HOME SCREEN (first 3000 chars) ===")
    print(home_source[:3000])

    # --- Search ---
    wait = WebDriverWait(driver, 20)
    try:
        field = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "homeSearchInput")
            )
        )
    except Exception:
        field = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.EditText")
            )
        )
    field.clear()
    field.send_keys("quantum")
    driver.execute_script("mobile: performEditorAction", {"action": "search"})

    # --- Wait generously for navigation + API response ---
    time.sleep(20)

    # --- Search results screen: capture state ---
    results_source = driver.page_source
    _save(os.path.join(out_dir, "page_source_results.xml"), results_source)
    print("\n\n=== RESULTS SCREEN (first 5000 chars) ===")
    print(results_source[:5000])
    print("\n=== RESULTS SCREEN (chars 5000-8000) ===")
    print(results_source[5000:8000])

    # Summarise what clickable ViewGroups exist
    _summarise_clickable(results_source)

    assert True  # diagnostic only — never fails


def _save(path: str, content: str) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\nSaved: {path} ({len(content)} chars)")
    except Exception as e:
        print(f"\nCould not save {path}: {e}")


def _summarise_clickable(source: str) -> None:
    """Print every unique element class that has clickable='true'."""
    import re

    classes = re.findall(r'<([^\s>]+)[^>]*clickable="true"', source)
    unique = sorted(set(classes))
    print("\n=== CLICKABLE ELEMENT CLASSES ===")
    for cls in unique:
        count = classes.count(cls)
        print(f"  {cls}: {count} occurrences")
