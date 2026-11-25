"""Semantic validation of the parsed model.

Rules come in two kinds:
- program rules: see the whole Program (e.g. duplicate pattern names)
- leaf rules:  see one expression plus the name of its owning pattern
Adding an invariant = adding one function and registering it.
"""

from collections.abc import Iterable

from canopus_dsl.checking import LeafRule, ProgramContext, ProgramRule
from canopus_dsl.errors import Issue
from canopus_dsl.lib import Program


def _duplicate_pattern_names(ctx: ProgramContext) -> list[Issue]:
    """Check for duplicate pattern names in the program."""
    issues: list[Issue] = []
    seen: set[str] = set()
    for pattern in ctx.program.patterns:
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


DEFAULT_PROGRAM_RULES: tuple[ProgramRule, ...] = (_duplicate_pattern_names,)
DEFAULT_LEAF_RULES: tuple[LeafRule, ...] = ()


def validate(
    program: Program,
    program_rules: Iterable[ProgramRule] = DEFAULT_PROGRAM_RULES,
    leaf_rules: Iterable[LeafRule] = DEFAULT_LEAF_RULES,
) -> list[Issue]:
    """Return every invariant violation in ``program``; valid input yields [].

    ``program_rules`` see the whole model; ``leaf_rules`` get each expression
    and the name of the pattern owning it. Rule order determines output order.
    """
    return ProgramContext(program).collect(program_rules, leaf_rules)
