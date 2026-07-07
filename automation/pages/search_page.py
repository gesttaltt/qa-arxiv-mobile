from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

# Android keycode 66 = Enter / search action key — more reliable than
# performEditorAction on BrowserStack (confirmed from page_source analysis).
_KEYCODE_ENTER = 66


class SearchPage(BasePage):
    """Page object for the Search screen."""

    _SEARCH_INPUT = (AppiumBy.ACCESSIBILITY_ID, "homeSearchInput")
    _SEARCH_INPUT_XPATH = (AppiumBy.XPATH, "//android.widget.EditText")

    # Result cards confirmed via page_source on BrowserStack (Samsung S22 / Android 12).
    # Structure: ScrollView > ViewGroup (FlatList) > ViewGroup (Card) > ViewGroup (CardItem) > TextView
    # TouchableNativeFeedback does NOT set clickable=true on Android 12 — locate by structure.
    _RESULT_ITEM = (
        AppiumBy.XPATH,
        "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[.//android.widget.TextView]",
    )
    _RESULT_TITLE = (AppiumBy.XPATH, ".//android.widget.TextView")

    def search(self, keyword: str) -> None:
        """Tap the search field, type keyword, and submit via Enter keycode."""
        wait = self._wait()
        try:
            field = wait.until(EC.element_to_be_clickable(self._SEARCH_INPUT))
        except Exception:
            field = wait.until(EC.element_to_be_clickable(self._SEARCH_INPUT_XPATH))
        field.click()
        field.clear()
        field.send_keys(keyword)
        # press_keycode(66) fires the native Android Enter/Search action and
        # reliably triggers onSubmitEditing in React Native on BrowserStack.
        self.driver.press_keycode(_KEYCODE_ENTER)

    def get_results(self) -> list:
        """Wait for and return all visible result card elements."""
        return self._wait(30).until(
            EC.presence_of_all_elements_located(self._RESULT_ITEM)
        )

    def get_current_results(self) -> list:
        """Return currently visible result items without waiting."""
        return self.driver.find_elements(*self._RESULT_ITEM)

    def get_first_result_titles(self) -> list:
        """Return visible text elements inside the first result card."""
        results = self.get_results()
        return list(results[0].find_elements(*self._RESULT_TITLE))

    def is_search_field_displayed(self, timeout: int = 5) -> bool:
        """Return True if the search field is still accessible (app not crashed)."""
        wait = self._wait(timeout)
        try:
            field = wait.until(EC.presence_of_element_located(self._SEARCH_INPUT))
        except Exception:
            field = wait.until(EC.presence_of_element_located(self._SEARCH_INPUT_XPATH))
        return field.is_displayed()
