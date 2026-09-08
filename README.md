# Jedi Review

An adversarial review tribunal for Claude Code: parallel hostile attack lenses, findings put on trial before anyone acts on them, and fixes re-attacked as new attack surface — with a gate that opens only at zero confirmed defects.

## The doctrine

1. **Scope** — Name the target and declare which attack lenses run, and why that count.
2. **Attack** — Each lens runs as a parallel subagent with one job: break the target and produce a concrete failure scenario, not an impression.
3. **Adjudicate** — A fresh, non-attacking subagent tries to refute every finding. Verdicts are binary: CONFIRMED or REFUTED.
4. **Fix re-review** — Once fixes land, re-attack them: try to refute the fix claim, and attack the fix's new state for defects it introduced.
5. **Gate** — Pass only when one full round, every declared lens, returns zero confirmed findings.
6. **Ledger** — Append every confirmed defect, its root cause, and the prevention rule it taught to `LESSONS-DB.md`.

## Why

Most reviews stop at a single generalist pass: one pair of eyes, one read-through, findings reported as-is. Two mechanics are usually missing, and both matter more than the review itself:

- **Findings are adversarially verified before anyone acts on them.** A finding is a claim, not a fact, until a skeptic who didn't raise it tries to knock it down and fails.
- **Fixes are re-attacked as new attack surface.** A comment claiming a bug is fixed is a claim on trial, not evidence — the fix gets the same hostility the original code did.

On top of that, the gate only opens at zero confirmed findings — there is no "ship after quick fixes" exit — and every confirmed defect gets written to a ledger, so the same mistake has to be relearned in writing before it can be relearned in production.

## Install

**As a plugin:**

```
/plugin marketplace add zayvillion-dot/jedi-review
/plugin install jedi-review@jedi-review
```

**Manual:**

Copy `skills/jedi-review/` into `~/.claude/skills/`.

## Usage

Invoke with `/jedi-review`, or say "jedi review," "adversarial review," "tear this apart," or "run the tribunal," and point it at a diff, branch, document, plan, spec, or quote. Add `--deep` to bring in persona walkthroughs and live end-to-end runs alongside the standard lenses.

## Structure

```
skills/jedi-review/
  SKILL.md                        the six-stage contract
  references/attack-lenses.md     lens menus by target type: code, docs/plans/specs,
                                   quotes/financial, deep-mode grafts
  references/ledger-template.md   starter template for a target's LESSONS-DB.md
tests/
  fixture/                        seeded-defect pricing memo + discount module
  ANSWER-KEY.md                   sealed defect list, for scoring only
  red-baseline.md                 the pre-skill baseline run this skill was built against
```

## Tested

Built RED before GREEN: a generalist single-pass review was run against a seeded-defect fixture under time, authority, and sunk-cost pressure, and the failures it produced are what this skill's six stages are built to close. See `tests/red-baseline.md` for the baseline run and `tests/ANSWER-KEY.md` for the seeded defects it missed or hedged on.

## License

MIT — see `LICENSE`.
