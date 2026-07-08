# Testability Feedback Notes

Based on current execution of test cases and review of app behavior:

- 🔸 **Search field accepts empty input**  
  No validation or warning is shown to prevent an empty search. This makes it hard to confirm if the app is working or simply idle (UX issue).  

- 🔸 **Download action has no visual feedback**  
  Tapping the download icon gives no progress indicator, toast, or confirmation. It's unclear if the action was successful, making it hard to validate manually.

- 🔸 **Offline behavior is not clearly handled**  
  When the network is disabled, search fails silently or inconsistently. There is no retry strategy, timeout message, or loading indicator for poor connectivity.

---

These issues affect manual test reliability and suggest areas for improving app observability and testability.
