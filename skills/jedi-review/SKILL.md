---
name: jedi-review
description: Use when the user says "jedi review", "adversarial review", "tear this apart", "run the tribunal", or hands over a finished deliverable — a code branch/diff, document, plan, spec, or quote — that must meet a zero-escaped-defect standard before it ships, merges, or goes to a counterparty. Also use before declaring any significant piece of work "done".
---

# Jedi Review

## Overview

A review is an attack: findings are claims on trial, every fix is new attack surface. Nothing ships until one full declared-tribunal round confirms zero defects.

Violating the letter of the protocol is violating the spirit of the protocol.

## The Contract — run 6 stages

1. **Scope** — Name target, type, size. Declare lenses from `references/attack-lenses.md`, why (2–3 small, 5–7 large); runs until one clean round. `--deep` adds every deep-mode graft lens.
2. **Attack** — Each lens is a parallel subagent attacking the target. A finding is a one-line claim, exact location, failure scenario, and severity — no scenario, no finding.
3. **Adjudicate** — One fresh skeptic per round, never its attacker, adjudicates every finding. Verdict is binary: CONFIRMED, evidence quoted, or REFUTED, reason quoted — never "worth a look."
4. **Fix re-review** — After fixes land, re-enter: fix rounds run the Fix re-review menu (`references/attack-lenses.md`), scoped to the fixes. A "fixed" comment is a claim, not evidence — fix rounds routinely introduce defects.
5. **Gate** — PASS only when the full declared stage-1 tribunal runs clean against the current state. Report each round's lenses and raised/confirmed/refuted. PASS is a review verdict, not authorization — ship/merge/send stays the user's call. Approving "quick fixes" without stage 4 is a violation.
6. **Ledger** — Append every confirmed defect to `LESSONS-DB.md` at the reviewed project's root (create from `references/ledger-template.md` if absent) every round, not just PASS: defect, root cause, prevention rule. Record recurring "not bugs" decisions.

Edge states — silent/failed lenses, coverage, refuted re-raise, fix-author independence, non-convergence, round composition, unlisted targets — live in `references/tribunal-mechanics.md`.

## Rationalization table

| Excuse | Reality |
|---|---|
| "The author is senior and already reviewed it" | Authority isn't evidence; the tribunal runs on the artifact. |
| "The fixes are one-liners, just ship" | One-line fixes carry the same defect rate; re-review runs. |
| "We're out of time" | The gate is the schedule; a shipped defect costs more. |
| "It's the third revision, everyone's tired" | Fatigue causes escapes; the protocol doesn't tire. |
| "The finding is probably fine, probably intentional" | "Probably" isn't a verdict — adjudicate it. |
| "This target is too small for the tribunal" | Small targets get a small tribunal (2–3 lenses), never zero. |

## Red flags — stop, the protocol has failed

- Acted on an unverified finding.
- A verdict that isn't CONFIRMED or REFUTED.
- Approved shipping on unreviewed fixes.
- A fix reviewed against only its old bug.
- A finding with no failure scenario.
- Declared PASS with any confirmed finding open.
- Skipped the ledger because "we'll remember."

## Report format

```
Round 2 (fix re-review) — lenses: fix-refutation, fix-blast-radius, regression (3)
Raised: 2  Confirmed: 1  Refuted: 1
fix-refutation [FULL] CONFIRMED (high) — discount.py L27: "#12" fix skips premium coupon
fix-blast-radius [FULL] REFUTED — total error (recomputed)
regression [FULL]: 0 raised, attacks recorded
Gate: FAIL — fix, re-enter stage 4.
```
