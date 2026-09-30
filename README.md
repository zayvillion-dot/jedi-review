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

Invoke with `/jedi-review`, or say "jedi review," "adversarial review," "tear this apart," or "run the tribunal," and point it at a diff, branch, document, plan, spec, or quote. Add `--deep` to bring in the deep-mode grafts — persona walkthroughs, live end-to-end runs, and A/B against the pre-change state.

## Structure

```
LESSONS-DB.md                     the repo's own review ledger — dogfood
.claude-plugin/
  plugin.json                     plugin manifest
  marketplace.json                marketplace manifest
skills/jedi-review/
  SKILL.md                        the six-stage contract
  references/attack-lenses.md     lens menus by target type: code, docs/plans/specs,
                                   quotes/financial, deep-mode grafts
  references/ledger-template.md   starter template for a target's LESSONS-DB.md
  references/tribunal-mechanics.md  edge-state and independence rules for the tribunal
tests/
  fixture/                        seeded-defect pricing memo + discount module
  ANSWER-KEY.md                   sealed defect list, for scoring only
  red-baseline.md                 the pre-skill baseline run this skill was built against
  green-run.md                    the post-skill re-run confirming all seeded defects
```

## Companion skill: overhaul

`overhaul` encodes a different but related rhythm: a live human test-pass feeding in findings while testing continues, triaged into a running register, mapped for cross-cutting causes, and delegated to Opus/Sonnet fix legs — each of which ends in a `jedi-review` pass before it merges. It now lives in its own repo: https://github.com/zayvillion-dot/overhaul

## Tested

Built RED before GREEN: a generalist single-pass review was run against a seeded-defect fixture under time, authority, and sunk-cost pressure, and the failures it produced are what this skill's six stages are built to close. See `tests/red-baseline.md` for the baseline run, `tests/green-run.md` for the same scenario re-run with the skill applied, and `tests/ANSWER-KEY.md` for the seeded defects the baseline missed or hedged on.

## When to run it — and when not to

This is a milestone gate, not a per-step habit. It is deliberately expensive: every round dispatches parallel subagents (attackers, then a skeptic), and the loop does not stop at "looks good" — it stops at zero confirmed findings or at its own non-convergence valve. Budget accordingly.

- **Run it** when a piece of work is *finished by its author's own standard* and is about to ship, merge, or go to a counterparty: a feature branch before merge, a quote or contract before it leaves the building, a plan before you commit resources to it, a skill or spec before you publish it.
- **Don't run it** on work in progress, on every commit, or as a substitute for tests. The tribunal reviews finished claims; half-built work just generates findings you already knew about.
- **Expect real cost.** A small document is a few subagent runs. A large codebase at 5–7 lenses, with fix re-review rounds and full-tribunal gate rounds, can run for hours — and on a big enough target with a strict bar, days. That precision is the point: the zero-confirmed-defect gate is a Six Sigma posture, and you pay for sigma in rounds.
- **The stops are a feature.** When the non-convergence rule fires, the review isn't broken — it's telling you the fix *approach* is minting new defects, and handing the call to a human. Answer the question it asks; don't just re-run it.
- **Scale the tribunal to the target.** Two or three lenses for a small memo; the full bench for a launch. The lens menus and sizing rules are in `skills/jedi-review/references/attack-lenses.md`.
- **Keep the ledger.** The `LESSONS-DB.md` it maintains in each target repo is where the compounding value lives — every confirmed defect leaves behind the prevention rule it taught, and reviewers consult it before similar work.

## Origin story

The skill's first real target was itself, and the review took fourteen rounds to pass. Its own tribunal confirmed 56 defects in this package — including defects in the protocol's own constitution: a phantom lens its example cited before any menu defined it, an escape hatch its rationalization table explicitly forbids, a fallback rule that would have let a fix's author grade its own fix, and a safety-valve counter blind to the exact thrash loop it guarded against. The non-convergence rule fired twice and stopped the review both times for a human decision rather than rubber-stamping its author; the counter rule, one round after being written, caught its own author's miscount. Gate round one confirmed eight findings, gate round two confirmed two, and gate round three ran clean — PASS at zero confirmed findings, every lens filing its attack record. The full round-by-round record lives in this repo's own `LESSONS-DB.md`. The gate does not have a "good enough" exit, even for the skill that defines it.

## License

MIT — see `LICENSE`.
