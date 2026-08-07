# TC015 – Slow network throttling (< 1 Mbps)

**User Story:** US004 – Network Connectivity
**ISTQB Design Technique:** Boundary Value Analysis (network speed boundary)
**Priority:** Low
**Platform:** Both (Android / iOS)
**Test Type:** Performance / Functional
**Status:** Designed — Not Executed (added 2026-08-07)

---

**Objective:**
Verify the app remains usable — showing a loading state rather than appearing frozen —
when the network is available but severely throttled (< 1 Mbps with induced latency), a
common real-world condition (poor cellular signal, congested public WiFi).

**Preconditions:**
- App is installed and running.
- iOS testing: iPhone simulator or device running iOS 15 or later, with **Additional Tools for
  Xcode** installed for Network Link Conditioner (Xcode 15+).
- Android: emulator network throttling settings, or a physical device behind a WiFi throttling
  proxy.
- Internet connectivity active but throttled to **< 1 Mbps** with **≥ 400 ms** induced round-trip
  latency.

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | Enable the throttling profile; record the exact bandwidth/latency/packet-loss settings used | Throttled condition confirmed active | |
| 2 | Search for `graph neural networks` | Request is dispatched | |
| 3 | Observe the UI while the request is in flight | A loading indicator is visible throughout; UI is not frozen or unresponsive; repeated taps on Search do not fire duplicate requests | |
| 4 | Wait for the request to complete or time out | Results eventually load, or a timeout message appears — record the observed timeout threshold if one triggers | |
| 5 | If a PDF is available, attempt a download under the same throttled condition | Progress indicator reflects the slow rate accurately; not stuck at 0% with no feedback | |

---

**Expected Result:**
- Step 3: The app clearly communicates "working" state throughout the wait.
- Step 4: Either a successful (slow) load or an explicit timeout message — never an indefinite
  silent wait.
- Step 5: Download progress feedback remains accurate under throttled conditions.

**Notes:**
- No timeout threshold is currently documented anywhere in the app or its docs. If one is
  observed during execution, record it and consider filing a testability-feedback note
  recommending it be documented explicitly.
- Relates to TC001 (baseline load-time expectation, ≤ 5 s under normal conditions — this TC is
  the boundary case at the opposite end), TC009 (WiFi to cellular transition).

---

**Automation Coverage:**

None at the mobile-UI level (requires real device/simulator network throttling). Partially
adjacent to `TestPerformanceBaseline` in `automation/tests/test_search_api.py`, which validates
SLA assertion logic under mocked 0.5 s / 3.5 s API latency — that covers the assertion logic,
not the mobile UI's behavior under a genuinely slow transport.
