# LESSONS-DB.md — template

Running database of confirmed defects, their root causes, and the prevention rule each one taught. Consult it before similar work; append one section per Jedi Review. Lives at the target repo's root as `LESSONS-DB.md`.

Copy everything between the `---` lines below for each new review. Newest review goes on top, oldest at the bottom.

---

## Review: <YYYY-MM-DD> — <target name>

**Scope:** <target, type (code/doc/plan/spec/quote), size>
**Process:** <N> lenses × <N> rounds — raised <N> / confirmed <N> / refuted <N>

### Confirmed defects

| ID | Defect | Root cause | Prevention rule |
|---|---|---|---|
| D1 | <one-line defect> | <why it happened> | <what to check next time> |
| D2 | | | |

### Deliberate decisions (not bugs — do not "fix")

| Decision | Rationale |
|---|---|
| <thing reviewers keep flagging> | <why it's intentional> |

### Follow-ups

- <work deferred out of this review, with an owner if known>

---

<!-- Insert each new review's block directly below this line; keep newest-first order. -->

