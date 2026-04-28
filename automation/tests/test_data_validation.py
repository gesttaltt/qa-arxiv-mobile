"""
Data validation tests — arXiv API response layer.

Validates field presence, data types, and format rules in the Atom XML
response. Mirrors the kind of assertions a QA tester runs via SQL against
a backend database; here applied to the API's XML payload.

See docs/TESTING_THEORY.md § 4 (SQL Data Validation) for the DB-query
equivalents of each assertion.
"""

import re
import xml.etree.ElementTree as ET

import pytest
import requests

BASE_URL = "http://export.arxiv.org/api/query"
ATOM_NS = "http://www.w3.org/2005/Atom"
ARXIV_NS = "http://arxiv.org/schemas/atom"


def _fetch_entries(search_term: str, max_results: int = 5) -> list[ET.Element]:
    params = {
        "search_query": f"all:{search_term}",
        "start": 0,
        "max_results": max_results,
    }
    response = requests.get(BASE_URL, params=params, timeout=15)
    assert response.status_code == 200
    root = ET.fromstring(response.content)
    return root.findall(f"{{{ATOM_NS}}}entry")


@pytest.mark.integration
class TestRequiredFieldPresence:
    """
    Validate that required fields are never absent or empty.
    SQL equivalent: SELECT id FROM papers WHERE title IS NULL OR authors IS NULL
    """

    def test_every_entry_has_an_id(self) -> None:
        entries = _fetch_entries("machine learning")
        assert entries, "No entries returned — cannot validate fields"
        for entry in entries:
            entry_id = entry.findtext(f"{{{ATOM_NS}}}id")
            assert entry_id and entry_id.strip(), (
                "Entry is missing a non-empty <id> element"
            )

    def test_every_entry_has_a_title(self) -> None:
        entries = _fetch_entries("neural networks")
        for entry in entries:
            title = entry.findtext(f"{{{ATOM_NS}}}title")
            assert title and title.strip(), "Entry has a null or empty <title>"

    def test_every_entry_has_at_least_one_author(self) -> None:
        entries = _fetch_entries("quantum computing")
        for entry in entries:
            authors = entry.findall(f"{{{ATOM_NS}}}author")
            assert len(authors) >= 1, "Entry has no <author> elements"
            for author in authors:
                name = author.findtext(f"{{{ATOM_NS}}}name")
                assert name and name.strip(), "Author element contains an empty <name>"

    def test_every_entry_has_a_published_date(self) -> None:
        entries = _fetch_entries("deep learning")
        for entry in entries:
            published = entry.findtext(f"{{{ATOM_NS}}}published")
            assert published and published.strip(), (
                "Entry has a null or empty <published> date"
            )

    def test_every_entry_has_a_summary(self) -> None:
        entries = _fetch_entries("computer vision")
        for entry in entries:
            summary = entry.findtext(f"{{{ATOM_NS}}}summary")
            assert summary and len(summary.strip()) > 10, (
                "Entry has a missing or suspiciously short <summary>"
            )


@pytest.mark.integration
class TestDataFormats:
    """
    Validate field formats and data types.
    SQL equivalent: WHERE published_date NOT LIKE '____-__-__T__:__:__Z'
    """

    ISO8601_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    ARXIV_ID_PATTERN = re.compile(r"https?://arxiv\.org/abs/[\w./]+")

    def test_published_date_is_iso8601(self) -> None:
        entries = _fetch_entries("robotics")
        for entry in entries:
            published = entry.findtext(f"{{{ATOM_NS}}}published") or ""
            assert self.ISO8601_PATTERN.match(published.strip()), (
                f"Published date '{published}' does not match ISO 8601 format"
            )

    def test_entry_id_is_valid_arxiv_url(self) -> None:
        entries = _fetch_entries("reinforcement learning")
        for entry in entries:
            entry_id = entry.findtext(f"{{{ATOM_NS}}}id") or ""
            assert self.ARXIV_ID_PATTERN.match(entry_id.strip()), (
                f"Entry ID '{entry_id}' is not a valid arXiv abstract URL"
            )

    def test_no_duplicate_entry_ids(self) -> None:
        """
        SQL equivalent: SELECT paper_id, COUNT(*) FROM papers
        GROUP BY paper_id HAVING COUNT(*) > 1
        """
        entries = _fetch_entries("artificial intelligence", max_results=10)
        ids = [
            (entry.findtext(f"{{{ATOM_NS}}}id") or "").strip() for entry in entries
        ]
        assert len(ids) == len(set(ids)), (
            f"Duplicate entry IDs found in response: {ids}"
        )


@pytest.mark.integration
class TestResponseMetadata:
    """
    Validate opensearch metadata fields used for pagination.
    """

    def test_total_results_is_a_positive_integer(self) -> None:
        params = {
            "search_query": "all:machine learning",
            "start": 0,
            "max_results": 5,
        }
        response = requests.get(BASE_URL, params=params, timeout=15)
        root = ET.fromstring(response.content)
        total = root.findtext(
            "{http://a9.com/-/spec/opensearch/1.1/}totalResults"
        )
        assert total is not None, "opensearch:totalResults element is missing"
        assert int(total) > 0, f"totalResults should be > 0, got '{total}'"

    def test_items_per_page_matches_max_results_param(self) -> None:
        params = {
            "search_query": "all:quantum",
            "start": 0,
            "max_results": 3,
        }
        response = requests.get(BASE_URL, params=params, timeout=15)
        root = ET.fromstring(response.content)
        items_per_page = root.findtext(
            "{http://a9.com/-/spec/opensearch/1.1/}itemsPerPage"
        )
        assert items_per_page == "3", (
            f"itemsPerPage '{items_per_page}' does not match requested max_results=3"
        )
