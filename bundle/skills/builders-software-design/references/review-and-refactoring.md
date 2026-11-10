# Review and Refactoring Workflow

Use this for design reviews, code-smell investigations, and behaviour-preserving refactors.

## Establish review scope

Identify the requested files, feature path, diff, or risk. Review surrounding callers and tests only as needed to understand impact. Do not expand a targeted review into a repository rewrite.

## Review order

Review in this order so surface style does not distract from correctness:

1. required behaviour and invariants;
2. data/state ownership and authorization/integrity boundaries;
3. responsibility and dependency structure;
4. contracts, side effects, failures, and compatibility;
5. tests and verification gaps;
6. simplicity, readability, naming, and local organization;
7. patterns, abstractions, and dependencies.

## Evidence-backed findings

Each finding must include:

- exact code evidence and affected behaviour;
- why it creates a defect, change risk, or comprehension burden;
- smallest safe improvement;
- tests or evidence needed before and after;
- consequence of leaving it unchanged;
- severity based on impact, not aesthetic preference.

Do not report personal style differences that are consistent with the repository and create no material risk.

## Code-smell routing

| Smell | Ask first | Possible small refactor |
|---|---|---|
| Giant function/module | Which responsibilities and reasons to change are mixed? | Extract cohesive rule or side-effect boundary |
| Deep nesting | Can guard clauses or explicit state transitions clarify behaviour? | Simplify control flow |
| Long parameter list | Are parameters one concept or hidden state/dependency? | Parameter object/value object only if cohesive |
| Duplicated business conditional | Is the same knowledge represented, and can cases diverge? | Centralize rule owner |
| Primitive obsession | Does a value have validation, units, identity, or operations? | Introduce value type where it protects invariants |
| Feature envy | Which capability owns the rule and data? | Move behaviour toward owner |
| Shotgun surgery | What missing boundary makes one change spread? | Create narrow seam around actual change axis |
| Circular dependency | Which direction reflects policy versus detail? | Move contract/ownership or extract stable capability |
| Boolean flags | Are several behaviours hidden in one operation? | Explicit operation/strategy when variants are real |
| Dead code/speculative abstraction | What current caller or requirement needs it? | Delete with verification |

## Safe refactoring sequence

1. Capture current observable behaviour with characterization tests when coverage is insufficient.
2. Make one structural change without intended behaviour change.
3. Run targeted checks and inspect the diff.
4. Repeat in small steps.
5. Add the new behaviour only after the needed seam exists.
6. Remove obsolete paths and update documentation after adoption is verified.

Refactoring and behaviour change may occur in one overall task but keep their commits or review steps distinguishable when practical.

## Completion report

Report:

- design health summary;
- findings ranked by behavioural/change risk;
- strengths worth preserving;
- recommended minimal refactor sequence;
- verification evidence obtained and still missing;
- larger redesigns deliberately deferred.



## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
