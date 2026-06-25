"""
Session-level fixtures shared across all non-Appium tests.

Includes a lightweight rate-limit guard so the suite does not trip
arXiv's per-IP throttle when tests run sequentially (especially on
repeated local runs). The delay is deliberately small — CI runners
start with clean IP history and rarely need it.
"""

import time

import pytest
import requests

_INTER_TEST_DELAY = 0.8  # seconds between test executions


@pytest.fixture(autouse=True)
def _arxiv_rate_limit_guard() -> None:
    """Pause briefly before each test to avoid hitting arXiv's rate limit."""
    time.sleep(_INTER_TEST_DELAY)


def _get_with_retry(
    url: str,
    params: dict,
    timeout: int = 15,
    retries: int = 3,
    backoff: float = 5.0,
) -> requests.Response:
    """GET with simple retry on 429 / 5xx transient errors."""
    for attempt in range(retries):
        response = requests.get(url, params=params, timeout=timeout)
        if response.status_code == 429 and attempt < retries - 1:
            time.sleep(backoff * (attempt + 1))
            continue
        return response
    return response  # return last response after exhausting retries
