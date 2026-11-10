# Report template

Use this structure for the final output. The goal is a document a non-technical founder can read top to bottom and come away knowing exactly what to do before launch, what can wait, and why. It should not be a checklist dump where every category gets a paragraph whether or not it's relevant.

```markdown
# Production Readiness Assessment: [what's being assessed]

**Risk tier:** [0/1/2/3] ([one sentence on why, naming the factor that drove it: money, irreversibility, data sensitivity, traffic, etc.])

**Bottom line:** [One or two sentences. Is this safe to ship as-is, safe to ship with the blocking items below fixed first, or not yet, and the single biggest reason why.]

---

## What this covers

[One or two sentences on what was actually assessed: the specific feature/change, not the whole system, unless the whole system is genuinely in scope. Name what was inspected, such as repo paths, config, or existing infra found. If something relevant couldn't be inspected (no access to the actual deploy config, for instance), say so here rather than silently assuming it's fine.]

## Already in good shape

[Short list of what's already handled well. This isn't padding: confirming what's fine is part of the deliverable, and it tells the reader which categories they don't need to think about further. Keep each line to one sentence.]

## Findings

Group findings by the category-playbook group they fall under (only include groups with actual findings; omit empty ones entirely, don't write "N/A"). Within each group, order findings by severity, blocking first.

### [Group name]

**[BLOCKING | SHOULD FIX BEFORE LAUNCH | CAN FOLLOW AFTER LAUNCH]: [short finding title]**

What's true today: [the technical fact, stated plainly]

What that means in practice: [the plain-language consequence. This is the sentence a founder actually needs. Use the "if X, then Y" pattern from the category playbook's consequence framing.]

Fix: [a specific, concrete action, not "add monitoring" but what monitoring, on what, alerting whom. If there's a genuinely reasonable minimal version and a more thorough version, say so in one line rather than picking the maximal option by default.]

[Repeat for each finding.]

## Action plan

A short, ordered list separating what has to happen before this goes live from what can follow shortly after. This is the part most likely to actually get used, so make it stand alone even if nobody reads the findings above it in full.

**Before launch:**
1. [blocking item]
2. [blocking item]

**Soon after launch:**
1. [should-fix item]

**When it becomes relevant:**
1. [lower-priority item, with the condition that would make it matter, e.g. "once traffic crosses X" or "once a second church reports the same issue"]
```

## Notes on filling this in well

- **Severity is a judgment call, own it.** "BLOCKING" should mean you'd genuinely tell the person not to ship until it's addressed. Don't inflate everything to blocking to look thorough, and don't downgrade something that really would hurt a real user just to keep the list short.
- **Every finding needs the plain-language consequence, no exceptions.** If you can't articulate what actually happens to a real person or the business when this goes wrong, you haven't finished thinking about the finding yet. Go back to the category playbook's consequence-framing examples for the pattern.
- **Cut categories that don't apply, and don't narrate the cut.** A report that says "Caching: not applicable, nothing is cached" for six different unused categories reads as padding. Just don't include those sections.
- **Don't let this become a wall of hypotheticals for a Tier 0/1 change.** A short report that says "this is low-stakes, here are the two things worth a quick look, everything else genuinely doesn't apply" is a better outcome than a long one manufacturing findings to fill every group.


## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
