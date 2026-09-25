---
name: overhaul
description: Use when the user is running a live human test-pass (mobile, browser, device) and feeding in findings one at a time while testing continues, invokes /overhaul or says "let's overhaul this," or hands over a raw batch of bug/UX findings from a test round that need triage, cross-cutting root-cause mapping, and delegated fixes before the next live re-test. Not for a single isolated bug report, a first-time build, or steady-state one-off fixes.
---

# Overhaul

## Overview

A live test pass produces findings faster than anyone can fix them; the register is the buffer between the two. Log a finding the instant it lands, keep the human testing, map causes before assigning fixes, and batch reviewed legs into deploys the human can re-test live — instead of alternating "find one, stop, fix one."

**REQUIRED SUB-SKILL:** jedi-review for stage 5 — this skill does not restate jedi-review's contract, gate, or non-convergence rule; it cites them. **Cross-referenced:** 5x-think (stage 3, new mechanisms only), grill-me (stage 3, ambiguous scope only).

## The Contract — run 7 stages, looped per wave

### 1. Intake

- Log every finding the instant it arrives into the register (`references/register-template.md`), inside the session's plan file.
- Do not fix it now. Fixing on the spot erases the cross-cutting map stage 2 depends on.
- Before dispatching any new wave, check the trunk's own hook/CI status is not already red — a red trunk absorbs every new push silently; note it as a blocking finding instead of building on top of it.

### 2. Map

- Scan the register for one root cause explaining several rows before assigning any leg.
- Dispatch Explore subagents for file:line evidence on anything not already confirmed.
- A finding with no confirmed cause gets a probe leg, never a guessed fix leg.

### 3. Plan legs — waves and ownership

- Group findings, singly or by shared cause, into legs. Hard/architectural work → Opus; routine work → Sonnet.
- Run `5x-think` before dispatch on any leg introducing a mechanism the codebase doesn't already have.
- Run `grill-me` before dispatch on any leg whose scope is still ambiguous.
- A **wave** is the set of legs dispatched to run concurrently.
- Cap a wave at 5 concurrently running legs.
- Every leg in a wave owns a disjoint file set — no two concurrently running legs may write the same file.
- Build the wave's file-ownership table (`references/register-template.md`) before dispatching a single leg in it.
- When two legs must touch the same file, sequence them in the table with "then" and name the order; the later leg's worktree is cut only after the earlier leg merges.
- When another concurrent session (a different agent thread, not this wave) owns work in the same repo, name its tickets after that session in the register rather than dispatching a leg that collides with it.
- Each leg's dispatch is written on the `references/leg-prompt-template.md` shape — it is the contract that keeps single-owner files, the no-push rule, and the gate record from being renegotiated mid-leg.

### 4. Execute

- Each leg runs in its own git worktree, on its own branch, cut off one integration branch for the session.
- Branch names are flat: `session/<name>-<leg-slug>`, cut from `session/<name>` — never nested (`session/<name>/<leg-slug>` fails: git refuses a ref nested under an existing branch ref).
- TDD: write the test, watch it fail, then fix.
- Targeted tests only. A leg never runs the full suite from its own worktree — full-suite runs happen exactly once per batch, at stage 6, on the integration branch. State this categorically; do not soften it with a parenthetical exception.
- Before adding prose into a template or comment shared with any test's substring assertions, grep `tests/` for that literal text — a comment can accidentally satisfy or break a page-wide string check.
- A browser/UI test run against an isolated or seeded database must assert it actually reached the target page, not merely that it ran without error — a forged or misrouted session that silently bounces to a login page can pass every assertion vacuously.
- An undiagnosed symptom ships a probe, never a guessed fix.
- Commit to the leg's own branch. Never push from inside a leg's worktree, and never merge the leg yourself.
- If the leg's cause turns out unconfirmed once inside the code, stop and ship a probe instead of guessing.
- If a fix keeps landing on one door of a multi-door mechanism (e.g. one delete path, one send path) and missing its sibling, the leg's tests must enumerate every door, not just the one that was reported.

### 5. Review

- Every leg ends in a jedi-review pass before it can merge into the integration branch — see jedi-review's Contract (stage 1 Scope for lens count, stage 5 Gate for the PASS bar). A clean fix round is not itself a PASS; jedi-review's own stage 5 defines what is.
- Confirmed defects go to that project's `LESSONS-DB.md` every round jedi-review runs, per jedi-review's stage 6.
- Non-convergence stop: jedi-review's tribunal-mechanics defines the trigger (three confirming rounds, counted from the review's start or the user's last authorization; clean rounds between them do not reset the count) — this skill does not redefine it. On a stop, hand the user exactly three options: **(a) scoped pass** — fix only the survivors and re-run a scoped fix-pair, not a fresh full round; **(b) narrower ship** — cut the leg down to what already passed and park the rest as a new row; **(c) park** — leave the leg open and move on. Default when the third round's confirmed findings are all Low severity: **scoped pass + fix-pair only**, stated to the user as the recommendation, not silently taken.
- PASS on a leg authorizes merging that leg into the integration branch. It does not authorize the batch deploy at stage 6 — that is a separate, later authorization.

### 6. Batch & deploy

