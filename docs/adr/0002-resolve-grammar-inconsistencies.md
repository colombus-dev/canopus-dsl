# 0002: Resolve grammar inconsistencies

- **Status:** Accepted
- **Date:** 2026-11-23
- **Supersedes (partially):** the `wildcard-quantifier` validation rule defined
  in ADR-0001 is retired — the grammar now rejects that input before
  validation runs. ADR-0001 itself remains accepted (diagnostics collection
  unchanged); this record replaces only that one rule.

## Context

Five inconsistencies discovered in `ANTLR/CanopusDSL.g4`:

1. `*` is both the wildcard primary and the `'*'` multiplier — `*+` and `**`
   parse as a quantified wildcard (meaningless); the grammar carries a `TODO`
   admitting it.
2. `start -> end` is illegal (`middleExpr` requires at least one element) —
   an empty pipeline is a valid query.
3. Quantifiers apply only to whole groups, never inside them (top-level `Q1*`
   legal, `(Q1* | Q2)` not).
4. `(Q1)` is illegal — the alternative rule demands at least one `|`.
5. Imports are locked before all pattern definitions.

## Decision

Restructure the grammar once (one py+js regeneration); additive except one
restriction:

```
program:      (importPatterns | patternDef)+ EOF;             // 5
patternExpr:  START_OP '->' middleExpr? '->' END_OP          // 2
            | START_OP '->' middleExpr?
            | middleExpr '->' END_OP
            | middleExpr;
expr:         multipExpr ('->' multipExpr)*;                  // 3
multipExpr:   WILDCARD # wildcardAtom                         // 1
            | primary multipOperator? # quantified;
primary:      '(' expr ('|' expr)* ')' # alternativeExpr      // 4
            | '[' condition (',' condition)* ']' # elementExpr
            | ID # id;                                          // WILDCARD removed
```

The `*` dual role is resolved by structure, not a new symbol: `*` stays the
wildcard character, a lone `*` matches `wildcardAtom`, and any following
`+`/`*` has nothing to attach to — `*+`/`**` become parse errors.

## Alternatives considered

- **Keep the dual role, catch `*+` in validation (Phase-1 status quo).** Cheap,
  but the inconsistency and the grammar `TODO` persist; `*+` would live with
  two overlapping error paths. Rejected as the end state.
- **Rename the wildcard symbol** (e.g. `_` or `ANY`). Removes ambiguity but
  breaks the paper's notation, every example, and users. Rejected.
- **Structural fix (chosen).** One grammar change resolves all five
  inconsistencies; existing fixtures keep parsing (additive + one restriction).

## Consequences

- **Positive:** single-path grammar; the L29 `TODO` is resolved; `*+` is
  rejected at parse time and the Phase-1 validation rule is deleted (its test
  migrates to a parse-error assert in the same commit).
- **Positive:** regression safety — the four `ANTLR/resources/test_*.canopus`
  fixtures parse identically before and after.
- **Negative:** one regeneration touches both generated trees; the listener's
  wildcard handling is reworked once.
- **Neutral:** `import`/`pattern` interleaving becomes legal — a documented
  behavior change in the README syntax reference.

## Confidence

High. Mechanics verified against the generated lexer (implicit-literal token
ordering) and the fixture corpus.
