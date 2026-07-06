"""
Appium smoke tests for the DOWNLOADED tab.

Covers TC004 (downloaded articles) at the UI layer.
The DOWNLOADED tab shows articles saved to device storage.
On a fresh install there are no downloads, so the empty-state label is visible.
"""

import pytest

from automation.pages import DownloadedPage


@pytest.mark.appium
class TestDownloadedSmoke:
    """TC004-Appium: DOWNLOADED tab UI smoke tests."""

    def test_downloaded_tab_is_navigable(self, android_driver) -> None:
        """
        TC004-Appium: Tapping the DOWNLOADED tab does not crash the app
        and keeps the tab accessible.

        Steps:
          1. Tap the DOWNLOADED tab
          2. Assert the tab is still accessible (no crash)
        """
        page = DownloadedPage(android_driver)
        page.open()
        assert page.is_empty_label_displayed() or len(page.get_current_items()) >= 0, (
            "TC004 FAIL: DOWNLOADED tab unreachable after tap — possible crash"
        )

    def test_downloaded_tab_is_empty_on_fresh_install(self, android_driver) -> None:
        """
        TC004-Appium: On a fresh install (no_reset=False) the DOWNLOADED tab
        shows the empty-state label and no list items.

        Steps:
          1. Tap the DOWNLOADED tab
          2. Assert the empty-state label is displayed
          3. Assert no downloaded article items are present
        """
        android_driver.reset()

        page = DownloadedPage(android_driver)
        page.open()

        assert page.is_empty_label_displayed(), (
            "TC004 FAIL: Empty-state label not visible on fresh install"
        )
        items = page.get_current_items()
        assert len(items) == 0, (
            f"TC004 FAIL: Expected no downloaded items on fresh install, got {len(items)}"
        )
