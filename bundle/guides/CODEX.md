# Codex setup

Scope: manual setup on a different machine or an intentionally selected project. The machine used to prepare this bundle already has the revised skills installed; it does not need reinstallation.

## 1. Verify and check existing skills

Extract outside skill-discovery locations, open a terminal in the extracted bundle and run:

```text
python -B verify_bundle.py
```

Use a working Python 3 interpreter; Windows may use `py -3` instead of `python`. Packaged validators use standard-library and bundled local modules; no pip install is required by this bundle. Python 3.14 was used for the recorded checks; older versions are not certified. Mermaid rendering is separate: use an available renderer and record its version, or mark rendering NOT RUN.

Inspect existing project and user skills before copying. If a same-named skill exists, stop and compare versions; back it up outside skill-discovery directories before an explicitly approved replacement. Do not overwrite or merge folders blindly. Check older `.codex/skills` installations as well to avoid duplicates. Never replace `.system`.

## 2. Choose one installation scope

Current Codex documentation lists project `.agents/skills/` and user `~/.agents/skills/`. Choose one scope for this bundle:

- Project: copy each complete folder inside this bundle's `skills/` into `<your-project>/.agents/skills/`.
- Personal: copy each complete folder into `~/.agents/skills/` (`%USERPROFILE%\.agents\skills` on Windows).

For example, the resulting project path is `.agents/skills/boteco-requirements-intelligence/SKILL.md`. Do not add an extra `skills/skills/` nesting level. Keep references, assets, scripts and agents metadata with their skill. Regression Protection V2 stays in its own folder; if an identical V2 copy already exists, retain it. Production Readiness also stays separate.

Do not relocate a working existing installation just to match this guide. The original validated machine used a mixture of legacy `.codex/skills` and `.agents/skills` paths. This guide's current documented layout has not been live-tested by this packaging task.

## 3. Confirm discovery without implementing a feature

Start a fresh chat/session in the selected project and inspect the available skills. Explicitly select Boteco Requirements Intelligence if needed. Ask the agent to identify the loaded skill and its approval gates, with no application edits. Missing skills or name conflicts must be resolved before relying on the workflow.

Paste `feature-start-template.md`, fill in feature, repository and constraints, and retain every approval gate. Do not approve implementation while the requirements or governing designs remain pending.

## 4. Validation and recovery

Resolve helper paths from the actual installed skill folder, not from your project's current directory. For example:

```text
python -B <skill-folder>/scripts/validate_requirements_baseline.py <baseline.json>
```

The HLD and LLD entry points are `validate_system_design_pack.py <pack-directory>` and `validate_software_design_pack.py <pack-directory>` in their respective skill folders. Use a fresh non-production project for the acceptance scenarios in `ACCEPTANCE-TRIALS.md`.

To undo a newly added installation, remove only the exact folders you added after checking their resolved paths. For an approved replacement, restore the entire original folder from your backup, ensuring newer extra files do not remain. No recovery is performed by this bundle.

Source checked 10 November 2026: [OpenAI local skill locations](https://learn.chatgpt.com/docs/build-skills). Host behavior may vary by version and organization policy.
