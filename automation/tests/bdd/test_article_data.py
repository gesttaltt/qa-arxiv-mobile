"""
BDD tests for arXiv article data contract — pytest-bdd implementation.

Validates that the arXiv API returns all the fields the mobile app needs
to display articles in search results and the DOWNLOADED tab (id, title,
authors, published date) and that bulk operations receive well-formed,
distinct results.

Each scenario maps to a manual test case in manual-tests/test-cases/:
  Scenario "A search result contains all fields..."    → TC003
  Scenario "Multiple results all provide..."           → TC008

Shared fixtures (`result`, Given "I have access to the arXiv search API")
are defined in conftest.py.
"""

import xml.etree.ElementTree as ET

from pytest_bdd import parsers, scenarios, then, when

from ..utils import arxiv_get

scenarios("../../features/article_data_contract.feature")

_NS = {"atom": "http://www.w3.org/2005/Atom"}


# ---------------------------------------------------------------------------
# When
# ---------------------------------------------------------------------------


@when(parsers.parse('I fetch a paper from the search results for "{topic}"'))
def fetch_one_paper(result: dict, topic: str) -> None:
    response = arxiv_get(
        {"search_query": f"all:{topic}", "start": "0", "max_results": "1"}
    )
    assert response.status_code == 200, f"API returned {response.status_code}"
    root = ET.fromstring(response.content)
    entries = root.findall("atom:entry", _NS)
    assert entries, "No entries returned — cannot validate article data"
    result["entry"] = entries[0]


@when(parsers.parse('I fetch 5 papers from the search results for "{topic}"'))
def fetch_five_papers(result: dict, topic: str) -> None:
    response = arxiv_get(
        {"search_query": f"all:{topic}", "start": "0", "max_results": "5"}
    )
    assert response.status_code == 200, f"API returned {response.status_code}"
    root = ET.fromstring(response.content)
    entries = root.findall("atom:entry", _NS)
    assert entries, "No entries returned — cannot validate bulk article data"
    result["entries"] = entries


# ---------------------------------------------------------------------------
# Then — single paper (TC003)
# ---------------------------------------------------------------------------


@then("the paper has a unique identifier for storage")
def has_unique_id(result: dict) -> None:
    paper_id = result["entry"].findtext("atom:id", namespaces=_NS)
    assert paper_id and paper_id.strip(), "Entry is missing <id>"


@then("the paper has a non-empty title for display")
def has_title(result: dict) -> None:
    title = result["entry"].findtext("atom:title", namespaces=_NS)
    assert title and title.strip(), "Entry is missing <title>"


@then("the paper has at least one author for display")
def has_author(result: dict) -> None:
    authors = result["entry"].findall("atom:author", _NS)
    assert authors, "Entry has no <author> elements"
    name = authors[0].findtext("atom:name", namespaces=_NS)
    assert name and name.strip(), "First author has an empty <name>"


@then("the paper has a published date for metadata")
def has_published_date(result: dict) -> None:
    published = result["entry"].findtext("atom:published", namespaces=_NS)
    assert published and published.strip(), "Entry is missing <published> date"


# ---------------------------------------------------------------------------
# Then — bulk papers (TC008)
# ---------------------------------------------------------------------------


@then("every paper has a unique identifier")
def all_have_ids(result: dict) -> None:
    for entry in result["entries"]:
        paper_id = entry.findtext("atom:id", namespaces=_NS)
        assert paper_id and paper_id.strip(), "An entry is missing a non-empty <id>"


@then("every paper has a non-empty title")
def all_have_titles(result: dict) -> None:
    for entry in result["entries"]:
        title = entry.findtext("atom:title", namespaces=_NS)
        assert title and title.strip(), "An entry has a missing or empty <title>"


@then("all paper identifiers are distinct")
def ids_are_distinct(result: dict) -> None:
    ids = [
        (entry.findtext("atom:id", namespaces=_NS) or "").strip()
        for entry in result["entries"]
    ]
    assert len(ids) == len(set(ids)), f"Duplicate paper IDs found: {ids}"
