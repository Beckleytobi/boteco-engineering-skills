# Software Design Artifact Specifications

Create the four artifacts under `docs/software-design/` using the templates in `assets/`. Replace instructional placeholders and preserve unknowns explicitly.

## SOFTWARE_DESIGN_STATE.md

Resumable working memory containing change snapshot, current stage, observed facts, requirements, assumptions, confirmed decisions, open questions, next actions, and change log.

## FEATURE_SOFTWARE_DESIGN.md

The product-to-code design containing behaviour, rules, invariants, current-path evidence, impact map, responsibility map, contracts, state ownership, errors, dependencies, mechanism decisions, compatibility/migration, and verification.

## SOFTWARE_DESIGN_DECISIONS.md

Lightweight design decision log using stable `SDD-NNN` IDs. Each record includes context, evidence, options, decision, consequences, verification, and reconsideration trigger. Keep proposed decisions distinct from builder-confirmed decisions.

## CHANGE_IMPLEMENTATION_PLAN.md

Small, ordered, reviewable slices. Each step states outcome, affected files/modules, dependencies, behaviour preserved/changed, tests/checks, risk, and rollback/recovery. Do not use the plan to smuggle in unrelated cleanup.

## Consistency rules

- Every business rule and invariant has one named owner.
- Every public contract has input, output, failure, side-effect, and compatibility expectations where applicable.
- Every introduced abstraction/pattern/dependency has a mechanism decision and evidence.
- Every affected module appears in the impact map and implementation plan.
- Every implementation slice maps to acceptance or verification evidence.
- Facts from code and intended requirements are labelled separately.
- System-architecture questions are linked to system-design decisions rather than answered implicitly.



## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.

Every pack includes design-handoff.json as specified in [design-handoff.md](design-handoff.md), plus the existing visual coverage/register records. Validate baseline and decision traceability even when diagrams are omitted.
