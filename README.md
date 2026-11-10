# Boteco Engineering Skills

A coordinated engineering workflow for requirements, HLD, LLD, implementation verification and controlled delivery, usable with Codex and Claude Code.

**FR4 Claude-tested licensed-r1.** Public repository: `Beckleytobi/boteco-engineering-skills`. Fork this repository to adapt the skills under the MIT license.

## Download and start

Download the Boteco ZIP and SHA256SUMS.txt from the [release page](https://github.com/Beckleytobi/boteco-engineering-skills/releases/tag/fr4-claude-tested-licensed-r1). GitHub's automatic source archive contains the full repository; the curated Boteco ZIP contains just the portable bundle.

1. Extract the curated ZIP outside agent skill-discovery folders.
2. Run `python -B verify_bundle.py` inside it.
3. Follow the [Codex setup guide](bundle/guides/CODEX.md) or [tested Claude Code setup guide](bundle/guides/CLAUDE-CODE.md).
4. Start a feature with the [reusable template](bundle/feature-start-template.md).

For a repository clone, the portable package is in `bundle/`; run `python -B bundle/verify_bundle.py`. Copy complete skill folders only after reviewing existing names and scope. Extraction does not install or activate anything.

## Skills and handoffs

| Skill | Responsibility |
|---|---|
| Requirements Intelligence | Requirements, measurable criteria, baseline versions and controlled scope changes |
| Builders System Design | HLD: boundaries, architecture and system decisions |
| Builders Software Design | LLD: components, contracts, state and exception paths |
| Software Design Principles | Proportionate design and review |
| Change Impact & Regression Guard | Direct/indirect impact, protected behaviours and approval invalidation |
| Testing & Verification | Evidence that new requirements work |
| Regression Protection V2 | Evidence that existing behaviour still works; separately preserved |
| Production Readiness | Independent operational readiness |
| CI/CD Delivery Governance | Delivery evidence, release authority and gates |

Approve requirements, then HLD and LLD or justified exemptions. Implementation needs explicit authority. Material changes invalidate affected approvals and mark uncertain dependencies stale. Merge, deployment and publication remain separate gates. Skills guide behaviour; host permissions and independent evidence remain necessary.

## Tested scope

The recorded Claude Code CLI trial used version 2.1.148 and claude-sonnet-4-6: cancellation suite 20 passed, nine independent acceptance checks passed, label suite two passed, and material change correctly stopped. See [results and reproducible fixtures](bundle/trial-results/README.md) and [compatibility limits](bundle/VERIFICATION.md).

Automatic routing, Claude Desktop, native READY promotion in the positive cases and production readiness were not established. Codex evidence is documented separately. This is not a universal host certification.

## License and provenance

MIT license, copyright 2026 Tobi Beckley. Retain the [license](LICENSE) copyright and permission notice in copies or substantial portions. See [attribution](ATTRIBUTION.md) and the [licensing review](LICENSING-REVIEW.md). Codex and Claude Code names indicate compatibility targets; no affiliation or endorsement is claimed.

## Release review

[Draft release notes](RELEASE-NOTES.md) · [publication plan](PUBLISHING-PLAN.md). No automatic publishing workflow or installer is included.
