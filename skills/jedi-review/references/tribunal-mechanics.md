# Tribunal Mechanics

Edge-state and independence rules for running the Jedi Review tribunal. This supplements `SKILL.md`'s six-stage contract — it doesn't replace any of it.

## Adjudication cardinality

One fresh skeptic subagent per round adjudicates all of that round's findings; the skeptic is never one of the round's attackers.

## Round composition

Round 1 = the full declared tribunal. Fix rounds = the Fix re-review menu (see `attack-lenses.md`) plus regression when the target is code, scoped to the fixes and their blast radius. The gate round = the full declared stage-1 tribunal re-run against the current state; when it confirms zero findings, PASS. A clean fix round alone never passes the gate.

## Lens accountability

Every lens reports its strongest failed attacks alongside its findings. A lens returning zero findings and no attack record did not run — the round is incomplete. In round reports, every finding line names its lens, and every declared lens appears in exactly one of three states: with findings, with its attack record, or as DID NOT RUN (per Lens failure states) — so a silent lens is visible no matter which lens goes silent.

## Lens failure states

A lens that cannot dispatch runs serially, or in-line by the orchestrator as last resort. A lens that errored or never returned is reported DID NOT RUN; a round containing one cannot reach the gate. The in-line-by-orchestrator fallback never applies to a stage-4 lens when the orchestrator authored or directed the fix under review: such a lens runs as a subagent, or is reported DID NOT RUN, blocking the gate.

## Coverage

Each lens declares coverage: FULL, or PARTIAL plus what it read. PARTIAL coverage on any lens blocks PASS until the uncovered remainder has been attacked.

## Refuted findings

An attacker may re-raise a REFUTED finding once, only with new evidence the skeptic didn't consider. A second refutation is final for the review.

## Fix-author independence

Stage-4 attackers and skeptic are never any agent or session that authored or directed the fix under review. No author or director of a fix communicates anything about it beyond its stated claim ("what it fixes, where") to any stage-4 participant — attacker or skeptic, before or during the round. Attackers are briefed on a fix only via that stated claim; the skeptic receives the attackers' findings, as stage 3 requires.

## Non-convergence

After three consecutive fix rounds that each end with any confirmed finding — a newly introduced defect, or the original defect still standing unfixed — stop. Report the pattern to the user and question the fix approach itself before burning a fourth round.

## Interruption and standing state

A review keeps one ledger section, updated as each round's adjudication closes, not only at PASS, so an interrupted review keeps its record. Every round close performs three steps: add the round's confirmed rows to the Confirmed defects table; update the Process and Status lines; compare the live ledger's header instructions against `ledger-template.md` (which is canonical for sectioning and placement) and re-sync the header if they differ.

Status takes one of three values: OPEN while any confirmed finding stands; PASSED, with date, the moment the gate round confirms zero findings; or SHIPPED OVER OPEN FINDINGS the moment the user ships anyway despite open findings, recorded with who shipped and when.

## Pre-existing ledger

If `LESSONS-DB.md` exists with a different structure, insert this protocol's `## Review:` section directly below the marker (or, absent a marker, directly below the file's header and intro) and above any prior entries — never rewrite or restructure prior entries.

## Unlisted target types

A target outside the code / docs-plans-specs / quotes-financial menus declares lenses by analogy to the nearest menu and names the analogy in stage 1 (e.g., an infra config reviews as code: correctness, security, blast radius).
