# 0001: Collect parse diagnostics instead of raising

- **Status:** Accepted
- **Date:** 2026-11-23

## Context

`parse_string` throws a raw `RecognitionException` through ANTLR's default
console listener: the first invalid token aborts the program with no collected
error, no partial model, and a stack trace. Semantic errors are worse —
duplicate pattern names and unknown references parse clean and fail later,
inside the SQL-compiling consumer in Colombus. The DSL targets data scientists,
whose failure mode is interactive `.canopus` editing; abort-on-first-error
forces an edit-reparse loop.

## Decision

Keep the grammar as the single source of syntax, and put every other check in
pure Python one layer above it:

- Replace ANTLR's default error listeners with silent collectors; merge their
  findings into `listener.errors`. `parse_string(content)` never raises and
  keeps its signature — an invalid parse yields a populated `.errors`.
- `validate(program)` checks model invariants (duplicate patterns; a wildcard
  carrying a quantifier until the grammar rejects it in Phase 2).
- `resolve(program, external_patterns)` checks references and imports: forward
  references legal, unknown reference is an error, unresolved import is a
  warning, import missing from externals is an error.
- CLI: exit 0 clean, 1 on any error-severity finding, 2 on usage error;
  diagnostics to stderr, model dump to stdout only when clean. Warnings never
  fail.

## Alternatives considered

- **Raise on first error (status quo).** Simple, but one fix per run, no model
  for partial recovery, hostile to interactive use. Rejected.
- **Reject semantic violations in the grammar.** Would need a `.g4` change and
  py+js regeneration for every rule; directly against the stabilization goal
  of the phase. Rejected.
- **Collect + validate + resolve above the grammar (chosen).** One-time cost,
  all future model-level fixes land in tested Python without grammar churn.

## Consequences

- **Positive:** multi-error UX instead of abort-on-first; caller API unchanged;
  zero grammar changes in this phase.
- **Positive:** schema-level and reference-level bugs are fixed in
  `validation.py`/`resolve.py`; `.g4` regeneration is reserved for true syntax
  changes (Phases 2–4).
- **Negative:** two new layers to maintain; cross-file resolution depends on
  callers supplying `external_patterns` — the CLI does not wire sibling-file
  loading (deferred).

## Confidence

High. The design mirrors Fowler's Notification pattern and the DSL catalog's
semantic-model layering already visible in this repo.
