from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class DownloadedPage(BasePage):
    """Page object for the DOWNLOADED tab on the Home screen."""

    _DOWNLOADED_TAB = (
        AppiumBy.XPATH,
        "//android.widget.TextView[@text='DOWNLOADED']",
    )
    _LIST_ITEM = (AppiumBy.ACCESSIBILITY_ID, "downloadedArticle")
    _EMPTY_LABEL = (
        AppiumBy.XPATH,
        "//android.widget.TextView[@text='Your downloaded articles will appear here']",
    )

    def open(self) -> None:
        """Tap the DOWNLOADED tab to navigate to it."""
        tab = self._wait().until(EC.element_to_be_clickable(self._DOWNLOADED_TAB))
        tab.click()

    def get_items(self) -> list:
        """Wait for and return all downloaded article list items."""
        return self._wait().until(
            EC.presence_of_all_elements_located(self._LIST_ITEM)
        )

    def get_current_items(self) -> list:
        """Return currently visible downloaded items without waiting."""
        return self.driver.find_elements(*self._LIST_ITEM)

    def is_empty_label_displayed(self, timeout: int = 5) -> bool:
        """Return True if the empty-state label is visible (no downloads yet)."""
        try:
            label = self._wait(timeout).until(
                EC.presence_of_element_located(self._EMPTY_LABEL)
            )
            return label.is_displayed()
        except Exception:
            return False
