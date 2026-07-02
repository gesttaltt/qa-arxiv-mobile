"""
BDD tests for arXiv paper search — pytest-bdd implementation.

Each scenario maps to a manual test case in manual-tests/test-cases/:
  Scenario "Valid keyword returns results"          → TC001
  Scenario "Empty query is handled gracefully"      → TC002
  Scenario Outline "Popular academic topics..."     → TC001 (parametrised)

Step definitions share state through the `result` fixture (a plain dict).
Steps mutate it; Then-steps read from it.

Shared fixtures (`result`, Given "I have access to the arXiv search API")
are defined in conftest.py so they are available to all BDD test modules.
"""

import xml.etree.ElementTree as ET

from pytest_bdd import parsers, scenarios, then, when

from ..utils import arxiv_get

scenarios("../../features/search.feature")

_NS = {"atom": "http://www.w3.org/2005/Atom"}


# ---------------------------------------------------------------------------
# When
# ---------------------------------------------------------------------------


@when(parsers.parse('I search for "{keyword}"'))
def search_for_keyword(result: dict, keyword: str) -> None:
    result["response"] = arxiv_get(
        {"search_query": f"all:{keyword}", "start": "0", "max_results": "5"}
    )


@when("I search with an empty query")
def search_empty(result: dict) -> None:
    result["response"] = arxiv_get(
        {"search_query": "", "start": "0", "max_results": "5"}
    )


# ---------------------------------------------------------------------------
# Then
# ---------------------------------------------------------------------------


@then("the response status is 200")
def status_200(result: dict) -> None:
    assert result["response"].status_code == 200


@then("the response status is 200 or 400")
def status_200_or_400(result: dict) -> None:
    assert result["response"].status_code in (
        200,
        400,
    ), f"Unexpected status {result['response'].status_code}"


@then("the response contains at least 1 paper")
def has_results(result: dict) -> None:
    root = ET.fromstring(result["response"].content)
    entries = root.findall("atom:entry", _NS)
    assert len(entries) >= 1, f"Expected at least 1 paper but got {len(entries)}"


@then("each paper has a non-empty title")
def has_titles(result: dict) -> None:
    root = ET.fromstring(result["response"].content)
    for entry in root.findall("atom:entry", _NS):
        title = entry.findtext("atom:title", namespaces=_NS)
        assert title and title.strip(), "Found a paper with an empty or missing <title>"
