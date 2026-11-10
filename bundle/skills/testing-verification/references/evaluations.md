# Forward Evaluation Record

These scenarios evaluate routing and reasoning, not framework-specific syntax. Each was applied to the operational instructions and checked against an expected invariant.

| # | Scenario | Expected invariant | Observed skill response | Result |
|---|---|---|---|---|
| 1 | Add a pure discount rule with threshold boundaries. | Focused unit tests cover partitions and boundary values; no gratuitous E2E/performance suite. | Risk/strategy routes isolated decision logic to unit tests and boundary analysis, with deeper levels only for a material real boundary. | PASS |
| 2 | Add login with MFA and role-restricted API access. | Unit/integration/API allow-and-deny paths; security judgment handed off. | Workflow derives permission criteria, real-boundary auth tests, negative cases, and records bypass evidence for Security without claiming overall security. | PASS |
| 3 | Fix an off-by-one pagination defect. | Reproduce, failing test, fix, pass, regression handoff. | Bug path explicitly requires failure capture, proof the test detects the bad behaviour, post-fix execution, and test handoff. | PASS |
| 4 | Add a non-null database column migration to a populated table. | Test representative existing data, not only an empty database; coordinate operational safety. | Database guidance separates empty, prior-schema, representative/adversarial data and postchecks, then hands rollout/recovery to Production Readiness and enforcement to CI/CD. | PASS |
| 5 | Add a client form with async submit and accessible errors. | Component/interaction/negative/accessibility coverage; selective browser evidence rather than every possible browser test. | Frontend guidance chooses states, keyboard/focus/error semantics and duplicate/slow response checks, using E2E only for a critical real-browser journey. | PASS |
| 6 | Add an idempotent payment transfer. | High-risk depth across business rule, persistence, API, duplicate/concurrency, provider failure, and critical journey with specialist handoffs. | Risk triggers unit, database/integration, API idempotency, concurrency/failure, selective E2E, Security and Production Readiness handoffs. | PASS |
| 7 | Correct static help text. | Proportionate render/manual confirmation; no load, chaos, MC/DC, database, or full E2E demand. | Low-risk example explicitly permits rendered-content confirmation and rejects unrelated specialized testing. | PASS |
| 8 | Agent loosens `equals(401)` to `isDefined()` after a failure. | Detect likely test weakening and investigate product/test/requirement mismatch. | Execution guidance classifies exact-to-existence changes as suspicious weakening and requires diagnosis before modification. | PASS |
| 9 | Required integration tests cannot start because the service is unavailable. | `BLOCKED` or `INSUFFICIENT EVIDENCE`, never `PASS`. | Verdict rules choose `BLOCKED` for unavailable required dependencies; validator rejects a PASS with material non-pass criteria/run failures. | PASS |
| 10 | Suite reports 100% line coverage but assertions only check non-null results. | Do not equate coverage with correctness; identify weak evidence. | Coverage guidance treats structural coverage as execution only; weak assertions cannot satisfy the PASS rule. | PASS |

## Evaluation limitations

- These are design-time forward evaluations, not executions against ten real application repositories.
- Framework commands, fixtures, platform matrices, coverage thresholds, and environment safety must be discovered per repository.
- The JSON validator checks internal consistency, not whether a test semantically proves its criterion.

## Result

All ten required invariants are represented by explicit operational rules without forcing inappropriate universal test types. The skill is suitable for repository-level use subject to project-specific discovery and authorization.