- A **batch** is the set of jedi-review-gated legs merged into the integration branch together for one deploy.
- Ship a batch as soon as its own legs are gated; don't hold it for a slower parallel leg in another wave — that leg joins the next batch. Exception: a leg sequenced behind an unmerged same-file leg always waits for that merge, gated or not.
- Merge every gated leg into the integration branch. On every file two legs (or a leg and a moving `origin/main`) both touched, run the merge-collision lens (`references/merge-collision-lens.md`) — an exact-union proof, both directions, that no line either side wrote was lost, before trusting the merge.
- Before running the batch gate, pre-flight: the main working tree is clean, `main == origin/main` (`git log origin/main..main` empty), no push is currently in flight, and no foreign test process is already running (`pgrep -f run_all.py` or the project's suite entrypoint) — another session's suite can silently absorb or collide with this one.
- Run the full suite exactly once, on the integration branch's final tip — never launch two gates against two different tips, and never gate a tip that is about to move. If `origin/main` moves again before the gate finishes, merge the new tip in, re-run the merge-collision lens on anything it touched, and gate the new tip instead — one gate, on the final tip, always.
- A killed gate (rc 143/137, or any signal-terminated run) is not a red run — it means something external killed it (a foreign suite starting, a session restart). Re-launch; do not read it as a failure.
- A red suite blocks this deploy — no further legs merge into a red integration branch. It does not block other legs from continuing to build in their own worktrees. The fix for the red suite is itself a leg: diagnosed, fixed, jedi-reviewed, and merged before the gate re-runs; never patched directly on the integration branch.
- Green gate → push/deploy, naming the human authorization it rests on (a standing session authorization such as "proceed with everything," or an explicit go for this specific deploy) — a green gate is a review verdict, not by itself a decision to ship.
- Issue this deploy's stage-7 hand-back items, then loop to stage 1 for the next wave.

### 7. Hand back

- Anything left for the human outside the code (console/env/settings, device checks) is delivered per item as **WHAT** it is, **WHERE** to set it, **HOW** (exact steps + the verification signal) — never a prose paragraph mixing several steps.
- Any item that belongs to a different, concurrently running session is named as a ticket addressed to that session by name, not folded into this session's hand-back.

## Quality bar

- Six Sigma defect rate on what ships — the jedi-review gate at stage 5 is how that's held, not a hope.
- Click-speed / time-to-complete, not just correctness: a fix that works but adds a tap or buries information isn't done.
- Simplicity without losing information — condensing a finding or a stats block is not the same as deleting what someone still needs.
- Scope = organization, testing, functionality, and fixes of existing code. **Never mass deletion** — an overhaul repairs a running system, it doesn't gut it.
- When a reviewed sentence turns out false, delete it — never rewrite it smaller and leave a shrunken false claim standing.

## Rationalization table

| Excuse | Reality |
|---|---|
| "It's quick, just fix it now" | Skipping the register loses the cross-cutting map; today's off-register quick fix is tomorrow's untracked regression. |
| "Small enough to skip the worktree" | A shared file between two live legs is exactly how one agent's edit erases another's. |
| "It's cosmetic, skip jedi-review" | Small targets get a small tribunal (2–3 lenses), never zero. |
| "Review the whole batch at the end" | Waiting until the register is empty means every leg's merge conflicts and regressions land at once instead of one leg at a time. |
| "I can already see what's wrong, skip the probe" | A guessed fix that misses becomes a second, harder-to-see defect stacked on the first. |
| "Fold the console steps into one paragraph" | A step buried in prose is a step that gets re-parsed wrong; per-item WHAT/WHERE/HOW is what makes it executable without a follow-up question. |
| "The gate came back red/killed, just re-run it" without checking why | rc 143/137 really is safe to re-run; any other red is a leg of its own, diagnosed before the next gate. |
| "It's just a comment, it can say anything" | A comment sharing a file with a substring test can silently satisfy or break that test. |
| "One more leg fits in this wave" | The builder cap (≤5 concurrent, disjoint files) is what keeps a wave reviewable; a sixth leg is next wave's problem, not this one's. |

## Red flags — stop and back up

- Fixed a finding directly instead of logging it into the register first.
- Two concurrently running legs with write access to the same file.
- A leg merged into the integration branch without a jedi-review PASS.
- A guessed fix shipped for a symptom no explorer confirmed the cause of.
- A new mechanism built without running `5x-think` first.
- Pushed, or merged a leg, from inside a leg's own worktree instead of the integration branch.
- Findings sitting in chat history instead of the register because "I'll add them later."
- Two gates launched against two different tips of the same integration branch.
- A batch gate launched without checking for a foreign suite or an in-flight push first.
- A merge across an auto-mergeable shared file with no merge-collision lens run against it.

**All of these mean: stop, log/split/gate before continuing.**

## Report format (batch close-out)

```
Batch 2 — legs: 4 (Opus), 5 (Opus), 6 (Opus), 7 (Opus)
Leg 4 multi-day mover: jedi-review 3 lenses, 0 confirmed → merged
Leg 5 nav anchoring: gated on Leg 3 probe, BLOCKED — probe pending
Leg 6 client form: jedi-review 3 lenses, 1 confirmed (fixed) → merged
Merge-collision lens: 2 shared files, exact-union proof both directions, MERGE CLEAN
Pre-flight: main clean, main==origin/main, no foreign suite, no push in flight
Gate: <tip sha> full suite rc 0 — 142/0
Register: 8 open, 5 closed this batch, 2 cross-cutting causes mapped
Deploy: pushed 4/6/7 to main (authorized: standing session go) → live; human re-testing
```

Leg dispatch prompt shape: `references/leg-prompt-template.md`. Register/plan-file shape: `references/register-template.md`. Wave/batch mechanics worked through in full: `references/wave-batch-runbook.md`. Merge-collision lens brief: `references/merge-collision-lens.md`.
