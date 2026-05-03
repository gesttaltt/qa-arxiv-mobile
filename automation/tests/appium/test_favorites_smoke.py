"""
Appium smoke tests for the Favorites feature.

Covers TC003 (toggle favorite) at the UI layer.
Locators — validate with Appium Inspector before first run (docs/APPIUM_SETUP.md).
"""

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from appium.webdriver.common.appiumby import AppiumBy


class _Locators:
    SEARCH_INPUT = (AppiumBy.ACCESSIBILITY_ID, "search-input")
    SEARCH_INPUT_XPATH = (AppiumBy.XPATH, "//android.widget.EditText")
    SEARCH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "search-button")
    RESULT_ITEM = (
        AppiumBy.XPATH,
        "//android.view.ViewGroup[@clickable='true' and @focusable='true']",
    )
    # Favorite/star button — typically inside the first result card
    FAVORITE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "favorite-button")
    FAVORITE_BUTTON_XPATH = (
        AppiumBy.XPATH,
        "(//android.view.ViewGroup[@clickable='true' and @focusable='true'])[1]"
        "//android.widget.ImageView",
    )
    # Bottom tab or top navigation item for the Favorites screen
    FAVORITES_TAB = (AppiumBy.ACCESSIBILITY_ID, "favorites-tab")
    FAVORITES_TAB_XPATH = (
        AppiumBy.XPATH,
        "//android.widget.TextView[@text='Favorites' or @text='Bookmarks']",
    )
    FAVORITES_LIST_ITEM = (
        AppiumBy.XPATH,
        "//android.view.ViewGroup[@clickable='true' and @focusable='true']",
    )
    EMPTY_FAVORITES_LABEL = (AppiumBy.ACCESSIBILITY_ID, "empty-favorites-label")


@pytest.mark.appium
class TestFavoritesSmoke:
    """
    TC003-Appium: Favorites feature UI smoke tests.
    Traceability: TC003 (toggle favorite).
    """

    def _wait(self, driver, timeout: int = 15) -> WebDriverWait:
        return WebDriverWait(driver, timeout)

    def _search_for(self, driver, keyword: str) -> None:
        wait = self._wait(driver)
        try:
            field = wait.until(EC.presence_of_element_located(_Locators.SEARCH_INPUT))
        except Exception:
            field = wait.until(
                EC.presence_of_element_located(_Locators.SEARCH_INPUT_XPATH)
            )
        field.clear()
        field.send_keys(keyword)
        buttons = driver.find_elements(*_Locators.SEARCH_BUTTON)
        if buttons:
            buttons[0].click()
        else:
            driver.execute_script("mobile: performEditorAction", {"action": "search"})

    def _open_favorites_tab(self, driver) -> None:
        wait = self._wait(driver)
        try:
            tab = wait.until(EC.element_to_be_clickable(_Locators.FAVORITES_TAB))
        except Exception:
            tab = wait.until(EC.element_to_be_clickable(_Locators.FAVORITES_TAB_XPATH))
        tab.click()

    def _tap_favorite_button_on_first_result(self, driver) -> None:
        wait = self._wait(driver)
        wait.until(EC.presence_of_all_elements_located(_Locators.RESULT_ITEM))
        try:
            btn = driver.find_elements(*_Locators.FAVORITE_BUTTON)
            if btn:
                btn[0].click()
                return
        except Exception:
            pass
        # Fallback: tap the star icon inside the first result card
        btn = driver.find_elements(*_Locators.FAVORITE_BUTTON_XPATH)
        assert btn, "Could not locate favorite/star button on first result"
        btn[0].click()

    # -----------------------------------------------------------------------

    def test_add_paper_to_favorites(self, android_driver) -> None:
        """
        TC003-Appium (part 1): Marking a paper as favorite makes it appear in
        the Favorites tab.

        Steps:
          1. Search for "deep learning"
          2. Tap the favorite/star button on the first result
          3. Navigate to the Favorites tab
          4. Assert the list contains at least one item
        """
        self._search_for(android_driver, "deep learning")

        wait = self._wait(android_driver)
        wait.until(EC.presence_of_all_elements_located(_Locators.RESULT_ITEM))

        self._tap_favorite_button_on_first_result(android_driver)
        self._open_favorites_tab(android_driver)

        favorites = wait.until(
            EC.presence_of_all_elements_located(_Locators.FAVORITES_LIST_ITEM)
        )
        assert (
            len(favorites) > 0
        ), "TC003-Appium FAIL: Favorites tab is empty after marking a paper"

    def test_remove_paper_from_favorites(self, android_driver) -> None:
        """
        TC003-Appium (part 2): Unmarking a previously favorited paper removes it.

        Precondition: test_add_paper_to_favorites has run (session-scoped driver).

        Steps:
          1. While on Favorites tab, tap the star on the first item (unmark)
          2. Assert the item is no longer listed or the list is empty
        """
        wait = self._wait(android_driver)

        # Ensure we are on the Favorites tab
        self._open_favorites_tab(android_driver)
        favorites_before = wait.until(
            EC.presence_of_all_elements_located(_Locators.FAVORITES_LIST_ITEM)
        )
        count_before = len(favorites_before)
        assert count_before > 0, (
            "TC003-Appium FAIL: Favorites list is already empty — "
            "run test_add_paper_to_favorites first"
        )

        # Tap the star on the first favorite to remove it
        self._tap_favorite_button_on_first_result(android_driver)

        # Give the UI a moment to update
        wait = self._wait(android_driver, timeout=5)
        try:
            favorites_after = wait.until(
                EC.presence_of_all_elements_located(_Locators.FAVORITES_LIST_ITEM)
            )
            count_after = len(favorites_after)
        except Exception:
            count_after = 0  # List became empty — that's a valid outcome

        assert count_after < count_before, (
            f"TC003-Appium FAIL: Favorites count unchanged after removing "
            f"({count_before} before, {count_after} after)"
        )

    def test_favorites_tab_is_empty_on_fresh_install(self, android_driver) -> None:
        """
        Sanity check: after app reset (no_reset=False in conftest), the
        Favorites tab should start empty before any interaction.

        Note: This test is only meaningful when run first in a clean session.
        Mark with @pytest.mark.order(1) if test ordering plugin is available.
        """
        # Re-open the app in a clean state
        android_driver.reset()

        self._open_favorites_tab(android_driver)

        wait = self._wait(android_driver, timeout=5)
        items = android_driver.find_elements(*_Locators.FAVORITES_LIST_ITEM)

        assert len(items) == 0, (
            f"TC003-Appium FAIL: Expected empty favorites on fresh install, "
            f"found {len(items)} item(s)"
        )
