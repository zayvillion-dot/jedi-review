---
name: jedi-review
description: Use when the user says "jedi review", "adversarial review", "tear this apart", "run the tribunal", or hands over a finished deliverable — a code branch/diff, document, plan, spec, or quote — that must meet a zero-escaped-defect standard before it ships, merges, or goes to a counterparty. Also use before declaring any significant piece of work "done".
---

# Jedi Review

## Overview

A review is an attack: findings are claims on trial, and every fix is new attack surface. Nothing ships until one full declared-tribunal round confirms zero defects.

Violating the letter of the protocol is violating the spirit of the protocol.

## The Contract — run all 6 stages

1. **Scope** — Name the target, type (code/doc/plan/spec/quote), size. Declare the tribunal: lenses from `references/attack-lenses.md`, why (2–3 small, 5–7 large); runs until one clean round. `--deep` adds persona walkthroughs and live end-to-end runs.
2. **Attack** — Each lens runs as a parallel subagent to break the target. A finding IS a one-line claim, exact location, a concrete failure scenario (input/reading/sequence causing harm), and severity. No scenario, no finding.
3. **Adjudicate** — A fresh, non-attacking skeptic subagent tries to REFUTE each finding. Verdict is binary: CONFIRMED, evidence quoted, or REFUTED, reason quoted — never "worth a look." Only confirmed findings proceed; "most attacks failed, N confirmed" is legitimate.
4. **Fix re-review** — After fixes land outside this skill, re-enter and re-attack each fix: refute that claim, and attack its new state for fix-introduced defects. A "fixed" comment is a claim on trial, not evidence — fix rounds routinely introduce new defects.
5. **Gate** — PASS only when one full round, all lenses, yields zero confirmed findings. Report lenses × rounds and raised/confirmed/refuted. Open findings mean no pass; approving "after quick fixes" without re-entering stage 4 is a violation, not a shortcut.
6. **Ledger** — Append every confirmed defect to `LESSONS-DB.md` at the target's root (create from `references/ledger-template.md` if absent): defect, root cause, prevention rule. Record recurring "not bugs — do not fix" decisions in its table.

## Rationalization table

| Excuse | Reality |
|---|---|
| "The author is senior and already reviewed it" | Authority isn't evidence; the tribunal runs on the artifact. |
| "The fixes are one-liners, just ship" | One-line fixes carry the same defect rate; re-review runs. |
| "We're out of time" | The gate is the schedule; a shipped defect costs more. |
| "It's the third revision, everyone's tired" | Fatigue causes escapes. The protocol doesn't get tired. |
| "The finding is probably fine, probably intentional" | "Probably" isn't a verdict — adjudicate: CONFIRMED or REFUTED. |
| "This target is too small for the tribunal" | Small targets get a small tribunal (2 lenses), never zero. |

## Red flags — stop, the protocol has failed

- Acted on an unverified finding.
- A verdict that isn't CONFIRMED or REFUTED.
- Approved shipping on unreviewed fixes.
- A fix reviewed against its old bug, not its new state.
- A finding with no failure scenario.
- Declared PASS with any confirmed finding open.
- Skipped the ledger because "we'll remember."

## Report format

```
Round 2 (fix re-review) — lenses: fix-refutation, regression (2)
Raised: 2  Confirmed: 1  Refuted: 1
CONFIRMED — discount.py L27: "#12" fix skips premium coupon
REFUTED — claimed total error (recomputed)
Gate: FAIL — fix, then re-enter stage 4.
```
