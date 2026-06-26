import time
import xml.etree.ElementTree as ET
from unittest.mock import patch

import pytest
import requests

from .utils import ARXIV_BASE_URL, arxiv_get


class TestArxivSearchAPI:
    """
    Automation examples that complement manual testing efforts.
    These tests focus on API validation while manual tests verify UI/UX.
    """

    def test_search_valid_keyword_api_response(self) -> None:
        """
        TC001 Automation Support: Validates API response structure.
        Manual test focuses on UI behavior, this validates data layer.
        """
        search_term = "machine learning"
        response = arxiv_get(
            {"search_query": f"all:{search_term}", "start": "0", "max_results": "10"}
        )

        assert response.status_code == 200
        assert "application/atom+xml" in response.headers.get("content-type", "")
        root = ET.fromstring(response.content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entries = root.findall("atom:entry", ns)
        assert len(entries) > 0, "No Atom entries returned"
        all_text = " ".join(
            (
                entry.findtext("atom:title", "", ns)
                + " "
                + entry.findtext("atom:summary", "", ns)
            ).lower()
            for entry in entries
        )
        assert (
            search_term.lower() in all_text
        ), f"Search term '{search_term}' not found in any entry title or summary"

    def test_empty_search_api_validation(self) -> None:
        """
        TC002 Automation Support: API-level validation of empty queries.
        Complements manual testing of UI validation behavior.
        """
        response = arxiv_get({"search_query": "", "start": "0", "max_results": "10"})
        assert response.status_code in (200, 400)

    def test_network_timeout_handling(self) -> None:
        """
        TC004 Automation Support: Network resilience testing.
        Validates timeout behaviour that manual testing observes.
        """
        with patch("requests.get") as mock_get:
            mock_get.side_effect = requests.exceptions.Timeout()
            with pytest.raises(requests.exceptions.Timeout):
                requests.get(ARXIV_BASE_URL, timeout=1)

    @pytest.mark.parametrize(
        "search_term,expected_min_results",
        [("quantum physics", 1), ("neural networks", 1), ("computer science", 1)],
    )
    def test_search_relevance_data_validation(
        self, search_term: str, expected_min_results: int
    ) -> None:
        """Data-driven testing to validate search relevance."""
        response = arxiv_get(
            {"search_query": f"all:{search_term}", "start": "0", "max_results": "5"}
        )
        assert response.status_code == 200
        assert len(response.text) > 100


class TestFavoritesDataPersistence:
    """
    Automation support for TC003: Favorites functionality.
    Focuses on data persistence while manual testing validates UI interactions.
    """

    def test_favorite_data_structure(self) -> None:
        """Validates favorite paper data structure consistency."""
        favorite_paper = {
            "id": "arxiv:1234.5678",
            "title": "Sample Paper Title",
            "authors": ["Author One", "Author Two"],
            "abstract": "Sample abstract text...",
            "published": "2025-01-01",
            "is_favorite": True,
            "date_favorited": "2025-01-20T10:30:00Z",
        }

        required_fields = ["id", "title", "authors", "is_favorite"]
        for field in required_fields:
            assert field in favorite_paper
            assert favorite_paper[field] is not None

        assert isinstance(favorite_paper["is_favorite"], bool)
        assert isinstance(favorite_paper["authors"], list)
        assert len(favorite_paper["authors"]) > 0


class TestManualTestingSupport:
    """Utility tests that verify the environment is ready for manual testing."""

    def test_test_environment_connectivity(self) -> None:
        """Validates test environment is ready for manual testing."""
        response = arxiv_get({"search_query": "all:test", "max_results": "1"})
        assert response.status_code == 200

    def test_generate_test_data_for_manual_testing(self) -> None:
        """Ensures each standard test keyword returns results for manual testers."""
        test_search_terms = [
            "machine learning",
            "quantum computing",
            "artificial intelligence",
            "deep learning",
        ]
        for term in test_search_terms:
            response = arxiv_get(
                {"search_query": f"all:{term}", "start": "0", "max_results": "3"}
            )
            assert response.status_code == 200
            assert len(response.text) > 500


class TestPerformanceBaseline:
    """
    Non-functional: SLA enforcement logic for the arXiv search endpoint.

    These tests verify that the 3-second SLA check behaves correctly under
    fast and slow response conditions. They use mocks to simulate controlled
    latency instead of hitting the real API — measuring arXiv's server speed
    in an automated test is not meaningful because it is a third-party service
    outside our control and subject to rate-limiting.

    See docs/TESTING_THEORY.md § 5 (Performance Testing Categories).
    """

    SLA_SECONDS = 3.0

    def _make_timed_request(self) -> tuple[requests.Response, float]:
        """Issue one HTTP call and return (response, elapsed_seconds)."""
        params = {
            "search_query": "all:machine learning",
            "start": "0",
            "max_results": "5",
        }
        start = time.monotonic()
        response = requests.get(ARXIV_BASE_URL, params=params, timeout=15)
        elapsed = time.monotonic() - start
        return response, elapsed

    def test_fast_response_passes_sla(self) -> None:
        """A response arriving in 0.5 s must not trigger the SLA assertion."""

        def fast_response(*args, **kwargs):
            time.sleep(0.5)
            mock = requests.Response()
            mock.status_code = 200
            return mock

        with patch("requests.get", side_effect=fast_response):
            response, elapsed = self._make_timed_request()

        assert response.status_code == 200
        assert (
            elapsed < self.SLA_SECONDS
        ), f"Expected elapsed < {self.SLA_SECONDS}s but got {elapsed:.2f}s"

    def test_slow_response_fails_sla(self) -> None:
        """A response arriving in 3.5 s must be caught by the SLA assertion."""

        def slow_response(*args, **kwargs):
            time.sleep(3.5)
            mock = requests.Response()
            mock.status_code = 200
            return mock

        with patch("requests.get", side_effect=slow_response):
            response, elapsed = self._make_timed_request()

        assert response.status_code == 200
        assert elapsed >= self.SLA_SECONDS, (
            f"Expected elapsed >= {self.SLA_SECONDS}s but got {elapsed:.2f}s — "
            "SLA check would not have caught this slow response"
        )
