"""
API-level validation for valid search queries against the arXiv API.

Replaces a former Selenium-based test that was incompatible with React Native
(native mobile apps do not expose a browser DOM). The arXiv API is the data
layer that the mobile search feature depends on, so validating it at the API
level provides meaningful coverage that complements the Appium UI smoke tests
in automation/tests/appium/.

See also:
  - test_search_empty.py (empty/invalid query API behavior)
  - test_search_api.py (response structure, data formats)
  - automation/tests/appium/test_search_smoke.py (UI-layer smoke tests)
"""

import xml.etree.ElementTree as ET

import pytest

from .utils import arxiv_get


@pytest.mark.integration
class TestValidSearchAPI:
    """Validates that well-formed search queries return expected results."""

    def test_valid_keyword_returns_results(self) -> None:
        """A standard academic keyword must return at least one result entry."""
        response = arxiv_get(
            {"search_query": "all:quantum computing", "start": "0", "max_results": "5"}
        )

        assert response.status_code == 200
        assert "application/atom+xml" in response.headers.get("content-type", "")
        assert "<entry>" in response.text

    def test_multi_word_query_accepted(self) -> None:
        """Multi-word queries with URL-unsafe characters must not error."""
        response = arxiv_get(
            {
                "search_query": 'all:"machine learning"',
                "start": "0",
                "max_results": "3",
            }
        )
        assert response.status_code == 200
        assert "<entry>" in response.text

    @pytest.mark.parametrize("max_results", [1, 3, 10])
    def test_max_results_param_respected(self, max_results: int) -> None:
        """The max_results parameter must cap the number of entries returned."""
        response = arxiv_get(
            {
                "search_query": "all:test",
                "start": "0",
                "max_results": str(max_results),
            }
        )
        assert response.status_code == 200
        root = ET.fromstring(response.content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entries = root.findall("atom:entry", ns)
        assert (
            len(entries) <= max_results
        ), f"Expected <= {max_results} entries, got {len(entries)}"
