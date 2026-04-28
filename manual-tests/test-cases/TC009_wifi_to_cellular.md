# TC009 – WiFi to Cellular network transition

**User Story:** US004 – Network Connectivity  
**ISTQB Design Technique:** State Transition Testing  
**Priority:** Medium  
**Platform:** Both (Android / iOS)  
**Test Type:** Performance / Functional

---

**Objective:**  
Verify that the app continues to function without crashing or data loss when the
device switches from WiFi to mobile data (and back) during active use.

**State Diagram:**

```
[WiFi Active] ──── disable WiFi ───► [Cellular Active] ──── disable cellular ───► [Offline]
      ▲                                       │
      └────────── re-enable WiFi ─────────────┘
```

**Preconditions:**  
- Physical device with an active SIM (cellular data enabled) **or** network-condition
  simulation tool (e.g., Android Emulator network settings / iOS Network Link Conditioner).  
- App is installed and running; internet connectivity is active (WiFi).

---

**Test Steps:**

| # | Action | Expected Outcome | Pass/Fail |
|---|---|---|---|
| 1 | With WiFi active, search for `computer vision` | Results load normally | |
| 2 | While results are displayed, disable WiFi (leave cellular on) | App detects the transition; either reloads with cellular data or shows a brief connectivity-change indicator | |
| 3 | Perform a new search for `robotics` | Results load via cellular; no crash | |
| 4 | Open a paper detail view and tap **Download PDF** | Download starts or completes over cellular | |
| 5 | Re-enable WiFi while the download is in progress (or after) | App does not duplicate the download or throw an error | |
| 6 | Disable both WiFi and cellular data | App enters offline state; shows appropriate message on new search attempt | |
| 7 | Re-enable WiFi | App recovers; previously shown results are accessible | |

---

**Expected Result:**  
- Transitions between network states do not cause crashes, data corruption, or UI freezes.  
- In-progress downloads survive a network switch without producing a corrupt file.  
- Offline state (step 6) shows a user-facing message, consistent with TC004 behaviour.

**Notes:**  
- On Android, use **Settings → Network & internet** or `adb shell svc wifi disable` to toggle.  
- On iOS Simulator, use **Additional Tools for Xcode → Network Link Conditioner** to simulate
  cellular or packet-loss conditions.  
- Document the exact network type used during testing (4G LTE / 5G / WiFi 6) in the
  execution log.
