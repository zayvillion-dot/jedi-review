# Tribunal Mechanics

Edge-state and independence rules for running the Jedi Review tribunal. This supplements `SKILL.md`'s six-stage contract — it doesn't replace any of it.

## Adjudication cardinality

One fresh skeptic subagent per round adjudicates all of that round's findings; the skeptic is never one of the round's attackers.

## Round composition

Round 1 = the full declared tribunal; if it confirms zero findings, round 1 is the gate round and the review passes — no duplicate run is owed. Fix rounds = the Fix re-review menu (see `attack-lenses.md`) plus regression when the target is code, scoped to the fixes and their blast radius. The gate round = the full declared stage-1 tribunal run again against the current state; when it confirms zero findings, PASS. A clean fix round alone never passes the gate.

## Lens accountability

Every lens reports its strongest failed attacks alongside its findings. A lens returning zero findings and no attack record did not run — the round is incomplete. In round reports, every finding line names its lens, and every declared lens appears in exactly one of three states: with findings, with its attack record, or as DID NOT RUN (per Lens failure states) — so a silent lens is visible no matter which lens goes silent.

## Lens failure states

A lens that cannot dispatch runs serially, or in-line by the orchestrator as last resort. A lens that errored or never returned is reported DID NOT RUN; a round containing one cannot reach the gate. The in-line-by-orchestrator fallback never applies to a fix-round or gate-round lens when the orchestrator authored or directed a fix under review: such a lens runs as a subagent, or is reported DID NOT RUN, blocking the gate. If that rule would leave every lens of such a round DID NOT RUN (no dispatch available and the orchestrator authored or directed the fixes), the review pauses: report the blocked state to the user and hand the round to a session or agent that did not author or direct the fixes.

## Coverage

Each lens declares coverage: FULL, or PARTIAL plus what it read. PARTIAL coverage on any lens blocks PASS until the uncovered remainder has been attacked: re-invoke the same lens on the remainder, report one line per invocation carrying the lens name, the segment it read, and that invocation's own findings or attack record — for example:

```
ambiguity [PARTIAL: files A–M] 2 raised
ambiguity [remainder: files N–Z] 0 raised, attacks recorded
```

The lens counts as run only when its invocations' segments jointly reach FULL coverage of the target.

## Refuted findings

An attacker may re-raise a REFUTED finding once, only with new evidence the skeptic didn't consider. A second refutation is final for the review.

## Fix-author independence

These rules bind every round that reviews or gates fixed work — fix rounds and gate rounds alike. Their attackers and skeptic are never any agent or session that authored or directed a fix under review. No author or director of a fix communicates anything about it beyond its stated claim ("what it fixes, where") to any participant of those rounds — attacker or skeptic, before or during the round. Attackers are briefed on a fix only via that stated claim; the skeptic receives the attackers' findings, as stage 3 requires.

## Non-convergence

A confirming round is any round — fix round or gate round — that ends with at least one confirmed finding: a newly introduced defect, a newly surfaced one, or an original still standing unfixed. After three confirming rounds, counted from the review's start, its last PASS, or the user's last authorization to continue — clean rounds in between do not reset the count — stop. Report the pattern to the user and question the fix approach itself before burning another round. User authorization resets the count to zero.

## Interruption and standing state

A review keeps one ledger section, updated as each round's adjudication closes, not only at PASS, so an interrupted review keeps every closed round's record. A round interrupted between attack and adjudication is void: its raised findings are unadjudicated claims — discard them, and the resuming session re-runs that round from stage 2. Every round close performs three steps: add the round's confirmed rows to the Confirmed defects table; update the Process and Status lines; compare the live ledger's header instructions against `ledger-template.md` (which is canonical for sectioning and placement) and re-sync the header if they differ.

Status takes one of three values: OPEN while any confirmed finding stands; PASSED, with date, the moment the gate round confirms zero findings; or SHIPPED OVER OPEN FINDINGS the moment the user ships anyway despite open findings, recorded with who shipped and when.

## Pre-existing ledger

If `LESSONS-DB.md` exists with a different structure, insert this protocol's `## Review:` section directly below the marker (or, absent a marker, directly below the file's header and intro) and above any prior entries — never rewrite or restructure prior entries.

## Unlisted target types

A target outside the code / docs-plans-specs / quotes-financial menus declares lenses by analogy to the nearest menu and names the analogy in stage 1 (e.g., an infra config reviews as code: correctness, security, blast radius).
