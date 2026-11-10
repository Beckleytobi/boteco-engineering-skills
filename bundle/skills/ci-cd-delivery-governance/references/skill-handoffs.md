# Skill and agent handoffs

Use this reference when coordinating specialized skills or agents.

## Ownership map

| Capability | Owns | CI/CD consumes |
|---|---|---|
| `software-design-principles` — **BUILD WELL** | internal design, responsibility, coupling, maintainability, bounded implementation | design check, actual-diff drift check, regression handoff, evidence-backed status |
| `regression-protection` — **DON'T BREAK** | impacted behavior, contracts, critical journeys, regression-test selection | Regression Evidence artifact, missing coverage, status, confidence |
| `production-readiness` — **OPERATE SAFELY** | configuration, resilience, observability, scalability, failure/recovery readiness | risk tier, blocking findings, before-launch actions, inspection limits |
| CI/CD Delivery & Pipeline Governance — **DELIVER SAFELY** | delivery path, independent evidence, gates, authority, merge, artifact promotion, deployment verification, completion/rollback | all of the above plus CI/platform/deploy evidence |

CI/CD may notice a missing input but should route deep analysis to the owner when available. It must not mark the input `PASS` merely because the other skill is absent.

## Status translation

Keep the sibling's native result in the evidence record and translate only at the delivery gate:

- `PASS` → `PASS` when the evidence is tied to the current change.
- `PASS WITH CONCERNS` → `PASS WITH CONDITIONS` only if each concern is visible, owned, and acceptable for this delivery stage; otherwise `BLOCKED`.
- `FAIL` → `FAIL` and block the next governed action.
- `ESCALATE` → `BLOCKED` until the named human decision or missing evidence resolves it.
- `BLOCKED` → `BLOCKED`.
- A Production Readiness `BLOCKING` finding → `BLOCKED`; “should fix before launch” is not automatically non-blocking—use the report's stated bottom line and consequence.

Production Readiness tiers `0–3` and CI/CD risks `LOW–HIGH` answer different questions. Preserve both instead of pretending there is a one-to-one conversion.

## Handoff envelope

Every handoff should include:

- requirement/change identity;
- repository, branch, PR, and exact commit;
- plain-language change summary and scope exclusions;
- risk classification with reasons;
- affected contracts/data/environments;
- required and completed gates with evidence;
- unresolved findings and their severity/owner;
- artifact/build identity if created;
- requested action and authority required;
- recovery/stop conditions;
- next safe action.

## Independence

The builder may provide implementation evidence, but independent review must come from a distinct reviewer/tool/run where required. Multiple agents repeating the same unsupported claim do not create independent evidence.

When CodeRabbit or another reviewer reports a serious issue, carry the exact finding and resolution evidence forward. When CI reports a check, tie it to the reviewed commit. When Production Readiness sets a release condition, keep it visible through deployment and monitoring.

## Missing skills or unavailable agents

Do not fabricate a handoff. Mark the expected output `UNKNOWN`, explain whether equivalent evidence can be gathered within the current task, and either do so or block/escalate. The user may choose a proportionate alternative; the agent must not silently waive the gate.


## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
