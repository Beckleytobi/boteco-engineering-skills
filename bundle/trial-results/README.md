# Recorded Claude Code trial results

PASS within the approved synthetic fixture scope, 10 November 2026. Claude Code CLI 2.1.148 / claude-sonnet-4-6 / medium effort / Python 3.14.0 / Windows. One successful run per scenario; no claim of universal compatibility or production readiness.

| Scenario | Independent evidence |
|---|---|
| Normal cancellation | 20 suite tests passed: 6 original + 14 additive. Nine additional acceptance test methods passed. Original methods and tests preserved. |
| Label and justified omission | Two tests passed: one original + one additive exact-value test. Only the constant and additive test changed. |
| Material change | Correct STOP; v2 remains NEEDS DECISION / APPROVAL REQUIRED. LLD-CANCEL-v1 and EVD-REG-v1 INVALIDATED; HELP-UNKNOWN and LOCAL-BOUNDARY-v1 STALE. No scenario code changed. |

The pending baseline was structurally valid; DRAFT handoff accepted; READY rejected because an approved governing baseline was required. This is a successful negative test, not approval to implement cancellation after collection.

The evaluator independently executed the suites and reviewed actual diffs, original method ASTs, criterion links and file hashes. The 14 Claude-authored cancellation tests first failed because cancel was absent. The independent suite likewise detected the absent feature on the original fixture. No passing result was achieved by weakening original tests. Guard coordinated direct/indirect scope; Regression Protection V2 supplied existing-behaviour safeguards; operational readiness remained independent.

Seven diagrams had been rendered and visually inspected before user approval of the requirements, HLD, LLD and omissions. Those private review records and the user's approval message are not redistributed. Their approval does not authorize another user's implementation.

## Reproduce the code checks without an agent

From this bundle's root, run:

```text
python -B -m unittest discover -s trial-results/fixtures/before/normal -v
python -B -m unittest discover -s trial-results/fixtures/before/omission -v
python -B -m unittest discover -s trial-results/fixtures/after/normal -v
python -B -m unittest discover -s trial-results/fixtures/after/omission -v
python -B trial-results/independent_cancel_checks.py trial-results/fixtures/after/normal
```

Expected counts: 6, 1, 20, 2 and 9 passing test methods respectively. Optional negative control: point independent_cancel_checks.py at fixtures/before/normal; expect a nonzero exit because cancel is absent. Subtest errors are not additional test methods. These commands replay the code checks; they do not rerun Claude or the private approval-gate fixtures.

## Boundaries and tooling observations

CLI success does not establish automatic routing, slash-menu discovery or Claude Desktop integration. Positive approval was a version/hash-bound overlay on immutable drafts; native READY promotion was not tested. The material test does exercise rejection of unapproved READY. No real authentication, persistence, concurrency, rollback, production load, deployment or operational readiness was tested.

Directory-list attempts encountered a denied command and Windows/Bash quoting errors; a mkdir command was denied. The runs recovered with native file tools and existing directories without loosening settings. Raw execution logs remain local and are not bundled.

[Machine-readable results](results.json) retain observed test outputs and material statuses. Portable before/after fixtures are synthetic; no credentials, personal paths, account identifiers or conversation transcripts are included. Installed skill hashes were unchanged after the trial. Production Readiness remains independent.
