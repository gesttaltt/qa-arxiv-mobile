"""
PDF link contract tests — arXiv API response layer.

Validates that every arXiv search result exposes the link fields the
mobile app needs to open or download a paper PDF. A structural change
upstream would break TC005–TC007 at the data layer before any Appium
test could catch it.

Each TC maps to one or more assertions here:
  TC005 (PDF download and viewing)    → pdf_link presence + URL pattern
  TC006 (iOS Safari PDF integration)  → abstract_link presence + URL pattern
  TC007 (Android intent handling)     → pdf_link presence (intent fires from PDF href)
"""

import re
import xml.etree.ElementTree as ET

import pytest

from .utils import arxiv_get

ATOM_NS = "http://www.w3.org/2005/Atom"
_PDF_URL_PATTERN = re.compile(r"https?://arxiv\.org/pdf/[\w./]+")
_ABSTRACT_URL_PATTERN = re.compile(r"https?://arxiv\.org/abs/[\w./]+")


def _fetch_entries(search_term: str, max_results: int = 3) -> list[ET.Element]:
    response = arxiv_get(
        {
            "search_query": f"all:{search_term}",
            "start": "0",
            "max_results": str(max_results),
        }
    )
    assert response.status_code == 200
    root = ET.fromstring(response.content)
    return root.findall(f"{{{ATOM_NS}}}entry")


@pytest.mark.integration
class TestPDFLinkContract:
    """
    Automation support for TC005, TC006, TC007: PDF download and viewing.

    The mobile app builds its download URL and intent payload from the
    <link> elements in each Atom entry. These tests verify that the
    required links are present and correctly formatted so that a silent
    API change does not silently break PDF access in the app.
    """

    def test_every_entry_has_a_pdf_link(self) -> None:
        """Each paper must expose a PDF link (type='application/pdf') — TC005, TC007."""
        entries = _fetch_entries("machine learning")
        assert entries, "No entries returned — cannot validate PDF links"
        for entry in entries:
            links = entry.findall(f"{{{ATOM_NS}}}link")
            pdf_links = [lnk for lnk in links if lnk.get("type") == "application/pdf"]
            entry_id = entry.findtext(f"{{{ATOM_NS}}}id") or "unknown"
            assert pdf_links, f"Entry '{entry_id}' has no PDF link"

    def test_pdf_link_url_matches_arxiv_pattern(self) -> None:
        """PDF href must follow the arxiv.org/pdf/<id> format — TC005, TC007."""
        entries = _fetch_entries("neural networks")
        assert entries
        for entry in entries:
            for lnk in entry.findall(f"{{{ATOM_NS}}}link"):
                if lnk.get("type") == "application/pdf":
                    href = lnk.get("href", "")
                    assert _PDF_URL_PATTERN.match(
                        href
                    ), f"PDF URL '{href}' does not match expected arxiv.org/pdf/ pattern"

    def test_every_entry_has_an_abstract_link(self) -> None:
        """Each paper must have an abstract link (rel='alternate') — TC006, TC007."""
        entries = _fetch_entries("deep learning")
        assert entries
        for entry in entries:
            links = entry.findall(f"{{{ATOM_NS}}}link")
            abstract_links = [
                lnk
                for lnk in links
                if lnk.get("rel") == "alternate" and lnk.get("type") == "text/html"
            ]
            entry_id = entry.findtext(f"{{{ATOM_NS}}}id") or "unknown"
            assert abstract_links, f"Entry '{entry_id}' has no abstract link"

    def test_abstract_link_url_matches_arxiv_pattern(self) -> None:
        """Abstract href must follow the arxiv.org/abs/<id> format — TC006."""
        entries = _fetch_entries("quantum computing")
        assert entries
        for entry in entries:
            for lnk in entry.findall(f"{{{ATOM_NS}}}link"):
                if lnk.get("rel") == "alternate" and lnk.get("type") == "text/html":
                    href = lnk.get("href", "")
                    assert _ABSTRACT_URL_PATTERN.match(
                        href
                    ), f"Abstract URL '{href}' does not match expected arxiv.org/abs/ pattern"
