"""Unit tests for arxiv_get retry logic in utils.py."""

from unittest.mock import call, patch

import requests

from .utils import arxiv_get


def _response(status_code: int) -> requests.Response:
    r = requests.Response()
    r.status_code = status_code
    return r


class TestArxivGetRetry:
    """Verifies retry behaviour without hitting the real arXiv API."""

    def test_success_on_first_attempt_skips_sleep(self) -> None:
        """200 on the first try — no sleep, one request."""
        with (
            patch(
                "automation.tests.utils.requests.get", return_value=_response(200)
            ) as mock_get,
            patch("automation.tests.utils.time.sleep") as mock_sleep,
        ):
            response = arxiv_get({"search_query": "all:test"})

        assert response.status_code == 200
        mock_get.assert_called_once()
        mock_sleep.assert_not_called()

    def test_retries_once_on_429_then_succeeds(self) -> None:
        """429 then 200 — sleeps once with backoff * 1, returns the 200."""
        with (
            patch(
                "automation.tests.utils.requests.get",
                side_effect=[_response(429), _response(200)],
            ) as mock_get,
            patch("automation.tests.utils.time.sleep") as mock_sleep,
        ):
            response = arxiv_get({"search_query": "all:test"}, backoff=1.0)

        assert response.status_code == 200
        assert mock_get.call_count == 2
        mock_sleep.assert_called_once_with(1.0)  # backoff * (0 + 1)

    def test_retries_twice_with_increasing_backoff(self) -> None:
        """429 twice then 200 — sleeps twice with backoff * 1 then backoff * 2."""
        with (
            patch(
                "automation.tests.utils.requests.get",
                side_effect=[_response(429), _response(429), _response(200)],
            ) as mock_get,
            patch("automation.tests.utils.time.sleep") as mock_sleep,
        ):
            response = arxiv_get({"search_query": "all:test"}, retries=3, backoff=1.0)

        assert response.status_code == 200
        assert mock_get.call_count == 3
        mock_sleep.assert_has_calls([call(1.0), call(2.0)])

    def test_returns_last_429_when_all_retries_exhausted(self) -> None:
        """Three 429s with retries=3 — sleeps twice, returns the final 429."""
        with (
            patch(
                "automation.tests.utils.requests.get",
                side_effect=[_response(429), _response(429), _response(429)],
            ) as mock_get,
            patch("automation.tests.utils.time.sleep") as mock_sleep,
        ):
            response = arxiv_get({"search_query": "all:test"}, retries=3, backoff=1.0)

        assert response.status_code == 429
        assert mock_get.call_count == 3
        assert mock_sleep.call_count == 2  # not called on the last attempt
