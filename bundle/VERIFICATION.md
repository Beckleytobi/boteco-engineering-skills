# Verification and compatibility

## Original FR4 packaging evidence

- Nine skill folders; 136 skill files match installed sources byte for byte (126 FR4 files plus 10 preserved Regression Protection V2 files).
- 34 skill Python sources parsed successfully; 206 relative Markdown links inside skill folders resolve.
- 12/12 recorded canary validator checks repeated using packaged helpers: normal feature, justified diagram omission, material-change draft, and expected rejection of stale/current or unapproved/ready claims. These use the original isolated fixtures, not a new agent session. Fixture inputs are not included in the public-facing payload.
- Both installed skill roots, including .system, match their complete pre-packaging content snapshots. No installation, activation, upload or publication was performed.
- Feature-start template preserved byte for byte. Approval gates in every skill preserved by exact-content comparison.
- ZIP integrity and extracted-file identity are checked after archive creation; the external PACKAGE-VERIFICATION.json records those final results.

## Prior evidence, not rerun as part of packaging

FR4 evaluation recorded 156 primary and 58 additional expected outcomes, with the existing CI suite included within the additional checks; these are not independent statistical samples. The subsequent limited Codex canary covered a normal feature, justified omission and material change. Installation on 9 November 2026 passed 43/43 checks. The managed .system drift observed during the earlier canary was separately investigated; it did not alter these candidate files. No private raw logs are included here.

## Compatibility limits

Codex: prior evaluated instructions, isolated canary and installed-validator evidence; packaging does not certify every host version or automatic invocation.

Claude Code: three explicitly guided CLI trials passed on version 2.1.148 with claude-sonnet-4-6. See trial-results/README.md for scope, independent checks and limitations. Automatic invocation, slash discovery, Claude Desktop, Claude.ai, Cowork and other hosts are not certified.

Python: this run used 3.14.0. Validators rely on standard-library and bundled modules; no external renderer is bundled. Mermaid syntax/rendering and visual inspection still require evidence in each real design pack. No diagram rendering was performed by this packaging task.

Integrity hashes detect accidental content changes; they are not a publisher signature or proof that requirements and approval evidence are true. The manifest does not hash itself; the adjacent ZIP checksum covers the complete archive.

## Claude-tested-r1 documentation update

All 136 skill files, the feature-start template and Codex guide remain byte-identical to the original bundle. Updated setup and compatibility statements; added portable results and synthetic before/after test fixtures. Packaging verification replays the five documented local test commands, parses Python sources, verifies the file manifest and checks every ZIP member against its source. This is not a new Claude run or a new skill evaluation. See the external PACKAGE-VERIFICATION.json for observed packaging results.
