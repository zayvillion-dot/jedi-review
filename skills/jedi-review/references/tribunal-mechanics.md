# Tribunal Mechanics

Edge-state and independence rules for running the Jedi Review tribunal. This supplements `SKILL.md`'s six-stage contract — it doesn't replace any of it.

## Adjudication cardinality

One fresh skeptic subagent per round adjudicates all of that round's findings; the skeptic is never one of the round's attackers.

## Round composition

Round 1 = the full declared tribunal. Fix rounds = the Fix re-review menu (see `attack-lenses.md`) plus regression when the target is code, scoped to the fixes and their blast radius. The gate round = the full declared stage-1 tribunal re-run against the current state; when it confirms zero findings, PASS. A clean fix round alone never passes the gate.

## Lens accountability

Every lens reports its strongest failed attacks alongside its findings. A lens returning zero findings and no attack record did not run — the round is incomplete.

## Lens failure states

A lens that cannot dispatch runs serially, or in-line by the orchestrator as last resort. A lens that errored or never returned is reported DID NOT RUN; a round containing one cannot reach the gate.

## Coverage

Each lens declares coverage: FULL, or PARTIAL plus what it read. PARTIAL coverage on any lens blocks PASS until the uncovered remainder has been attacked.

## Refuted findings

An attacker may re-raise a REFUTED finding once, only with new evidence the skeptic didn't consider. A second refutation is final for the review.

## Fix-author independence

Stage-4 attackers and skeptic are never the fix's author and are not briefed by the author beyond the fix's stated claim ("what it fixes, where").

## Non-convergence

After three consecutive fix rounds that each confirm new defects, stop. Report the pattern to the user and question the fix approach itself before burning a fourth round.

## Interruption and standing state

The ledger is appended as each round's adjudication closes, not only at PASS — an interrupted review keeps its record. The review's open/passed status lives on the ledger entry's Status line.

## Pre-existing ledger

If `LESSONS-DB.md` exists with a different structure, append this protocol's block under its own `## Review:` heading at the top of the existing content — never rewrite or restructure prior entries.

## Unlisted target types

A target outside the code / docs-plans-specs / quotes-financial menus declares lenses by analogy to the nearest menu and names the analogy in stage 1 (e.g., an infra config reviews as code: correctness, security, blast radius).
