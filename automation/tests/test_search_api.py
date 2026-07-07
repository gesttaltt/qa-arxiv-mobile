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

    def test_network_timeout_propagates(self) -> None:
        """
        TC004 Automation Support: Network resilience testing.
        Validates that arxiv_get() propagates Timeout to the caller
        so the app can show an error state instead of hanging.
        """
        with patch("automation.tests.utils.requests.get") as mock_get:
            mock_get.side_effect = requests.exceptions.Timeout()
            with pytest.raises(requests.exceptions.Timeout):
                arxiv_get({"search_query": "all:test", "max_results": "1"})

    @pytest.mark.parametrize(
        "search_term,expected_min_results",
        [("quantum physics", 1), ("neural networks", 1), ("computer science", 1)],
    )
    def test_search_relevance_data_validation(
        self, search_term: str, expected_min_results: int
    ) -> None:
        """Each academic keyword must return at least expected_min_results entries."""
        response = arxiv_get(
            {"search_query": f"all:{search_term}", "start": "0", "max_results": "5"}
        )
        assert response.status_code == 200
        root = ET.fromstring(response.content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entries = root.findall("atom:entry", ns)
        assert len(entries) >= expected_min_results, (
            f"'{search_term}' returned {len(entries)} results, "
            f"expected at least {expected_min_results}"
        )


@pytest.fixture(scope="class")
def article_entry() -> ET.Element:
    """Fetch one arXiv entry for the entire TestArticleDataContract class.

    Using class scope avoids four separate API calls (one per test method)
    while still giving each test an independent assertion point.
    """
    response = arxiv_get(
        {"search_query": "all:deep learning", "start": "0", "max_results": "1"}
    )
    assert response.status_code == 200, "API unavailable — cannot validate article data"
    root = ET.fromstring(response.content)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entries = root.findall("atom:entry", ns)
    assert entries, "No entries returned — cannot validate article data"
    return entries[0]


class TestArticleDataContract:
    """
    Automation support for TC003: Article data contract.

    Verifies that the arXiv API returns the fields the app needs to display
    articles in search results and the DOWNLOADED tab (id, title, authors,
    published date). If any of these fields disappear from the API response,
    TC003 would break at the data layer before the UI is even involved.
    """

    NS = {"atom": "http://www.w3.org/2005/Atom"}

    def test_entry_has_id(self, article_entry: ET.Element) -> None:
        """Each paper must have a unique ID — used as the article storage key."""
        paper_id = article_entry.findtext("atom:id", namespaces=self.NS)
        assert paper_id and paper_id.strip(), "Entry is missing <id>"

    def test_entry_has_title(self, article_entry: ET.Element) -> None:
        """Each paper must have a title — displayed in search results and DOWNLOADED tab."""
        title = article_entry.findtext("atom:title", namespaces=self.NS)
        assert title and title.strip(), "Entry is missing <title>"

    def test_entry_has_authors(self, article_entry: ET.Element) -> None:
        """Each paper must have at least one author — shown below the title."""
        authors = article_entry.findall("atom:author", self.NS)
        assert authors, "Entry has no <author> elements"
        name = authors[0].findtext("atom:name", namespaces=self.NS)
        assert name and name.strip(), "First author has an empty <name>"

    def test_entry_has_published_date(self, article_entry: ET.Element) -> None:
        """Each paper must have a published date — shown as metadata."""
        published = article_entry.findtext("atom:published", namespaces=self.NS)
        assert published and published.strip(), "Entry is missing <published> date"


class TestSearchKeywordSanity:
    """
    Sanity checks for the search keywords used across the test suite.

    These tests verify that the arXiv API returns well-formed results for
    the academic terms that appear in TC001, BDD scenarios, and parametrised
    tests — so a failure here points to a data-layer problem, not a test bug.
    """

    def test_api_returns_atom_feed(self) -> None:
        """API must respond with a valid Atom feed for a generic query."""
        response = arxiv_get({"search_query": "all:test", "max_results": "1"})
        assert response.status_code == 200
        assert "application/atom+xml" in response.headers.get("content-type", "")

    @pytest.mark.parametrize(
        "term",
        [
            "machine learning",
            "quantum computing",
            "artificial intelligence",
            "deep learning",
        ],
    )
    def test_common_keyword_returns_at_least_one_result(self, term: str) -> None:
        """Each standard academic keyword must return at least one Atom entry."""
        response = arxiv_get(
            {"search_query": f"all:{term}", "start": "0", "max_results": "3"}
        )
        assert response.status_code == 200
        root = ET.fromstring(response.content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entries = root.findall("atom:entry", ns)
        assert (
            len(entries) >= 1
        ), f"'{term}' returned 0 results — keyword may be too specific or API changed"


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

    @pytest.mark.slow
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
