# Visual Design Contract VDC-1.1.0

This is the canonical shared contract. Each standalone skill bundles an identical copy. Specialist instructions define ownership; this contract defines representation and evidence.

## Sources and identity

Every diagram has a stable DGM identifier, purpose, semantic version, owner, design level, source path and source hash. Bind it to exact requirements baseline ID/version/hash and governing design decisions. Reference CHG, REQ (including existing FR/NFR/EXC aliases), AC, CJ, INV, DEC (including ADR/SDD aliases), RSK and EVD identifiers. Preserve existing IDs rather than renumbering them. Components and relationships require stable IDs and source references; a node's existence does not prove an edge.

## Ownership and levels

REQUIREMENTS: actors, business processes, journeys, logical context and traceability. No invented implementation technology.
HLD: system and component responsibilities, cross-system interactions, data flow, integrations, trust boundaries, justified deployment and resilience decisions.
LLD: behaviour inside approved HLD components, detailed sequences, functions, branches, state transitions, database interactions, transactions, retries, timeouts, idempotency and exceptions. Any new system boundary returns to HLD review.
IMPACT: direct/indirect dependencies, blast radius, affected/protected areas, journeys and contract changes derived independently from the actual diff where available.
OPERATIONS: observed deployment, critical dependencies, failure and recovery overlays. Findings route architecture changes to System Design and release decisions to CI/CD.

## Representation

Prefer Mermaid flowchart, sequenceDiagram, stateDiagram-v2 and erDiagram. Use separately labelled current and proposed views. Preserve unknowns. Label VERIFIED, PROPOSED, ASSUMED, POTENTIAL, UNKNOWN and PROTECTED explicitly; colour alone is insufficient. Include a legend when states differ. A protected component may still be potentially affected; represent both facts.

Use DOT for dense dependency graphs, BPMN for required formal process semantics, or an existing project notation when Mermaid cannot faithfully express the relationship. Record the reason and parser version. Do not introduce a renderer dependency without checking existing tools.

## Source and output

Keep one canonical source-controlled diagram per Markdown file with metadata and a plain-language description. Optional SVG/PNG derivatives record the source hash and renderer version. Prefer the project's existing documentation layout; otherwise use docs/<discipline>/diagrams/. No secrets, personal records, scripts or remote resources in render outputs. Do not upload private diagrams to public rendering services.

## Validation

Record metadata, traceability, syntax, rendering, visual inspection and specification consistency separately as PASS, FAIL or NOT RUN, with evidence and tool version. Missing tools never imply PASS. Parse and render when tooling permits. Inspect clipping, text size, contrast, edge directions, labels, legends, abstraction level and crossings. Split dense views by purpose. A syntactically valid diagram is not proof of technical truth or tested behaviour.

## Versioning and approval

Keep lifecycle (draft/approved/superseded), evidence state and freshness separate. Approvals bind exact artifact hashes and baseline versions. Hash only the immutable content payload; store approval evidence outside that payload to avoid circular hashes.

Material requirements or architecture changes trigger transitive dependency review across HLD, LLD, impact maps, verification evidence and operational findings. Preserve old evidence. Mark known affected approvals INVALIDATED and uncertain dependencies STALE; require reapproval before consumption as current. Preserve unaffected approval only with dependency evidence. Editorial changes require recorded equivalence review. Updating an image does not renew approval.

## Handoff envelope

Include diagram_id, version, purpose, owner_skill, design_level, source_hash, baseline identity, governing artifact versions, requirement/decision/component/evidence IDs, node and edge provenance, assumptions, unknowns, validation records, rendered-output hash/source hash, approval evidence and invalidation dependencies/reason/action. Each consumer verifies compatibility and freshness; incompatible contract versions block the affected handoff.

## Proportionality

Produce views that clarify material relationships. Do not require the entire catalogue for a trivial change. State why a necessary view cannot be produced. No diagram or approval grants execution, deployment or release authority.

## Coverage register (VDC-1.1.0)

Before claiming visual completion, create visual-coverage.json with owner_skill and views. Each view has a stable view name and status PROVIDED, NOT APPLICABLE or REQUIRED BUT INCOMPLETE. PROVIDED lists diagram_ids that exist in diagram-records. NOT APPLICABLE records reason, scope and evidence. REQUIRED BUT INCOMPLETE records the reason or blocking condition and prevents visual completion. A single diagram may satisfy several views when its purpose and content support them; no duplicate artwork is required.

Assess at least these ownership-specific views: Requirements Intelligence — business_process, requirements_traceability; System Design — architecture, cross_system_flow; Software Design — sequence, state_and_exceptions; Guard — blast_radius, protected_behaviours; Production Readiness — deployment_and_recovery. Add further views when the change warrants them. Every supplied diagram belongs in the register. The reviewer checks that the declared inventory covers the real scope; a validator cannot infer every missing relationship.

Design Principles, Testing & Verification and CI/CD consume the specialist owner's register without taking over authorship. If they create a separate consumption register, list the required views or use an empty views list with none_reason. Do not change operational, testing or release responsibilities.

When every view is legitimately omitted, retain visual-not-applicable.json (reason, scope, evidence) AND record the individual coverage decisions. Existing records without coverage remain historical; add a reviewed coverage record before a new visual-completion claim. No rerender is required merely to document unchanged coverage. Declare VDC-1.1.0 when producing new handoffs; do not silently reinterpret older contract versions.
