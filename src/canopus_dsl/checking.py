"""Shared rule harness: walk the model once, run program and leaf rules.

``validate`` and ``resolve`` both build on this. Leaf rules receive every
expression, the pattern owning it, and a read-only :class:`ProgramContext`
holding program-wide facts (e.g. the known names for resolution).
"""

from collections.abc import Callable, Mapping

from canopus_dsl.errors import Issue
from canopus_dsl.lib import AlternativeExpr, Pattern, Program

ProgramRule = Callable[[object], list[Issue]]
LeafRule = Callable[[object, Pattern, object], list[Issue]]


def iter_expr_leaves(sequence: list[object]) -> list[object]:
    """Depth-first leaves; hides lists and AlternativeExpr from rules."""
    leaves: list[object] = []
    for node in sequence:
        if isinstance(node, list):
            leaves.extend(iter_expr_leaves(node))
        elif isinstance(node, AlternativeExpr):
            for alt in node.alternatives:
                leaves.extend(iter_expr_leaves([alt]))
        else:
            leaves.append(node)
    return leaves


class ProgramContext:
    """Read-only program-wide facts, computed once per run."""

    def __init__(
        self,
        program: Program,
        external_patterns: Mapping[str, object] | None = None,
    ) -> None:
        self.program = program
        self.external_patterns = external_patterns
        own = {p.name for p in program.patterns}
        imported = set(program.imports)
        externals = set(external_patterns or {})
        self.known_names: frozenset[str] = frozenset(own | imported | externals)
        self.own_names: frozenset[str] = frozenset(own)

    def collect(self, program_rules, leaf_rules) -> list[Issue]:
        """Run rules in order; program rules first, then leaves depth-first."""
        issues: list[Issue] = []
        for rule in program_rules:
            issues.extend(rule(self))
        for rule in leaf_rules:
            for pattern in self.program.patterns:
                for node in iter_expr_leaves(pattern.sequence):
                    issues.extend(rule(node, pattern, self))
        return issues
