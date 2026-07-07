from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class SearchPage(BasePage):
    """Page object for the Search screen."""

    _SEARCH_INPUT = (AppiumBy.ACCESSIBILITY_ID, "homeSearchInput")
    _SEARCH_INPUT_XPATH = (AppiumBy.XPATH, "//android.widget.EditText")
    _RESULT_ITEM = (
        AppiumBy.XPATH,
        "//android.view.ViewGroup[@clickable='true' and @focusable='true']",
    )
    _RESULT_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text]")

    def search(self, keyword: str) -> None:
        """Type keyword into the search field and submit."""
        wait = self._wait()
        try:
            field = wait.until(EC.presence_of_element_located(self._SEARCH_INPUT))
        except Exception:
            field = wait.until(EC.presence_of_element_located(self._SEARCH_INPUT_XPATH))
        field.clear()
        field.send_keys(keyword)
        # No search button in the app — submit via keyboard action
        self.driver.execute_script("mobile: performEditorAction", {"action": "search"})

    def get_results(self) -> list:
        """Wait for and return all visible result card elements."""
        return self._wait().until(
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
