# 0006: Declaration order required

- **Status:** Accepted
- **Date:** 2026-11-26
- **Supersedes (partially):** ADR-0002's interleaved-imports decision (issue 5,
  the `program: (importPatterns | patternDef)+ EOF;` rule), and the
  "interleaved imports" item in ADR-0003's list of ADR-0002's remaining
  accepted fixes. ADR-0002 stays accepted for its other fixes (wildcard dual
  role, group quantifiers, single-element parens).

## Context

Phase-2 shipped two conveniences: `import` statements may appear before,
among, or after patterns, and symbol resolution accepts any pattern name
regardless of definition order. Both complicate the reading model for no
measured benefit — no fixture or consumer uses an interleaved import, and
order-free resolution silently permits reference cycles (mutual recursion).
The DSL contract should be one-pass: declare before use.

## Decision

1. **Imports precede all pattern definitions.** The `program` rule reverts to
   the pre-phase-2 shape:

   ```
   program: importPatterns* patternDef+ EOF;
   ```

   An `import` after the first pattern is a parse error (and per ADR-0005
   yields no program). Multiple import lines before the first pattern remain
   legal, and a file containing only imports (no pattern) is a parse error,
   as before phase 2.

2. **References must name an earlier declaration.** Resolution is
   order-aware: a reference inside a pattern body may only name a pattern
   defined earlier, an import, or an external. A reference to a later
   pattern or to the owning pattern's own name is a `forward-reference`
   error (severity `error`). Because a reference cycle always contains a
   forward edge, mutual recursion becomes impossible.

## Alternatives considered

- **Forbid interleaving in validation instead of the grammar.** Rejected:
   the model stores patterns and imports as separate lists and does not
   preserve their positions, so resolution cannot detect an interleaved
   import. The grammar is the only layer that sees order.
- **Allow self-reference (recursion).** Rejected: the single-pass mental
   model (a name becomes known when its definition completes) is simpler,
   and no fixture or example uses a recursive pattern.
- **Order-free resolution plus a cycle rule.** Rejected: a cycle check and
   free ordering are more machinery than the one-pass rule, with the same
   net effect on recursive programs.

## Consequences

- **Positive:** a program reads top to bottom; every reference points at an
  already-complete definition; reference cycles are impossible.
- **Positive:** the import rule matches the pre-phase-2 grammar shape, so
  the change is a reversal, not a new construct.
- **Negative:** any corpus with an interleaved import or a forward reference
  now fails (parse error / `forward-reference`); the Colombus consumer owns
  its fixtures.
- **Neutral:** one grammar regeneration (py + js); README syntax reference
  updated.

## Confidence

High. The two enforcement points are the only layers that can see order —
the grammar for imports, `resolve` for references — and tests pin each
boundary (import after pattern, imports-only file, forward, self, nested,
mutual reference).
