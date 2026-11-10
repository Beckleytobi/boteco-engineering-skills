# Independent forward-test report

## Method

Six independent agents received the skill entrypoint and realistic scenario bundles. They were instructed to read only `SKILL.md` and routed references, avoid the `evals/` directory and expected answers, make no file or external-system changes, and return actual activation, risk, gate, authority, and next-action decisions.

Coverage:

- PR and CI controls;
- migrations and secrets;
- deployment health, concurrency, flakes, and provider failure;
- low-risk proportionality, recovery, hotfixes, and required-check removal;
- activation boundaries;
- cross-skill status handoffs.

## Initial results

- Scenario decisions reviewed: 24
- Safety-critical violations: 0
- Exact/acceptable outcomes without change: 21
- Ambiguities or under-classification requiring refinement: 3

### Finding F1 — health-gate failure versus overall decision

One forward test correctly separated `Post-deploy health: FAIL` from the overall delivery decision, which should be `BLOCKED` pending rollback/recovery. The deterministic evaluator previously returned only overall `FAIL`, making the required next state less explicit.

Refinement: added a two-layer rule and output: failed health gate plus blocked overall delivery, with rollback/recovery as the next safe action.

### Finding F2 — hotfix was marked complete too early

The original deterministic hotfix case returned `PASS` before necessarily post-deploy health checks and monitoring had run. The independent agent returned `PASS WITH CONDITIONS` for the pre-deploy gate and withheld final completion.

Refinement: added an explicit pre-deploy decision stage and a mandatory outstanding condition for health verification and monitoring.

### Finding F3 — stateful production concurrency risk

The original fixture retained user-supplied `MEDIUM` risk for overlapping production deployments against the same database. The independent agent classified the unresolved conflict as `HIGH` because corruption, causality, and recovery are ambiguous.

Refinement: production concurrency conflicts now elevate to `HIGH` unless verified isolation materially reduces the blast radius.

## Post-refinement retest

Three scenarios covering F1–F3 were given to fresh independent agents, again without expected answers.

- Failed critical production health: `Post-deploy health = FAIL`, overall `BLOCKED`, rollback required — PASS
- Governed payment hotfix at pre-deploy: `PASS WITH CONDITIONS`, final completion withheld — PASS
- Concurrent stateful production deploy: `HIGH`, concurrency gate `FAIL`, overall `BLOCKED` — PASS

Post-refinement result: **3/3 passed**.

## Conclusion

The forward tests found no unsafe bypass behavior. The observed issues were status/finality clarity and one risk under-classification in the deterministic model. All three were corrected and independently retested successfully.
