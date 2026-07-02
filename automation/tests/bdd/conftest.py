"""Shared BDD fixtures and steps for the arXiv feature suite."""

import pytest
from pytest_bdd import given


@pytest.fixture
def result() -> dict:
    return {}


@given("I have access to the arXiv search API")
def api_access() -> None:
    pass  # connectivity is verified implicitly when the When step runs
