# Wave / batch runbook

Mechanics for stage 3 (waves) and stage 6 (batch & deploy) — the parts too procedural to keep inline in `SKILL.md`. Worked shapes below are patterns, not literal scripts to copy verbatim; adapt the commands to the target repo's own test entrypoint and deploy tooling.

## Wave dispatch

1. Build the wave's file-ownership table (`register-template.md`) before writing a single leg-dispatch prompt.
2. Cap: **≤5 concurrently running subagents, session-wide** — count every subagent holding a session-scoped role at once (leg builders, dispatched jedi-review lenses/skeptics, the merge-collision lens), not per-wave and not builders alone. A wave that would push the session total past 5 splits: the overflow legs queue for the next wave. This is the one definition of the cap; `SKILL.md` and `register-template.md` reference it rather than restating a number.
3. A leg sequenced behind another same-file leg is not dispatched (no worktree cut) until the leg ahead of it merges into the integration branch. Cutting the worktree early is the same defect as writing the file early — it just hides until merge time.
4. Every leg dispatch cites its wave and its ownership-table row.

## Pre-flight (run before every batch gate, not just the first)

Check all five before launching a full-suite run on the integration branch:

- **Clean tree:** the main working copy has no uncommitted changes.
- **In sync:** `git log origin/main..main` is empty — local `main` is not ahead of the remote in a way this gate doesn't know about.
- **Integration ⊇ origin/main:** `git merge-base --is-ancestor origin/main <integration-tip>` is true. `main == origin/main` only checks the local `main` branch — it says nothing about the integration tip that is about to be gated and pushed. If this check is false, merge the missing commits into the integration branch, re-run the merge-collision lens on anything they touched, and re-check before gating.
- **No push in flight:** nothing else is mid-push to `origin/main` right now.
- **No foreign suite:** `pgrep -f <the project's suite entrypoint>` (e.g. `run_all.py`) comes back empty — a second session's own test run can silently race or kill this one.

If any check fails, resolve it — do not launch the gate speculatively "to see what happens." "Resolve" means: wait for it to clear, merge in what's missing, or name the other session in the register as a ticket. It never means pushing or resetting another session's work: **an unpushed local `main` you did not create is not yours to push or reset** — even when it fails the "in sync" check — wait for that session's own push, then merge `origin/main` in as usual.

## One gate, on the final tip

- If `origin/main` (or any other integration branch this one must reconcile with) moves while a wave is running, merge the new tip into the integration branch before gating. Run the merge-collision lens (`merge-collision-lens.md`) on every file the merge touched from both sides.
- Never run two full-suite gates against two different tips of the same branch in the same window — the older one's result is meaningless the moment the branch moves again. Kill it (or let it die) and gate the new tip instead.
- A push to `origin/main` starting while your gate is still running is the same case one step earlier: your gate's tip is already stale the moment that push starts, not only once it lands. Kill your gate rather than let it finish, then run pre-flight again once the push completes.
- A gate that returns rc 143 (SIGTERM) or rc 137 (SIGKILL) was killed by something external (a foreign suite starting, a session restart, a manual interrupt) — it is not a red run. Re-launch the gate by going back through the full pre-flight checklist above, not by relaunching it directly — whatever killed it may still be true; do not read the signal itself as a test failure.
- A gate that returns a real nonzero rc with named failing tests is red. No further leg merges into the integration branch until it's green again. The fix is its own leg: diagnosed, jedi-reviewed, and merged, then the gate re-runs from the top — never a direct patch on the integration branch.
- A green gate's push can still be refused at push time (a pre-push hook or CI check failing on the push itself). That refusal is a second gate, not a green deploy: diagnose it, fix it as its own leg, jedi-review it, merge it, then re-run the batch gate from the top before pushing again. Never treat a push refusal as the rc 143/137 case, and never push past it with `--no-verify` or equivalent.

## Deploy

1. Green gate on the final tip → the batch is ready. This is a review verdict, not a ship decision.
2. Name the human authorization the deploy rests on — a standing session-level go ("proceed with everything") or an explicit go for this specific batch. Write which one in the batch close-out.
3. Push/deploy via the project's own deploy tooling; capture its log.
4. Verify the live site/app reflects the change (a version marker, a specific page, a specific behavior) — a deploy with no visible change (e.g. no static asset touched) needs its own verification method; don't rely on a build-id stamp that this batch never actually moved.
5. Issue the batch's stage-7 hand-back (WHAT/WHERE/HOW), naming any item that belongs to a different concurrently running session as a ticket to that session, not a hand-back to the human.
6. Remove the leg worktrees once merged and deployed; keep the branches unless the user says otherwise.

## Worked batch close-out

```
Pre-flight: main clean, main==origin/main, integration ⊇ origin/main, no foreign suite (pgrep clean), no push in flight
Merge-collision lens: base.html × Leg 2 + Leg 5 — exact-union both directions, MERGE CLEAN
Gate #1 on <tip-a>: KILLED rc 143 (foreign suite started) — not red, re-launching
origin/main moved <tip-a> → <tip-b> mid-gate: merged, re-ran merge-collision lens, re-gating <tip-b>
Gate #2 on <tip-b>: rc 0 — 142 PASS / 0 FAIL
Deploy: pushed <tip-b> to origin/main (authorized: standing session go) — live verify: <specific page/behavior> confirmed
```
