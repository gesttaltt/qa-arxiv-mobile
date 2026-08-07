# TC016 – Server error responses (429 / 503) from the arXiv API

**User Story:** US001 – Search for Academic Papers
**ISTQB Design Technique:** Error Guessing
**Priority:** Medium
**Platform:** Both (Android / iOS)
**Test Type:** Functional – Negative
**Status:** Designed — Not Executed (added 2026-08-07)

---

**Objective:**
Verify the app shows a clear, non-crashing message when the arXiv API responds with a
rate-limit (429) or service-unavailable (503) error, and that this is visibly distinguished
from a legitimate "no results found" state.

**Preconditions:**
- App is installed and running; internet connectivity is active.
- iOS testing: iPhone simulator or device running iOS 15 or later (Xcode 15+ if using Simulator).
- A way to simulate a 429/503 response: either a local intercepting proxy (e.g. mitmproxy)
  configured on the device/simulator to return a crafted 429/503 for the arXiv API host, or
  rapid repeated searches to trigger a real 429 from arXiv directly.

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | Configure the interception method, or fire several rapid repeated searches | 429/503 response is reliably reproducible | |
| 2 | Submit a search | Request is dispatched | |
| 3 | Observe how the app renders the 429/503 response | App shows a server-error message (e.g., "Search temporarily unavailable, try again") — **not** an empty-results state indistinguishable from a real zero-match search | |
| 4 | Confirm the search field and app remain usable | No crash; user can retry immediately | |
| 5 | Wait past the rate-limit window (or restore the normal response) and retry the same search | Search succeeds normally | |

---

**Expected Result:**
- Step 3: Server errors are visually distinct from "no matches" — a user should never conclude
  their search term has no results when the real cause is a server error.
- Step 5: The app recovers automatically on retry, without requiring an app restart.

**Notes:**
- `automation/tests/utils.py`'s `arxiv_get()` already retries 429s with exponential backoff at
  the HTTP layer (covered by `automation/tests/test_utils.py`, 100% branch coverage on the retry
  function). This TC validates the **UI-level** experience during the retry window and after
  retries are exhausted — something the automated unit tests do not observe, since they assert
  on the retry function's return value, not on any rendered screen state.
- Relates to `automation/tests/test_utils.py` (automated retry-logic coverage) and TC001
  (baseline search flow).

---

**Automation Coverage:**

| Layer | File | What it validates |
|---|---|---|
| Unit (retry logic only, not UI) | `automation/tests/test_utils.py` — `TestArxivGetRetry` | 429 retry with exponential backoff: success path, 1-retry, 2-retry, exhausted-retries branches |
