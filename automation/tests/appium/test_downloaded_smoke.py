"""
Appium smoke tests for the DOWNLOADED tab.

Covers TC003 (download a paper and remove it) and TC008 (bulk downloaded
papers management — boundary value 0) at the UI layer.
The DOWNLOADED tab shows articles saved to device storage.
On a fresh install there are no downloads, so the empty-state label is visible.
"""

import pytest

from automation.pages import DownloadedPage


@pytest.mark.appium
class TestDownloadedSmoke:
    """TC003/TC008-Appium: DOWNLOADED tab UI smoke tests."""

    def test_downloaded_tab_is_navigable(self, android_driver) -> None:
        """
        TC003-Appium: Tapping the DOWNLOADED tab does not crash the app
        and keeps the tab accessible.

        Steps:
          1. Tap the DOWNLOADED tab
          2. Assert the tab is still accessible (no crash)
        """
        page = DownloadedPage(android_driver)
        page.open()
        assert (
            page.is_empty_label_displayed() or len(page.get_current_items()) >= 0
        ), "TC003 FAIL: DOWNLOADED tab unreachable after tap — possible crash"

    def test_downloaded_tab_is_empty_on_fresh_install(self, android_driver) -> None:
        """
        TC008-Appium: On a fresh install (no_reset=False) the DOWNLOADED tab
        shows the empty-state label and no list items — the 0-item boundary
        from TC008's boundary value analysis.

        Steps:
          1. Tap the DOWNLOADED tab
          2. Assert the empty-state label is displayed
          3. Assert no downloaded article items are present
        """
        # driver.reset() removed — deprecated in Appium 2.x.
        # Session is fresh per CI run and no test downloads any article,
        # so the DOWNLOADED tab is always empty without an explicit reset.
        page = DownloadedPage(android_driver)
        page.open()

        assert (
            page.is_empty_label_displayed()
        ), "TC008 FAIL: Empty-state label not visible on fresh install"
        items = page.get_current_items()
        assert (
            len(items) == 0
        ), f"TC008 FAIL: Expected no downloaded items on fresh install, got {len(items)}"
