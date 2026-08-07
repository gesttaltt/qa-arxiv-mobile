# TC014 – Airplane mode triggered mid-search-request

**User Story:** US001 – Search for Academic Papers (secondary: US004 – Network Connectivity)
**ISTQB Design Technique:** Error Guessing + State Transition Testing
**Priority:** Medium
**Platform:** Both (Android / iOS)
**Test Type:** Functional – Negative
**Status:** Designed — Not Executed (added 2026-08-07)

---

**Objective:**
Verify the app handles network loss that occurs **after** a search request has already
been sent but **before** the response arrives — distinct from TC004, which starts already
offline before any request is made. This targets a common source of unhandled promise
rejections and race conditions in `fetch`-based React Native apps.

**State Diagram:**

```
[Online] ── submit search ──► [Request in flight] ── airplane mode enabled ──► [Interrupted]
                                                                                    │
                                                            ┌───────────────────────┘
                                                            ▼
                                                   [Error shown, UI stable]
                                                            │
                                                  airplane mode disabled
                                                            ▼
                                                    [Retry succeeds]
```

**Preconditions:**
- App is installed and running; internet connectivity is active.
- iOS testing: iPhone simulator or device running iOS 15 or later (Xcode 15+ if using Simulator).
- A quick way to trigger Airplane Mode from Control Center / Quick Settings.
- Optional: a throttled connection (see TC015) makes the in-flight timing window easier to
  hit consistently.

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | Type a search keyword, e.g. `superconductivity` | Text is accepted in the field | |
| 2 | Tap the keyboard's Search key to submit | Request is dispatched; loading indicator appears | |
| 3 | Immediately (within ~1 second, before results render) enable Airplane Mode | Airplane Mode engages while the request is still pending | |
| 4 | Observe app behavior | A clear network-error or timeout message appears; no infinite spinner, no crash, no stale/partial list rendered as if complete | |
| 5 | Disable Airplane Mode | Connectivity restores | |
| 6 | Repeat the same search | Results load successfully | |

---

**Expected Result:**
- Step 4: The interrupted request resolves into a visible error state, not a silent hang.
- Step 6: The app recovers fully without requiring a restart.

**Notes:**
- Distinct from TC004 (already offline before the request starts). This test targets the
  request-already-in-flight race condition specifically.
- Timing-sensitive — hitting the exact window between "request sent" and "response received"
  may take several attempts on a fast connection. Document the number of attempts needed in the
  execution log.
- Relates to TC004 (search offline behavior), TC009 (WiFi to cellular transition).

---

**Automation Coverage:**

None — requires real device network-state manipulation timed against an in-flight request,
not reproducible at the API-mock layer with the timing precision this needs.
