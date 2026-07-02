"""
Unit tests for Page Object Model classes — mock-based, no device required.

Validates that each POM method calls the correct Appium/Selenium APIs and
handles the accessibility-ID → XPath fallback paths correctly. The Appium
driver is replaced with MagicMock so these tests run in CI without a
connected Android device or emulator.
"""

from unittest.mock import MagicMock

from ..pages.base_page import BasePage
from ..pages.favorites_page import FavoritesPage
from ..pages.search_page import SearchPage


def _search_page() -> tuple[SearchPage, MagicMock, MagicMock]:
    """Return (page, driver mock, wait mock) with _wait pre-stubbed."""
    driver = MagicMock()
    page = SearchPage(driver)
    mock_wait = MagicMock()
    page._wait = MagicMock(return_value=mock_wait)  # type: ignore[method-assign]
    return page, driver, mock_wait


def _favorites_page() -> tuple[FavoritesPage, MagicMock, MagicMock]:
    """Return (page, driver mock, wait mock) with _wait pre-stubbed."""
    driver = MagicMock()
    page = FavoritesPage(driver)
    mock_wait = MagicMock()
    page._wait = MagicMock(return_value=mock_wait)  # type: ignore[method-assign]
    return page, driver, mock_wait


class TestBasePage:
    def test_init_stores_driver(self) -> None:
        driver = MagicMock()
        page = BasePage(driver)
        assert page.driver is driver

    def test_wait_returns_webdriverwait_instance(self) -> None:
        from selenium.webdriver.support.ui import WebDriverWait

        driver = MagicMock()
        page = BasePage(driver)
        assert isinstance(page._wait(timeout=5), WebDriverWait)


class TestSearchPage:
    def test_search_uses_accessibility_id_when_found(self) -> None:
        """Happy path: field found by accessibility ID, button found and clicked."""
        page, driver, mock_wait = _search_page()
        mock_field = MagicMock()
        mock_wait.until.return_value = mock_field
        mock_button = MagicMock()
        driver.find_elements.return_value = [mock_button]

        page.search("quantum")

        mock_field.clear.assert_called_once()
        mock_field.send_keys.assert_called_once_with("quantum")
        mock_button.click.assert_called_once()

    def test_search_falls_back_to_xpath_and_executes_action(self) -> None:
        """Fallback: accessibility ID times out → XPath field, no button → execute_script."""
        page, driver, mock_wait = _search_page()
        mock_field = MagicMock()
        mock_wait.until.side_effect = [Exception("timeout"), mock_field]
        driver.find_elements.return_value = []

        page.search("quantum")

        driver.execute_script.assert_called_once()

    def test_get_results_waits_and_returns_elements(self) -> None:
        page, driver, mock_wait = _search_page()
        mock_elements = [MagicMock(), MagicMock()]
        mock_wait.until.return_value = mock_elements

        assert page.get_results() is mock_elements

    def test_get_current_results_returns_driver_elements(self) -> None:
        page, driver, mock_wait = _search_page()
        mock_elements = [MagicMock()]
        driver.find_elements.return_value = mock_elements

        assert page.get_current_results() is mock_elements

    def test_get_first_result_titles_returns_child_elements(self) -> None:
        page, driver, mock_wait = _search_page()
        mock_card = MagicMock()
        mock_titles = [MagicMock(), MagicMock()]
        mock_wait.until.return_value = [mock_card]
        mock_card.find_elements.return_value = mock_titles

        assert page.get_first_result_titles() == mock_titles

    def test_is_search_field_displayed_via_accessibility_id(self) -> None:
        page, driver, mock_wait = _search_page()
        mock_field = MagicMock()
        mock_field.is_displayed.return_value = True
        mock_wait.until.return_value = mock_field

        assert page.is_search_field_displayed() is True

    def test_is_search_field_displayed_falls_back_to_xpath(self) -> None:
        page, driver, mock_wait = _search_page()
        mock_field = MagicMock()
        mock_field.is_displayed.return_value = False
        mock_wait.until.side_effect = [Exception("timeout"), mock_field]

        assert page.is_search_field_displayed() is False

    def test_tap_favorite_via_accessibility_id(self) -> None:
        page, driver, mock_wait = _search_page()
        mock_button = MagicMock()
        driver.find_elements.return_value = [mock_button]

        page.tap_favorite_on_first_result()

        mock_button.click.assert_called_once()

    def test_tap_favorite_falls_back_to_xpath(self) -> None:
        """First find_elements returns nothing; XPATH fallback finds the button."""
        page, driver, mock_wait = _search_page()
        mock_button = MagicMock()
        driver.find_elements.side_effect = [[], [mock_button]]

        page.tap_favorite_on_first_result()

        mock_button.click.assert_called_once()


class TestFavoritesPage:
    def test_open_via_accessibility_id(self) -> None:
        page, driver, mock_wait = _favorites_page()
        mock_tab = MagicMock()
        mock_wait.until.return_value = mock_tab

        page.open()

        mock_tab.click.assert_called_once()

    def test_open_falls_back_to_xpath(self) -> None:
        page, driver, mock_wait = _favorites_page()
        mock_tab = MagicMock()
        mock_wait.until.side_effect = [Exception("timeout"), mock_tab]

        page.open()

        mock_tab.click.assert_called_once()

    def test_get_items_waits_and_returns_elements(self) -> None:
        page, driver, mock_wait = _favorites_page()
        mock_items = [MagicMock()]
        mock_wait.until.return_value = mock_items

        assert page.get_items() is mock_items

    def test_get_current_items_returns_driver_elements(self) -> None:
        page, driver, mock_wait = _favorites_page()
        mock_items = [MagicMock()]
        driver.find_elements.return_value = mock_items

        assert page.get_current_items() is mock_items

    def test_tap_favorite_via_accessibility_id(self) -> None:
        page, driver, mock_wait = _favorites_page()
        mock_button = MagicMock()
        driver.find_elements.return_value = [mock_button]

        page.tap_favorite_on_first_item()

        mock_button.click.assert_called_once()

    def test_tap_favorite_falls_back_to_xpath(self) -> None:
        """First find_elements returns nothing; XPATH fallback finds the button."""
        page, driver, mock_wait = _favorites_page()
        mock_button = MagicMock()
        driver.find_elements.side_effect = [[], [mock_button]]

        page.tap_favorite_on_first_item()

        mock_button.click.assert_called_once()
