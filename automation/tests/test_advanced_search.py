"""
Advanced API search tests — pagination and author-field queries.

Demonstrates knowledge of the arXiv API beyond basic keyword search:

  Pagination (start offset):
    Validates that paging through results returns distinct, non-overlapping
    entries with accurate metadata. Equivalent to verifying that a SQL
    LIMIT/OFFSET implementation returns stable, non-repeating pages.

  Author-field queries (au:Name):
    Validates the au: prefix as a distinct Equivalence Partition from
    all: searches — a narrower search that scopes results to a specific
    researcher rather than any mention of the name across all fields.
"""

import xml.etree.ElementTree as ET

import pytest

from .utils import arxiv_get

ATOM_NS = "http://www.w3.org/2005/Atom"
OPENSEARCH_NS = "http://a9.com/-/spec/opensearch/1.1/"


@pytest.mark.integration
class TestPagination:
    """
    Validates the start offset parameter for paginating through results.

    SQL equivalent:
      Page 1 — SELECT * FROM papers ORDER BY relevance LIMIT 5 OFFSET 0
      Page 2 — SELECT * FROM papers ORDER BY relevance LIMIT 5 OFFSET 5
    """

    def test_second_page_returns_different_entries(self) -> None:
        """Pages must not overlap — start=0 and start=5 must return distinct IDs."""
        resp_p1 = arxiv_get(
            {"search_query": "all:machine learning", "start": "0", "max_results": "5"}
        )
        resp_p2 = arxiv_get(
            {"search_query": "all:machine learning", "start": "5", "max_results": "5"}
        )
        assert resp_p1.status_code == 200
        assert resp_p2.status_code == 200

        def _ids(resp) -> set:
            root = ET.fromstring(resp.content)
            return {
                (e.findtext(f"{{{ATOM_NS}}}id") or "").strip()
                for e in root.findall(f"{{{ATOM_NS}}}entry")
            }

        ids_p1 = _ids(resp_p1)
        ids_p2 = _ids(resp_p2)
        assert ids_p1, "Page 1 returned no entries"
        assert ids_p2, "Page 2 returned no entries"
        assert ids_p1.isdisjoint(
            ids_p2
        ), f"Pages 1 and 2 share entry IDs: {ids_p1 & ids_p2}"

    def test_start_index_metadata_matches_requested_offset(self) -> None:
        """opensearch:startIndex in the response must equal the requested start value."""
        response = arxiv_get(
            {"search_query": "all:deep learning", "start": "5", "max_results": "3"}
        )
        assert response.status_code == 200
        root = ET.fromstring(response.content)
        start_index = root.findtext(f"{{{OPENSEARCH_NS}}}startIndex")
        assert (
            start_index == "5"
        ), f"Expected opensearch:startIndex=5 but got '{start_index}'"

    def test_total_results_consistent_across_pages(self) -> None:
        """opensearch:totalResults must be identical on page 1 and page 2."""

        def _total(start: str) -> str:
            resp = arxiv_get(
                {"search_query": "all:quantum", "start": start, "max_results": "3"}
            )
            root = ET.fromstring(resp.content)
            return root.findtext(f"{{{OPENSEARCH_NS}}}totalResults") or ""

        total_p1 = _total("0")
        total_p2 = _total("3")
        assert (
            total_p1 and total_p2
        ), "totalResults element missing from one of the pages"
        assert (
            total_p1 == total_p2
        ), f"totalResults changed between pages: p1={total_p1}, p2={total_p2}"


@pytest.mark.integration
class TestAuthorSearch:
    """
    Validates the au: field prefix as a distinct query syntax class.

    EP rationale: au:Name is a narrower partition than all:Name — it
    restricts matching to the author field only, so it must return fewer
    total results and only papers where the name appears as an author.
    """

    def test_author_query_returns_results(self) -> None:
        """au:bengio must return at least one entry."""
        response = arxiv_get(
            {"search_query": "au:bengio", "start": "0", "max_results": "5"}
        )
        assert response.status_code == 200
        root = ET.fromstring(response.content)
        entries = root.findall(f"{{{ATOM_NS}}}entry")
        assert len(entries) >= 1, "au:bengio returned no results"

    def test_author_field_is_more_specific_than_all_field(self) -> None:
        """au:bengio must return fewer total results than all:bengio.

        all: searches every field including title, abstract, and author,
        so it always matches a superset of au: which searches author only.
        """

        def _total(query: str) -> int:
            resp = arxiv_get({"search_query": query, "start": "0", "max_results": "1"})
            root = ET.fromstring(resp.content)
            return int(root.findtext(f"{{{OPENSEARCH_NS}}}totalResults") or "0")

        total_author = _total("au:bengio")
        total_all = _total("all:bengio")
        assert total_author < total_all, (
            f"Expected au: to be more specific than all: "
            f"(got au:{total_author} vs all:{total_all})"
        )

    def test_author_results_contain_queried_name(self) -> None:
        """At least one result from au:bengio must list 'bengio' as an author."""
        response = arxiv_get(
            {"search_query": "au:bengio", "start": "0", "max_results": "5"}
        )
        assert response.status_code == 200
        root = ET.fromstring(response.content)
        entries = root.findall(f"{{{ATOM_NS}}}entry")

        found = any(
            "bengio" in (author.findtext(f"{{{ATOM_NS}}}name") or "").lower()
            for entry in entries
            for author in entry.findall(f"{{{ATOM_NS}}}author")
        )
        assert found, "No entry from au:bengio search lists 'bengio' as an author"
