"""Session-level fixtures shared across all non-Appium tests."""

import time

import pytest

_INTER_TEST_DELAY = 1.5


@pytest.fixture(autouse=True)
def _arxiv_rate_limit_guard() -> None:
    """Pause briefly before each test to avoid hitting arXiv's rate limit."""
    time.sleep(_INTER_TEST_DELAY)
