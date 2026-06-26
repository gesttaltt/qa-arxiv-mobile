from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class FavoritesPage(BasePage):
    """Page object for the Favorites screen."""

    _FAVORITES_TAB = (AppiumBy.ACCESSIBILITY_ID, "favorites-tab")
    _FAVORITES_TAB_XPATH = (
        AppiumBy.XPATH,
        "//android.widget.TextView[@text='Favorites' or @text='Bookmarks']",
    )
    _LIST_ITEM = (
        AppiumBy.XPATH,
        "//android.view.ViewGroup[@clickable='true' and @focusable='true']",
    )
    _EMPTY_LABEL = (AppiumBy.ACCESSIBILITY_ID, "empty-favorites-label")
    _FAVORITE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "favorite-button")
    _FAVORITE_BUTTON_XPATH = (
        AppiumBy.XPATH,
        "(//android.view.ViewGroup[@clickable='true' and @focusable='true'])[1]"
        "//android.widget.ImageView",
    )

    def open(self) -> None:
        """Navigate to the Favorites tab."""
        wait = self._wait()
        try:
            tab = wait.until(EC.element_to_be_clickable(self._FAVORITES_TAB))
        except Exception:
            tab = wait.until(EC.element_to_be_clickable(self._FAVORITES_TAB_XPATH))
        tab.click()

    def get_items(self) -> list:
        """Wait for and return all items currently in the Favorites list."""
        return self._wait().until(EC.presence_of_all_elements_located(self._LIST_ITEM))

    def get_current_items(self) -> list:
        """Return currently visible favorites items without waiting."""
        return self.driver.find_elements(*self._LIST_ITEM)

    def tap_favorite_on_first_item(self) -> None:
        """Tap the favorite/star button on the first item in the Favorites list."""
        buttons = self.driver.find_elements(*self._FAVORITE_BUTTON)
        if buttons:
            buttons[0].click()
            return
        buttons = self.driver.find_elements(*self._FAVORITE_BUTTON_XPATH)
        assert buttons, "Could not locate favorite/star button on first favorites item"
        buttons[0].click()
