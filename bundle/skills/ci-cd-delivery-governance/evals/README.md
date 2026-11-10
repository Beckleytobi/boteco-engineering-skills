# Behavioral evaluation suite

These cases test decisions and prohibited outcomes rather than phrase matching. Each narrative scenario is converted into a structured evidence record, evaluated by the same deterministic consistency checker available to skill users, and compared with safety-critical expectations.

Run:

```text
python evals/run_behavioral_evals.py
```

The suite covers normal PR flow, failed tests/regression/coverage, unsafe attempts to obtain green CI, serious independent-review findings, migration risk, secret exposure, low-risk proportionality, failed post-deploy health, concurrency, flakes, provider failure, recovery, required-check removal, missing secrets, hotfix governance, a negative activation case, and status translation from sibling skills.

The harness verifies policy consistency, not natural-language quality, provider state, or real infrastructure enforcement. Use independent forward-testing with an agent/runtime when authorized and available.

`FORWARD_TEST_REPORT.md` records the completed blind agent runs, observed ambiguities, refinements, and focused retest results.
