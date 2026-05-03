"""
Appium smoke tests for the Search feature.

Covers TC001 (valid search) and TC002 (empty search) at the UI layer.
Locators use ACCESSIBILITY_ID (React Native accessibilityLabel) as primary
strategy and XPATH as fallback. Validate exact values with Appium Inspector
before the first run — see docs/APPIUM_SETUP.md.
"""

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from appium.webdriver.common.appiumby import AppiumBy


# ---------------------------------------------------------------------------
# Locators
# Verify these against the running app using Appium Inspector.
# React Native 'accessibilityLabel' maps to ACCESSIBILITY_ID on both platforms.
# ---------------------------------------------------------------------------
class _Locators:
    SEARCH_INPUT = (AppiumBy.ACCESSIBILITY_ID, "search-input")
    SEARCH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "search-button")
    # Fallback XPath when accessibilityLabel is not set on the app
    SEARCH_INPUT_XPATH = (AppiumBy.XPATH, "//android.widget.EditText")
    RESULT_ITEM = (
        AppiumBy.XPATH,
        "//android.view.ViewGroup[@clickable='true' and @focusable='true']",
    )
    RESULT_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text]")
    EMPTY_STATE_LABEL = (AppiumBy.ACCESSIBILITY_ID, "empty-results-label")
    ERROR_TOAST = (AppiumBy.XPATH, "//android.widget.Toast")


@pytest.mark.appium
class TestSearchSmoke:
    """
    TC001-Appium: Search feature UI smoke tests.
    Traceability: TC001 (valid search), TC002 (empty search).
    """

    def _wait(self, driver, timeout: int = 15) -> WebDriverWait:
        return WebDriverWait(driver, timeout)

    def _type_and_search(self, driver, keyword: str) -> None:
        wait = self._wait(driver)
        try:
            field = wait.until(EC.presence_of_element_located(_Locators.SEARCH_INPUT))
        except Exception:
            # Fallback to XPath if accessibility ID is not set in this build
            field = wait.until(
                EC.presence_of_element_located(_Locators.SEARCH_INPUT_XPATH)
            )
        field.clear()
        field.send_keys(keyword)

        # Try dedicated search button; fall back to keyboard submit
        buttons = driver.find_elements(*_Locators.SEARCH_BUTTON)
        if buttons:
            buttons[0].click()
        else:

            driver.execute_script("mobile: performEditorAction", {"action": "search"})

    # -----------------------------------------------------------------------

    def test_valid_search_displays_results(self, android_driver) -> None:
        """
        TC001-Appium: A valid keyword returns at least one paper card.

        Steps:
          1. Tap the search field
          2. Type "machine learning"
          3. Submit the search
          4. Assert at least one result card is visible
          5. Assert first card contains visible text (title/authors)
        """
        self._type_and_search(android_driver, "machine learning")

        wait = self._wait(android_driver)
        results = wait.until(EC.presence_of_all_elements_located(_Locators.RESULT_ITEM))

        assert (
            len(results) > 0
        ), "TC001-Appium FAIL: No result cards found after searching 'machine learning'"

        # Verify first result contains at least one visible text element
        first_titles = results[0].find_elements(*_Locators.RESULT_TITLE)
        assert (
            first_titles
        ), "TC001-Appium FAIL: First result card contains no visible text"

    def test_empty_search_does_not_crash(self, android_driver) -> None:
        """
        TC002-Appium: Submitting an empty search does not crash the app and
        either shows an empty-state message or keeps the results list empty.

        Steps:
          1. Clear the search field
          2. Submit without entering text
          3. Assert the app remains responsive (no crash / no unhandled exception)
          4. Assert no result cards are shown
        """
        self._type_and_search(android_driver, "")

        wait = self._wait(android_driver, timeout=5)

        # App must still be responsive — check the search field is still accessible
        try:
            field = wait.until(EC.presence_of_element_located(_Locators.SEARCH_INPUT))
        except Exception:
            field = wait.until(
                EC.presence_of_element_located(_Locators.SEARCH_INPUT_XPATH)
            )
        assert (
            field.is_displayed()
        ), "TC002-Appium FAIL: Search field not reachable after empty search — possible crash"

        results = android_driver.find_elements(*_Locators.RESULT_ITEM)
        assert (
            len(results) == 0
        ), f"TC002-Appium FAIL: Expected no results for empty search, got {len(results)}"

    @pytest.mark.parametrize(
        "keyword",
        ["quantum physics", "neural networks", "computer vision"],
    )
    def test_multiple_keywords_return_results(
        self, android_driver, keyword: str
    ) -> None:
        """
        Data-driven smoke: three common academic topics must each return results.
        Aligns with the parametrized API tests in test_search_api.py.
        """
        self._type_and_search(android_driver, keyword)

        wait = self._wait(android_driver)
        results = wait.until(EC.presence_of_all_elements_located(_Locators.RESULT_ITEM))

        assert (
            len(results) > 0
        ), f"TC001-Appium FAIL: No results for keyword '{keyword}'"
