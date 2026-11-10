# System Design Review Gates

Use these gates for an existing or newly produced design. Report `Pass`, `Partial`, `Fail`, or `Not applicable`, with evidence. A polished diagram is not evidence.

## Gate 1 — Product clarity

- Primary user and problem are explicit.
- Critical journeys have success and failure outcomes.
- Current stage and fixed constraints are distinguished from aspirations.

## Gate 2 — Quantitative clarity

- Launch and growth workload ranges are visible.
- Peak, geography, data growth, and largest operations are considered.
- Calculations expose inputs and assumptions.

## Gate 3 — Data and authorization integrity

- Core entities have owners and lifecycle rules.
- Source-of-truth and consistency requirements are explicit.
- Tenant/resource authorization is enforced server-side and testable.
- Sensitive data, retention, deletion, audit, and secrets are addressed.

## Gate 4 — Component justification

- Every component solves a named product problem.
- The design includes the minimum useful form.
- Deferred, conditional, and excluded components have reasons and triggers.
- Vendor selection follows capability/constraint reasoning.

## Gate 5 — Failure and recovery

- Timeouts, retries, idempotency, duplicate work, and partial failure are addressed where relevant.
- External service outage behaviour is defined.
- Data backup and restore are testable.
- User-visible degraded behaviour is explicit.

## Gate 6 — Operability and cost

- Critical journeys map to logs, metrics, traces, or audit events.
- Alerts have an owner and a user-impact reason.
- Variable cost drivers and budget controls are visible.
- The architecture fits the team's operational capacity.

## Gate 7 — Roadmap readiness

- The roadmap delivers vertical slices.
- Security and reliability are embedded rather than postponed wholesale.
- Acceptance evidence is measurable.
- Speculative scaling work is behind triggers.

## Decision outcome

- `Ready`: no failed gates and no unresolved critical question.
- `Ready with tracked assumptions`: only partial items with owners, validation dates, and bounded consequences.
- `Not ready`: any critical journey, trust boundary, data ownership, or expensive irreversible choice remains undefined.

End the review with the three highest-leverage next actions, not an undifferentiated issue list.



## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
