"""
Appium smoke tests for the Search feature.

Covers TC001 (valid search) and TC002 (empty search) at the UI layer.
Validate locator values with Appium Inspector before first run — see docs/APPIUM_SETUP.md.
"""

import pytest

from automation.pages import SearchPage


@pytest.mark.appium
class TestSearchSmoke:
    """
    TC001-Appium: Search feature UI smoke tests.
    Traceability: TC001 (valid search), TC002 (empty search).
    """

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
        page = SearchPage(android_driver)
        page.search("machine learning")

        results = page.get_results()
        assert len(results) > 0, "TC001 FAIL: No results for 'machine learning'"
        assert (
            page.get_first_result_titles()
        ), "TC001 FAIL: First result has no visible text"

    def test_empty_search_does_not_crash(self, android_driver) -> None:
        """
        TC002-Appium: Submitting an empty search keeps the app responsive
        and shows no result cards.

        Steps:
          1. Clear the search field
          2. Submit without entering text
          3. Assert the app remains responsive (search field still accessible)
          4. Assert no result cards are shown
        """
        page = SearchPage(android_driver)
        page.search("")

        assert (
            page.is_search_field_displayed()
        ), "TC002 FAIL: Search field not reachable after empty search — possible crash"
        results = page.get_current_results()
        assert (
            len(results) == 0
        ), f"TC002 FAIL: Expected no results for empty search, got {len(results)}"

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
        page = SearchPage(android_driver)
        page.search(keyword)

        results = page.get_results()
        assert len(results) > 0, f"TC001 FAIL: No results for keyword '{keyword}'"
