"""Shared utilities for the non-Appium test suite."""

import time

import requests

ARXIV_BASE_URL = "http://export.arxiv.org/api/query"


def arxiv_get(
    params: dict,
    timeout: int = 15,
    retries: int = 3,
    backoff: float = 5.0,
) -> requests.Response:
    """GET the arXiv API with automatic retry on 429 rate-limit responses."""
    for attempt in range(retries):
        response = requests.get(ARXIV_BASE_URL, params=params, timeout=timeout)
        if response.status_code == 429 and attempt < retries - 1:
            time.sleep(backoff * (attempt + 1))
            continue
        return response
    return response
