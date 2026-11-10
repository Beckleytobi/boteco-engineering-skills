# Artifact Specifications

Create the four artifacts under `docs/system-design/`. Use the templates in `assets/` and replace every instructional placeholder. Do not fabricate missing facts.

## 1. SYSTEM_DESIGN_STATE.md

The resumable working memory. Keep it short and current.

Required sections:

- product snapshot and last-updated marker;
- current interview stage;
- known facts with evidence;
- assumptions with confidence, consequence, and validation step;
- decisions with IDs;
- open questions ranked Critical / Important / Later;
- next interview questions;
- change log.

## 2. PRODUCT_SYSTEM_BLUEPRINT.md

The coherent product-specific architecture.

Required sections:

- executive design summary;
- users, actors, critical journeys, and system boundary;
- workload estimates and calculation inputs;
- quality constraints and SLOs where justified;
- domain/data model and ownership;
- identity, authorization, privacy, and trust boundaries;
- context diagram and critical-journey sequence diagram in Mermaid;
- component decision ledger;
- sync/async boundaries and external integrations;
- failure, degradation, recovery, and reconciliation behaviour;
- observability and cost controls;
- risks, unresolved choices, and scaling triggers;
- verification plan.

## 3. ARCHITECTURE_DECISIONS.md

A lightweight decision log. Give each decision a stable `ADR-NNN` identifier.

Each record includes status, context, constraints, options, decision, rationale, consequences, verification, reconsideration trigger, owner, and date. Use `Proposed` until the builder confirms it.

## 4. SYSTEM_BUILD_ROADMAP.md

A phased implementation sequence, not a backlog dump.

Each phase includes:

- demonstrable product outcome;
- user journey enabled;
- included components and relevant ADRs;
- dependencies and data migrations;
- security/reliability work included in the slice;
- acceptance evidence;
- risks and rollback/recovery approach;
- explicitly deferred work and trigger.

The first meaningful phase must create a deployable walking skeleton. The next phases should deliver end-to-end value before scale specialization.

## Consistency rules

- Product numbers and assumptions must match across files.
- Every required component appears in a roadmap phase.
- Every expensive-to-reverse decision has an ADR.
- Every conditional or deferred component has a trigger.
- Every critical journey has an observable success/failure signal.
- Mermaid nodes use product-domain names before vendor names.
- A vendor may be named only after the capability decision is explained.



## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.

Every pack includes design-handoff.json as specified in [design-handoff.md](design-handoff.md), plus the existing visual coverage/register records. Validate baseline and decision traceability even when diagrams are omitted.
