# Benchmark Analysis and Differentiation

This is a maintainer reference. It records the patterns borrowed, the gaps avoided, and the distinctive contract of Builders System Design as of 2026-08-31.

## Compared skills

| Existing skill | Strong pattern | Limitation for Builders Academy's goal |
|---|---|---|
| [Dwsy/agent system-design](https://github.com/Dwsy/agent/blob/main/skills/system-design/SKILL.md) | Requirements-first EventStorming flow, Mermaid diagrams, no silent assumptions | Optimized for producing a design catalog; not an adaptive novice-owned product roadmap |
| [alonbaron/claude-skills architect](https://github.com/alonbaron/claude-skills/blob/main/skills/architect/SKILL.md) | Source-of-truth documents, invariants, failure paths, architecture roadmap | Opinionated expert workflow and house-document structure; little learning-by-decision support |
| [wondelai design-code-architecture](https://github.com/wondelai/skills/blob/main/design-code-architecture/SKILL.md) | Resumable phases and emphasis on expensive-to-reverse decisions | Orchestrates a large skill ecosystem and assumes mature architecture practice |
| [MLSystemDesign skill](https://github.com/ML-SystemDesign/MLSystemDesign/blob/main/skills/README.md) | Evidence-based, stage-aware review for ML systems | Review-oriented and AI/ML-specific rather than general product discovery-to-roadmap |
| [at7211 system-design-skill](https://github.com/at7211/system-design-skill) | Clear interview-style phases and visual artifacts | Optimized for system-design interview performance, not sustained product building |
| [pinchen147 system-design-skill](https://github.com/pinchen147/system-design-skill) | Evidence over vibes, repository recovery, resumability, multiple synchronized outputs | Strong expert recommendation/audit orientation; less emphasis on beginner ownership and component exclusion triggers |
| Local `artifact-template-system-design` | Consistent system-design document templates | Formats an artifact but does not conduct product clarification or decide architecture |

## Builders System Design's distinct role

This skill is not:

- the Builders Academy teaching/content-generation system;
- a generic architecture report generator;
- a coding agent that immediately implements a stack;
- a system-design interview simulator;
- a tool that rewards maximum infrastructure.

It is a persistent decision environment carried by each builder into a real product. Its distinctive mechanisms are:

1. **Incomplete idea to design:** it can begin with non-technical product language.
2. **Adaptive interview:** it asks a small number of questions, branches, and explains consequences.
3. **Builder ownership:** the AI proposes; the builder confirms expensive choices.
4. **Evidence classes:** facts, assumptions, decisions, and questions cannot silently blend.
5. **Component admission control:** each component must be required, deferred, conditional, or excluded.
6. **Trigger ledger:** future scale architecture is attached to measurements, not aspiration.
7. **Minimum viable architecture:** simplicity is an explicit design result.
8. **Failure-first completion:** recovery, permissions, observability, and verification are required.
9. **Vertical-slice roadmap:** architecture becomes an ordered product-building path.
10. **Resumability:** the state survives sessions, model changes, and changing requirements.

## Portable packaging decision

The shared core uses the Agent Skills directory convention: a directory containing `SKILL.md`, with optional `references/`, `assets/`, and `scripts/`. Claude Code can discover the skill from `.claude/skills/builders-system-design/`. Codex can use the same directory from its skills location; `agents/openai.yaml` adds Codex presentation metadata without changing the core instructions.

Maintain a single source package. Copy or link that package into each platform-specific discovery location instead of maintaining separate behavioral prompts.

## Evaluation scenarios

Test the skill on at least these product shapes:

1. local appointment marketplace with a first-time founder;
2. multi-tenant B2B workflow product with sensitive records;
3. flash-sale commerce workload with a large peak;
4. media-heavy global public site where CDN may be justified;
5. AI research assistant using private documents and tools;
6. internal CRUD tool where queues, microservices, and vector search should be excluded;
7. existing repository with partially completed architecture documents;
8. requirement change that invalidates one ADR but not the entire design.

Score question relevance, unsupported assumptions, component justification, builder comprehension, artifact consistency, failure coverage, roadmap buildability, and appropriate restraint.

