# 0004: Group alternatives keep their sequence shape (SequenceExpr)

- **Status:** Accepted
- **Date:** 2026-11-25

## Context

ADR-0002's grammar (and the paper, §5.3 listing 1) make an alternative an
`expr` — a sequence that may have several steps:

```
expr : multipExpr ('->' multipExpr)*;
```

So `(Q1 -> Q2 | Q3)` is a group whose first alternative is the two-step
pipeline `Q1 -> Q2` and whose second is `Q3`. During implementation the
listener pushed a multi-step alternative as a raw Python `list` and
`AlternativeExpr.alternatives` flattened it back out with a pydantic
`field_validator` (`_flatten_sequence_alternatives`):

```
(Q1 -> Q2 | Q3)  →  alternatives = [IdExpr(Q1), IdExpr(Q2), IdExpr(Q3)]   # flat
```

The flat model is lossy: it cannot tell "first alternative is the pipeline
`Q1 -> Q2`" from "three alternatives, one per step". Consumers built on the
public model cannot route per-alternative; re-introducing the boundary later
is a breaking model change. A consumer check (colombus
`app/utils/convert_canopus_to_legacy.py`) reads `a.conditions` on every
alternative — each alternative must be a typed `Expr`, never a bare list.

## Decision

Introduce a typed sequence node and drop the flattening patch:

```python
class SequenceExpr(Expr):
    """A ``->`` step sequence: each group alternative is one mini-pipeline."""
    steps: list["Expr"]

class AlternativeExpr(Expr):
    alternatives: list["Expr"]  # single Expr or SequenceExpr per alternative
```

The listener's `exitExpr` emits `SequenceExpr(steps=items)` when an
alternative has more than one step, and the bare expression when it has one.
`_flatten_sequence_alternatives` is deleted; `iter_expr_leaves` recurses into
`SequenceExpr.steps` instead of duck-typing a raw list.

```
(Q1 -> Q2 | Q3)  →  alternatives = [SequenceExpr(steps=[Q1, Q2]), IdExpr(Q3)]
(Q1 | Q2)        →  alternatives = [IdExpr(Q1), IdExpr(Q2)]      # unchanged
```

## Alternatives considered

- **`alternatives: list[list[Expr]]`.** Mirrors the grammar literally, but
  every alternative — including today's ordinary `(B | C)` — becomes a bare
  list, and the colombus consumer's `a.conditions` crashes on a list.
  Rejected: it regresses the working case.
- **Stay flat (status quo).** Cheapest, but erases the sequence boundary the
  grammar declares; the exposing model is public API consumed by colombus, so
  un-flattening later is a breaking change. Rejected.
- **Typed `SequenceExpr` (chosen).** One new public node, listener change, and
  checker recursion; single-step alternatives keep today's shapes, so the
  consumer keeps working unchanged.

## Consequences

- **Positive:** the model preserves the per-alternative sequence boundary;
  single-step alternatives — every fixture and DSL input in use — keep their
  exact types, so colombus's consumer is unaffected.
- **Positive:** the dead duck-typed `isinstance(node, list)` branch in
  `iter_expr_leaves` is replaced by typed recursion over `SequenceExpr.steps`;
  an undefined name inside a multi-step alternative is reported by `resolve`
  (pinned by `test_ghost_in_sequence_alternative`).
- **Deferred:** colombus has no rendering for multi-step alternatives yet
  (`convert_canopus_to_legacy` flattens all alternative steps into one list,
  `# TODO: replace with visitor`). Modeling them is a new capability, not a
  regression; the consumer extension is out of scope here.

## Confidence

High. The shape was verified against the generated parser and the full suite
(55 tests green), including the two TDD cycles: the model-shape guard test
(RED before `SequenceExpr` existed) and the resolve-recursion guard (RED
while `iter_expr_leaves` still lacked the `SequenceExpr` branch).
