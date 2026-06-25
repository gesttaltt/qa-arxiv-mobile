"""
Appium smoke tests for the Favorites feature.

Covers TC003 (toggle favorite) at the UI layer.
Validate locator values with Appium Inspector before first run — see docs/APPIUM_SETUP.md.
"""

import pytest

from automation.pages import FavoritesPage, SearchPage


@pytest.mark.appium
class TestFavoritesSmoke:
    """
    TC003-Appium: Favorites feature UI smoke tests.
    Traceability: TC003 (toggle favorite).
    """

    def test_add_paper_to_favorites(self, android_driver) -> None:
        """
        TC003-Appium (part 1): Marking a paper as favorite makes it appear
        in the Favorites tab.

        Steps:
          1. Search for "deep learning"
          2. Tap the favorite/star button on the first result
          3. Navigate to the Favorites tab
          4. Assert the list contains at least one item
        """
        search = SearchPage(android_driver)
        favorites = FavoritesPage(android_driver)

        search.search("deep learning")
        search.get_results()
        search.tap_favorite_on_first_result()
        favorites.open()

        items = favorites.get_items()
        assert len(items) > 0, "TC003 FAIL: Favorites tab empty after marking a paper"

    def test_remove_paper_from_favorites(self, android_driver) -> None:
        """
        TC003-Appium (part 2): Unmarking a previously favorited paper removes it.

        Precondition: test_add_paper_to_favorites has run (session-scoped driver).

        Steps:
          1. Open the Favorites tab
          2. Record the current item count
          3. Tap the star on the first item to unmark it
          4. Assert the count decreased
        """
        favorites = FavoritesPage(android_driver)
        favorites.open()

        count_before = len(favorites.get_items())
        assert (
            count_before > 0
        ), "TC003 FAIL: Favorites list empty — run test_add_paper_to_favorites first"

        favorites.tap_favorite_on_first_item()

        try:
            count_after = len(favorites.get_items())
        except Exception:
            count_after = 0  # list became empty — valid outcome

        assert (
            count_after < count_before
        ), f"TC003 FAIL: Count unchanged after removing ({count_before} → {count_after})"

    def test_favorites_tab_is_empty_on_fresh_install(self, android_driver) -> None:
        """
        Sanity check: after app reset (no_reset=False in conftest), the
        Favorites tab should start empty before any interaction.

        Note: only meaningful when run first in a clean session.
        """
        android_driver.reset()

        favorites = FavoritesPage(android_driver)
        favorites.open()

        items = favorites.get_current_items()
        assert (
            len(items) == 0
        ), f"TC003 FAIL: Expected empty favorites on fresh install, found {len(items)}"
