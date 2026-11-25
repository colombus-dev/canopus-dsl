# 0005: Parse errors yield no program

- **Status:** Accepted
- **Date:** 2026-11-25

## Context

ADR-0001 made an invalid parse yield a populated `.errors` list and never
raise. It left `program` unspecified on error: ANTLR error recovery still
reaches `exitProgram`, so `parse_string` of broken input builds a partial
`Program` (e.g. `patterns=[]`, or one recovered pattern) next to the error
list. That left two overlapping validity signals — `program is None` and
`errors != []` — and each consumer picked one:

- The CLI gates `if listener.errors or not listener.program` — checks both,
  redundantly.
- The colombus consumer (`app/service/pattern.py`) gates on
  `if not canopus_listener.program` alone. `pattern P = *+` — a parse error —
  yields a non-None program with one recovered `*` pattern, so the consumer
  accepts the broken input as a plain wildcard while the collected error goes
  unchecked.

## Decision

`parse_string` sets `program = None` whenever any error was collected:

```
program is not None  ⟺  no parse errors
```

One line in `parse_string` after the walk; diagnostics stay in `errors`, which
remains the only home for parse findings. `validate`/`resolve` keep requiring
a non-None `Program`, and callers gate on `program is None` exactly the way
colombus already does.

## Alternatives considered

- **Keep the partial model (status quo).** Every consumer must check both
  signals or reproduce the colombus failure (recovered pattern accepted next
  to an unread error). Rejected for the single-channel contract.
- **Raise on first error.** Contradicts ADR-0001's never-raise contract and
  the interactive multi-error UX it exists for. The diagnostic collection is
  the point; only the model exposure changes.

## Consequences

- **Positive:** one validity channel — `program is not None` means clean; no
  caller can silently skip `errors`.
- **Positive:** colombus's existing gate becomes correct with no change
  there: `pattern P = *+` is now rejected.
- **Positive:** consistent with ADR-0001's model-construction failure branch,
  which already left `program = None` on error.
- **Neutral:** a partial model on error is no longer inspectable via
  `program`; no in-repo consumer relied on it (the CLI dumps the model only
  when clean).
- **Neutral:** `parse_string` keeps its signature; the README documents the
  contract.

## Confidence

High. Pinned by the parametrized `test_parse_errors_yield_no_program`
(`*+`, `()`, `abcdef`) and the flipped `test_parse_invalid_resource`; the
full suite (54 tests) stays green.
