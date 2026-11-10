# Adaptive Feature Design Workflow

Use this workflow for new behaviour or a significant change. It is a branching interview, not a fixed questionnaire.

## Interview behaviour

- Inspect the code and product/system documents before asking the builder.
- Ask 3–5 questions per round and explain briefly why an answer changes the design.
- Accept product language; translate it into software constraints without requiring jargon.
- Record unknowns as assumptions with consequence and a validation step.
- Show the builder the inferred rules and boundaries for correction.

## Round A — Behaviour and value

Establish:

- actor and triggering event;
- observable successful outcome;
- business rules and forbidden outcomes;
- what happens when prerequisites are missing;
- what is explicitly outside this change;
- acceptance examples in concrete terms.

Do not discuss class or folder structure until the required behaviour is coherent.

## Round B — Invariants and ownership

Ask or discover:

- facts that must always remain true;
- which entity/capability owns each rule;
- source of truth for each mutable fact;
- who may perform each transition;
- uniqueness, ordering, concurrency, and transaction expectations;
- audit or history requirements.

Prefer statements such as “an accepted booking cannot overlap another accepted booking for the same tutor” over generic “validate bookings.”

## Round C — Current path and change pressure

Trace:

- entry point and callers;
- current modules/functions/classes involved;
- reads, writes, external calls, and emitted events;
- tests that protect the path;
- known defects or repeated changes;
- the actual axis likely to vary.

Distinguish a stable rule from a coincidental current implementation.

## Round D — Boundaries and contracts

Define only the seams needed by the behaviour:

- capability/module responsibilities;
- public contract and visibility;
- domain rule location;
- orchestration and side-effect boundaries;
- state ownership and allowed transitions;
- error categories and propagation;
- dependency direction;
- compatibility and migration.

When multiple options are viable, compare them using change impact, understandability, testability, integrity, framework fit, and operational cost.

## Round E — Verification and rollout

For each rule and risk decide:

- evidence before implementation;
- unit/domain, integration, contract, or end-to-end checks as appropriate;
- static/type/lint/build checks;
- migration/backfill or feature-flag needs;
- runtime signal or manual review;
- rollback/recovery if the change fails.

## Branching signals

| Signal | Investigate next | Do not assume |
|---|---|---|
| Business rule appears in UI, API, and worker | One rule owner and multiple adapters/callers | A shared utility is always the right owner |
| Same conditional repeated with likely divergence | Duplicated knowledge and rule ownership | Every repeated line must be abstracted |
| Module changes for unrelated reasons | Split responsibilities around domain change axes | One class per method or one folder per layer |
| Many callers know internal data shape | Stable contract or encapsulation seam | Interface for every implementation |
| External call mixed with rules | Separate deterministic decision from side effect if it improves testing/recovery | Full clean architecture rewrite |
| Mutable state mirrored in several places | Source of truth, derived state, synchronization | Global state library by default |
| Expected failures use exceptions inconsistently | Error taxonomy, ownership, user outcome | Catch every error locally |
| New provider/library requested | Adapter boundary and dependency evaluation | A provider-neutral abstraction before a second provider exists |
| Legacy code has weak tests | Characterization tests and small seams | Rewrite before change |
| Security rule appears in client code | Server-side enforcement and negative tests | UI restriction is authorization |

## Confirmation summary

Before finalizing, present:

1. required behaviour and invariants;
2. current-path evidence;
3. proposed responsibilities and contracts;
4. abstractions/patterns/dependencies introduced and rejected;
5. impact and failure risks;
6. verification and small-change plan;
7. open decisions requiring builder confirmation.



## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
