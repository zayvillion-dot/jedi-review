---
name: overhaul
description: Use when the user is running a live human test-pass (mobile, browser, device) and feeding in findings one at a time while testing continues, invokes /overhaul or says "let's overhaul this," or hands over a raw batch of bug/UX findings from a test round that need triage, cross-cutting root-cause mapping, and delegated fixes before the next live re-test. Not for a single isolated bug report, a first-time build, or steady-state one-off fixes.
---

# Overhaul

## Overview

A live test pass produces findings faster than anyone can fix them; the register is the buffer between the two. Log a finding the instant it lands, keep the human testing, map causes before assigning fixes, and batch reviewed legs into deploys the human can re-test live — instead of alternating "find one, stop, fix one."

## The Contract — run 7 stages, looped per wave

1. **Intake** — The moment a finding arrives, log it into the living register (`references/register-template.md`) inside the session's plan file: number, surface, the finding condensed in the user's own words, severity, status. Do not stop the human's test pass to fix it now — jumping straight to a fix is the single most common failure under momentum pressure, and it is exactly what erases the cross-cutting map stage 2 depends on.
2. **Map** — Before assigning any leg, scan the register for cross-cutting causes: one root that explains several rows (one shell bug can explain five symptoms). Dispatch Explore subagents for file:line evidence on anything not already confirmed. A finding with no confirmed cause doesn't get a fix leg yet — it gets a probe leg.
3. **Plan legs** — Group findings, singly or by shared cause, into legs. Hard/architectural work → Opus; routine work → Sonnet. Before dispatch, the orchestrator runs **5x-think** on any leg introducing a mechanism the codebase doesn't already have and **grill-me** on any leg whose scope is still ambiguous. Build a file-ownership table so no two legs write the same file at the same time — same-file legs are sequenced, and the table names the order — a sequenced leg's worktree is cut only after the leg ahead of it merges.
4. **Execute** — Each leg runs in its own git worktree/branch off one integration branch for the session. Same dev process every leg: TDD, targeted tests only, commit to that leg's own branch, never push from inside a leg. Never run the full suite from a leg worktree — it runs once per batch at stage 6, on the integration branch. An undiagnosed symptom gets a probe shipped before a guessed fix.
5. **Review** — Every leg ends in a **jedi-review** pass (2–3 lenses for a small leg, 5–7 for a large one) before it merges into the integration branch. Confirmed defects go to that project's `LESSONS-DB.md`.
6. **Batch & deploy** — Merge a batch of reviewed legs into the integration branch, run the full suite once there — the batch gate; a red suite blocks this deploy, not the next leg — then push/deploy so the human can re-test live, mid-session. Don't hold every leg hostage to the last one — a batch ships as soon as its legs are gated, and the register keeps running for the next wave. Issue this deploy's stage-7 hand-back items, then loop to stage 1.
7. **Hand back** — Anything left for the human outside the code (console/env/settings, device checks) is delivered per item as **WHAT** it is, **WHERE** to set it, **HOW** (exact steps + the verification signal) — never a prose paragraph mixing several steps.

**REQUIRED SUB-SKILL:** jedi-review for stage 5. **Cross-referenced:** 5x-think (stage 3, new mechanisms only), grill-me (stage 3, ambiguous scope only).

## Quality bar

- Six Sigma defect rate on what ships — the jedi-review gate at stage 5 is how that's held, not a hope.
- Click-speed / time-to-complete, not just correctness: a fix that works but adds a tap or buries information isn't done.
- Simplicity without losing information — condensing a finding or a stats block is not the same as deleting what someone still needs.
- Scope = organization, testing, functionality, and fixes of existing code. **Never mass deletion** — an overhaul repairs a running system, it doesn't gut it.

## Standing rules that travel with every session

- Register updates the moment a finding lands, not in a batch at session end — a memory of "six things he mentioned" is not a register.
- `5x-think` gates any NEW mechanism; it is not required for a fix, a doc, or a rename.
- `grill-me` gates any leg whose scope is still ambiguous after the finding is logged.

## Rationalization table

| Excuse | Reality |
|---|---|
| "It's quick, just fix it now" | Skipping the register loses the cross-cutting map; today's off-register quick fix is tomorrow's untracked regression. |
| "Small enough to skip the worktree" | A shared file between two live legs is exactly how one agent's edit erases another's. |
| "It's cosmetic, skip jedi-review" | Small targets get a small tribunal (2–3 lenses), never zero. |
| "Review the whole batch at the end" | Waiting until the register is empty means every leg's merge conflicts and regressions land at once instead of one leg at a time. |
| "I can already see what's wrong, skip the probe" | A guessed fix that misses becomes a second, harder-to-see defect stacked on the first. |
| "Fold the console steps into one paragraph" | A step buried in prose is a step that gets re-parsed wrong; per-item WHAT/WHERE/HOW is what makes it executable without a follow-up question. |

## Red flags — stop and back up

- Fixed a finding directly instead of logging it into the register first.
- Two legs with write access to the same file at the same time.
- A leg merged into the integration branch without a jedi-review pass.
- A guessed fix shipped for a symptom no explorer confirmed the cause of.
- A new mechanism built without running `5x-think` first.
- Pushed from inside a leg's worktree instead of the integration branch.
- Findings sitting in chat history instead of the register because "I'll add them later."

**All of these mean: stop, log/split/gate before continuing.**

## Report format (batch close-out)

```
Batch 2 — legs: 4 (Opus), 5 (Opus), 6 (Opus), 7 (Opus)
Leg 4 multi-day mover: jedi-review 3 lenses, 0 confirmed → merged
Leg 5 nav anchoring: gated on Leg 3 probe, BLOCKED — probe pending
Leg 6 client form: jedi-review 3 lenses, 1 confirmed (fixed) → merged
Register: 8 open, 5 closed this batch, 2 cross-cutting causes mapped
Deploy: pushed 4/6/7 to main → live; human re-testing
```

Leg dispatch prompt shape: `references/leg-prompt-template.md`. Register/plan-file shape: `references/register-template.md`.
