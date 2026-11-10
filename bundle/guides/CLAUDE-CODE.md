# Claude Code setup — isolated CLI trial tested

FR4 documentation revision Claude-tested-r1, 10 November 2026. Skill contents are unchanged. Three explicitly guided local CLI trials passed with Claude Code 2.1.148, claude-sonnet-4-6, medium effort and Python 3.14.0 on Windows. See [results](../trial-results/README.md). Automatic skill selection, slash-menu discovery, Claude Desktop, Cowork and other hosts were not established by these trials.

## Verify and prepare a separate project

Extract outside skill-discovery locations. From the extracted bundle run:

```text
python -B verify_bundle.py
```

Create an empty, disposable project. Inspect existing project and personal skill names before copying. Copy the nine complete folders under this bundle's `skills/` into `<trial-project>/.claude/skills/`. Example: `.claude/skills/boteco-requirements-intelligence/SKILL.md`, with its references and scripts. If a destination already exists, stop and review it; do not overwrite it. Backups belong outside discovery folders. Do not change global skills, .system, CLAUDE.md, hooks or personal settings.

Project scope was tested. Personal `~/.claude/skills/` is documented by Claude but was not the installation scope tested here. Keep Regression Protection V2 as its own folder and Production Readiness independent. Codex's agents/openai.yaml metadata is retained; the trial did not rely on Claude consuming it. No installer is included.

## Check the CLI login

In your own terminal run `claude --version` and `claude auth status`. If needed, run `claude auth login` and complete sign-in. The open desktop app did not provide CLI authentication in this trial; verify the CLI separately. Never put login tokens in project files, prompts or the bundle.

Start `claude` from the disposable project. Explicitly ask it to read `.claude/skills/boteco-requirements-intelligence/SKILL.md` and the relevant design, Guard, verification and regression manifests. Check actual reads rather than inferring selection from a plausible answer. `/boteco-requirements-intelligence` is a documented invocation option, but slash invocation was not tested in the recorded runs.

## Preserve the approval sequence

Use [the unchanged feature-start template](../feature-start-template.md); its opening host reference can be adapted to Claude Code. Begin with discovery and requirements, then approve the version/hash-bound requirements, HLD, LLD and justified omissions. Implementation needs separate explicit authority. Delivery and publication remain separate approvals.

The recorded implementation trial used an approval-evidence overlay bound to the immutable review manifest. It did not silently rewrite DRAFT records as APPROVED. Positive-case native READY metadata promotion was not tested. In a new project, use your real approval evidence and the skill's handoff contract; this bundle supplies no transferable product approval. Material changes require reassessment and fresh affected approvals.

## Execution profile used in the trial

The evaluator ran separate `claude -p` sessions, supplied prompts on stdin and captured stream-json output. Recorded options included `--output-format stream-json --verbose --no-session-persistence --setting-sources project --strict-mcp-config --no-chrome --permission-mode dontAsk --model claude-sonnet-4-6 --effort medium`. The process used a trial-local settings file disabling hooks and automatic memory, an empty MCP configuration, tools Read/Edit/Write/Bash, and an allowed-tools list for Read/Edit/Write and `Bash(python -B *)`.

This is a recorded evaluation profile, not an automatic setup script or an OS sandbox. Keep interactive permission prompts for normal work. Do not use bypass-permissions flags or loosen controls to make a trial pass. Those tools and allow rules do not independently guarantee filesystem confinement; the evaluator used an isolated project, explicit scope instructions and before/after hashes. Claude model calls use the authenticated service; no artifact upload or publication workflow was performed.

Resolve validator paths relative to the owning skill, not the current project directory. On Windows, prefer exact native Read paths and portable `python -B` test commands. Do not mix PowerShell syntax with Claude's Bash tool or end a Bash-quoted Windows path with a backslash. If directory search fails, directly read the known reference before reporting it missing. Denied commands remain denied; report unavailable checks or have the evaluator execute them under existing authorization.

Run [acceptance scenarios](ACCEPTANCE-TRIALS.md) in each intended environment. For the recorded fixture scope, cancellation, repeat stock release, identity denials, copied results and later hold/collect behaviour were checked; concurrency, rollback and production authentication were not. Rendering and visual inspection are separate required evidence when diagrams apply.

Official references checked 10 November 2026: [skill locations and invocation](https://code.claude.com/docs/en/skills) and [CLI commands/options](https://code.claude.com/docs/en/cli-reference). Current documentation can describe versions newer than the tested CLI; verify flags with your installed CLI's help.
