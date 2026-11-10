# Boteco Engineering Skills — FR4 Claude-tested-r1 local review candidate

Prepared 10 November 2026. A portable copy of eight revised engineering skills and the independent Regression Protection V2 companion. No installation occurs when you extract this ZIP.

## Start here

1. Extract the archive into an ordinary folder outside any agent's skill-discovery directories.
2. Read [verification and compatibility](VERIFICATION.md) and [provenance and sharing status](PROVENANCE.md).
3. Run `python -B verify_bundle.py` from this folder to check the contents.
4. Follow either [Codex setup](guides/CODEX.md) or [Claude Code setup](guides/CLAUDE-CODE.md). Avoid duplicate or conflicting installed copies.
5. Copy [the feature-start prompt](feature-start-template.md) into a new agent chat, replace its three placeholders and begin with read-only discovery.

## Contents and responsibilities

| Folder under skills/ | Responsibility |
|---|---|
| boteco-requirements-intelligence | Validated, versioned requirements and controlled change |
| builders-system-design | HLD: system responsibilities, boundaries and architecture |
| builders-software-design | LLD: components, interfaces, state and exceptions |
| software-design-principles | Proportionate design and review of actual changes |
| boteco-change-impact-regression-guard | Impact planning, protected behavior and regression verification |
| testing-verification | Evidence that new behavior meets requirements |
| production-readiness | Independent operational readiness |
| ci-cd-delivery-governance | Delivery evidence, authority and release gates |
| regression-protection | Unchanged V2 companion regression workflow |

The Guard retains the V2 regression capabilities and adds explicit pre-change planning and baseline-aware handoffs. Use the Guard to coordinate the end-to-end workflow; do not duplicate identical test runs merely to obtain a second report. Production Readiness remains independent.

## Approval gates

Requirements approval permits design work only. Obtain HLD approval before completing dependent LLD. Implementation waits for approved requirements and designs (or justified exemptions) AND explicit implementation authorization. Merge and deployment require explicit authority. A material change triggers dependency review and reapproval of affected artifacts. Passing structural validators does not authenticate approval or prove product correctness.

The prompt contains the complete gates and Visual Design Contract requirements. Skill instructions guide the agent; they are not a technical permission system. Keep the host's approval controls enabled.

This release contains no .system skills, host configuration, credentials, installation backups, private execution logs or automatic installer. The original evaluated skill bytes are preserved. Three explicitly guided Claude Code CLI trials passed; automatic routing and Claude Desktop remain untested. See [trial results](trial-results/README.md).

## License

MIT, copyright 2026 Tobi Beckley. See [LICENSE](LICENSE) and [attribution](ATTRIBUTION.md).
