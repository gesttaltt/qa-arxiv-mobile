"""
API-level validation for empty and malformed search queries.

Replaces a former Selenium-based test that was incompatible with React Native
(native mobile apps do not expose a browser DOM). The arXiv API is the data
layer that the mobile search feature depends on.

These tests cover the negative scenarios that TC002 (empty query) validates
manually at the UI layer.  See automation/tests/appium/test_search_smoke.py
for the UI smoke equivalent.
"""

import pytest
import requests

BASE_URL = "http://export.arxiv.org/api/query"


@pytest.mark.integration
class TestEmptySearchAPI:
    """Validates how the API handles empty, missing, or malformed queries."""

    def test_empty_query_param_returns_200(self) -> None:
        """
        An empty search_query parameter should not crash the API.
        The API returns either 200 with no results or a 400 validation error.
        """
        params = {"search_query": "", "start": "0", "max_results": "10"}
        response = requests.get(BASE_URL, params=params, timeout=15)
        assert response.status_code in (200, 400)

    def test_missing_query_param_returns_400(self) -> None:
        """
        Omitting the search_query parameter entirely should produce a
        client-error status.
        """
        params = {"start": "0", "max_results": "10"}
        response = requests.get(BASE_URL, params=params, timeout=15)
        assert response.status_code == 400

    def test_whitespace_only_query(self) -> None:
        """
        A search query consisting only of whitespace characters.
        The API should handle this without crashing (200 or 400).
        """
        params = {"search_query": "   ", "start": "0", "max_results": "10"}
        response = requests.get(BASE_URL, params=params, timeout=15)
        assert response.status_code in (200, 400)

    def test_special_characters_in_query(self) -> None:
        """
        Special / control characters in the query should not cause a 500.
        """
        params = {
            "search_query": "all:\x00\x01\x02",
            "start": "0",
            "max_results": "5",
        }
        response = requests.get(BASE_URL, params=params, timeout=15)
        assert response.status_code in (200, 400)
