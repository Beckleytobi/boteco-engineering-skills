# Change impact guard

## Pre-change mode

Use the approved requirements baseline, acceptance criteria, exception scenarios, non-functional constraints, critical journeys, invariants, and proposed design boundary as inputs. If the baseline is not approved, continue only as a clearly labelled draft analysis and do not imply downstream authorization.

Produce:

1. direct impact: behaviour intentionally changing;
2. indirect impact: callers, consumers, contracts, data, events, configuration, integrations, and journeys reached through shared dependencies;
3. protected behaviour: existing outcomes and invariants that must remain true;
4. change boundary: expected, may-change, and protected areas;
5. prospective regression risk and uncertainty;
6. required evidence by direct, dependency, contract, critical-journey, and broader-suite level;
7. approval and stop conditions before implementation.

Do not claim a module, consumer, or journey is affected without evidence or a clearly labelled inference. Dynamic dispatch, configuration wiring, runtime integration, and missing architecture documentation reduce confidence and may justify an explicit discovery task.

## Boundary approval

For low-risk, contained changes, the user's implementation request may already supply sufficient authority. Do not create redundant ceremony. Seek a new decision when the analysis reveals a materially wider blast radius, public contract change, migration, security boundary, new infrastructure, irreversible operation, or protected behaviour not covered by the approved request.

Approval is recorded against the exact requirements baseline and impact-map version. It does not authorize release.

## Post-change drift

Compare the actual diff with the approved boundary:

- expected changes require normal verification;
- may-change areas require evidence for why they were touched;
- protected areas touched by the diff raise scrutiny immediately;
- unplanned contracts, dependencies, schema changes, test weakening, or unrelated refactors require explanation and may invalidate the plan.

Recalculate the surface from the actual diff. Never force the evidence to fit the pre-change plan when implementation changed the dependency graph.

## Material requirement change

A requirement change is material when it can alter design, implementation, verification, risk, user outcome, exception behaviour, non-functional thresholds, compatibility, data handling, or a prior decision. On material change:

1. consume the new baseline identity and its changed dependency IDs;
2. find impact maps, plans, evidence, tests, and approvals based on the superseded version;
3. mark directly affected artifacts `INVALIDATED` and uncertain dependents `STALE`;
4. recalculate only what the dependency graph shows may have changed, widening when traceability is incomplete;
5. issue a new plan and obtain reapproval where required.

Editorial changes retain approval only when meaning, scope, thresholds, exceptions, and traceability are unchanged and the classification is recorded.


## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
