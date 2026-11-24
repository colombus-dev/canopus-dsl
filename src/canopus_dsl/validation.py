"""Semantic validation of the parsed model.

Rules come in two kinds:
- program rules: see the whole Program (e.g. duplicate pattern names)
- leaf rules:  see one expression plus the name of its owning pattern
  (e.g. quantified wildcard)
Adding an invariant = adding one function and registering it.
"""

from collections.abc import Callable, Iterable

from canopus_dsl.errors import Issue
from canopus_dsl.lib import AlternativeExpr, Program, WildcardExpr

# --- traversal: the single place that knows the AST nesting shape ---


def _iter_expr_leaves(sequence: list[object]) -> list[object]:
    """Depth-first leaves; hides lists and AlternativeExpr from rules."""
    leaves: list[object] = []
    for node in sequence:
        if isinstance(node, list):
            leaves.extend(_iter_expr_leaves(node))
        elif isinstance(node, AlternativeExpr):
            for alt in node.alternatives:
                leaves.extend(_iter_expr_leaves([alt]))
        else:
            leaves.append(node)
    return leaves


# --- rules ---

ProgramRule = Callable[[Program], list[Issue]]
LeafRule = Callable[[object, str], list[Issue]]  # (expr, pattern_name)


def _duplicate_pattern_names(program: Program) -> list[Issue]:
    """Check for duplicate pattern names in the program."""
    issues: list[Issue] = []
    seen: set[str] = set()
    for pattern in program.patterns:
        if pattern.name in seen:
            issues.append(
                Issue(
                    code="duplicate-pattern",
                    severity="error",
                    message=f"duplicate pattern name '{pattern.name}'",
                )
            )
        else:
            seen.add(pattern.name)
    return issues


def _wildcard_quantifier(node: object, pattern_name: str) -> list[Issue]:
    """Check that wildcards do not carry multipliers."""
    if isinstance(node, WildcardExpr) and node.multiplicity != "1":
        return [
            Issue(
                code="wildcard-quantifier",
                severity="error",
                message=(
                    f"wildcard '*' cannot carry a multiplier (pattern '{pattern_name}')"
                ),
            )
        ]
    return []


DEFAULT_PROGRAM_RULES: tuple[ProgramRule, ...] = (_duplicate_pattern_names,)
DEFAULT_LEAF_RULES: tuple[LeafRule, ...] = (_wildcard_quantifier,)


def validate(
    program: Program,
    program_rules: Iterable[ProgramRule] = DEFAULT_PROGRAM_RULES,
    leaf_rules: Iterable[LeafRule] = DEFAULT_LEAF_RULES,
) -> list[Issue]:
    """Return every invariant violation in ``program``; valid input yields [].

    ``program_rules`` see the whole model; ``leaf_rules`` get each expression
    and the name of the pattern owning it. Rule order determines output order.
    """
    issues: list[Issue] = []
    for rule in program_rules:
        issues.extend(rule(program))
    for rule in leaf_rules:
        for pattern in program.patterns:
            for node in _iter_expr_leaves(pattern.sequence):
                issues.extend(rule(node, pattern.name))
    return issues
