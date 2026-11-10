# Boteco feature-start template

Copy the prompt below into a new Codex chat and replace the three placeholders.

---

Help me develop a real Boteco feature using the revised installed engineering skills.

**Feature:** [Describe the problem, intended users and desired outcome.]
**Project/repository:** [Path or attached project.]
**Known constraints:** [Scope, deadlines, compatibility requirements or “discover with me”.]

Start with read-only discovery. Inspect relevant project instructions, existing behavior, documentation and tests. Separate observed facts, assumptions and unresolved decisions. Ask focused questions where evidence is missing.

**Approval boundary**

Do not implement application code, change dependencies or schemas, run migrations, modify production systems, merge or deploy until the relevant authorization is explicit.

You may prepare requirements and design documents in an isolated feature-planning folder. Preserve existing approved artifacts. Requirements approval authorizes design work only. Begin implementation only after I have approved the exact requirements baseline, HLD and LLD—or justified design exemptions—and explicitly authorized implementation. Never infer approval from silence, passing validators or earlier approvals for another scope.

**Follow these stages and handoffs**

1. **Boteco Requirements Intelligence**
   - Define scope, non-goals, actors and critical journeys.
   - Document functional and measurable non-functional requirements, acceptance criteria, business rules, invariants, exceptions, assumptions and unresolved decisions.
   - Assign stable IDs and trace requirements to their sources and acceptance criteria.
   - Validate clarity, consistency, completeness, feasibility and testability.
   - Produce a business-process diagram and requirements traceability.
   - Present a versioned baseline with content hash, validation findings and pending approval.
   - **Stop for my requirements approval before proceeding to design.**

2. **Builders System Design — HLD**
   - Work from the approved baseline.
   - Define system responsibilities, data ownership, trust boundaries, integrations and failure/recovery behavior.
   - Reuse existing architecture where appropriate; explain material alternatives.
   - Produce architecture and cross-system-flow diagrams.
   - Trace material decisions to approved requirements.
   - **Present the HLD for my approval before completing dependent LLD.**

3. **Builders Software Design — LLD**
   - Reference the exact approved requirements baseline and HLD.
   - Define component responsibilities, interfaces, business-rule ownership, state transitions, transactions, concurrency, retries, idempotency and exceptions as applicable.
   - Produce sequence and state/exception views.
   - Return new system-boundary decisions to HLD review.
   - Apply **Software Design Principles** throughout: reuse existing capabilities, keep changes proportionate and identify expected, potentially affected and protected areas.

4. **Boteco Change Impact & Regression Guard — before implementation**
   - Prepare direct and indirect blast-radius analysis, a protected-behavior register and a risk-based regression plan.
   - Identify trustworthy pre-change evidence, relevant critical journeys and verification gaps.
   - Preserve Regression Protection V2’s capabilities. Reuse relevant V2 evidence without duplicating identical testing or claiming it ran when it did not.
   - Present the LLD, impact map, implementation scope and verification plan together.
   - **Stop for my design approval and explicit implementation authorization.**

5. **After implementation is authorized**
   - Implement within the approved boundary.
   - Use **Testing & Verification** to prove the new behavior meets acceptance criteria.
   - Use the **Guard** to inspect the actual diff, reassess indirect impact, scrutinize test changes and verify previously working behavior.
   - Use **Software Design Principles** to review actual changes against the agreed design.
   - Report executed evidence, failures, skipped checks and limitations separately. Stop when material scope or design changes require renewed approval.

6. **Readiness and delivery**
   - Keep **Production Readiness** independent: assess deployment, configuration, observability, dependencies, migrations, recovery and rollback.
   - Use **CI/CD Delivery Governance** to assemble evidence and check merge/deployment authority.
   - Obtain my explicit approval before merging or deploying. Passing tests or readiness checks do not grant release authority.

**Shared handoff and visual rules**

Every handoff must identify the artifact/version, governing requirements baseline/version/hash, requirement and acceptance-criterion links, scope, assumptions, evidence, limitations, approval evidence and freshness/invalidation state.

Bind the entire HLD and LLD packs to their governing baseline—not only their diagrams. Record design approval separately from structural readiness.

Apply Visual Design Contract VDC-1.1.0: stable diagram IDs, ownership, versions, provenance, traceability and separate syntax, rendering, visual-inspection and consistency results. Record required views as PROVIDED, NOT APPLICABLE with justification, or REQUIRED BUT INCOMPLETE. Never claim checks passed when they were not run.

For material requirements changes, preserve the old baseline and evidence, create a new version, review downstream dependencies, invalidate affected approvals and mark uncertain dependencies stale. Retain unaffected approvals only with documented dependency evidence. Stop affected work until required reapproval is obtained.

Begin by summarizing what you discover, proposing the feature boundary and identifying the questions needed to prepare the first requirements baseline. Do not implement anything yet.
