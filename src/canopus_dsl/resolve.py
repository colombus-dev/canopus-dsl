"""Symbol resolution: every reference and import resolves to a known name.

Known names are the local pattern definitions, plus ``external_patterns``
when the caller (e.g. the Colombus consumer) supplies them. An import the
caller could have satisfied but did not is an error; import verification
is skipped (warning) when no externals are given at all.

Declaration order (ADR-0006): only patterns defined earlier, imports, and
externals are in scope for a reference; forward and self references are
``forward-reference`` errors.

Rules come in two kinds:
- program rules: see the whole Program (e.g. import validation)
- leaf rules: see one reference expression plus the set of known names
  (e.g. unknown reference)
Adding a resolution rule = adding one function and registering it.
"""

from collections.abc import Iterable, Mapping

from canopus_dsl.checking import LeafRule, ProgramContext, ProgramRule
from canopus_dsl.errors import Issue
from canopus_dsl.lib import IdExpr, Pattern, Program


def _unknown_reference(
    node: object, pattern: Pattern, ctx: ProgramContext
) -> list[Issue]:
    """An IdExpr matching no pattern, import, or external is an error."""
    if isinstance(node, IdExpr) and node.name not in ctx.known_names:
        return [
            Issue(
                code="unknown-reference",
                severity="error",
                message=f"unknown reference '{node.name}'",
            )
        ]
    return []


def _forward_reference(
    node: object, pattern: Pattern, ctx: ProgramContext
) -> list[Issue]:
    """A name known to the program but declared after this pattern is an error.

    Only patterns defined earlier, imports, and externals are in scope; the
    owning pattern's own name is not yet known inside its definition
    (ADR-0006), so self references are rejected too.
    """
    if not isinstance(node, IdExpr):
        return []
    own_index = next(i for i, p in enumerate(ctx.program.patterns) if p is pattern)
    earlier = {p.name for p in ctx.program.patterns[:own_index]}
    in_scope = earlier | set(ctx.program.imports) | set(ctx.external_patterns or {})
    if node.name in ctx.known_names and node.name not in in_scope:
        return [
            Issue(
                code="forward-reference",
                severity="error",
                message=f"pattern '{node.name}' used before its definition",
            )
        ]
    return []


def _import_validation(ctx: ProgramContext) -> list[Issue]:
    """Imports: warning when unverifiable, error when missing from externals."""
    issues: list[Issue] = []
    for import_name in ctx.program.imports:
        if import_name in ctx.own_names:
            continue
        if ctx.external_patterns is None:
            issues.append(
                Issue(
                    code="unresolved-import",
                    severity="warning",
                    message=(
                        f"import '{import_name}' not verifiable without "
                        f"external pattern definitions"
                    ),
                )
            )
        elif import_name not in ctx.external_patterns:
            issues.append(
                Issue(
                    code="unknown-import",
                    severity="error",
                    message=(
                        f"import '{import_name}' missing from external "
                        f"pattern definitions"
                    ),
                )
            )
    return issues


DEFAULT_PROGRAM_RULES: tuple[ProgramRule, ...] = (_import_validation,)
DEFAULT_LEAF_RULES: tuple[LeafRule, ...] = (_unknown_reference, _forward_reference)


def resolve(
    program: Program,
    external_patterns: Mapping[str, object] | None = None,
    program_rules: Iterable[ProgramRule] = DEFAULT_PROGRAM_RULES,
    leaf_rules: Iterable[LeafRule] = DEFAULT_LEAF_RULES,
) -> list[Issue]:
    """Return resolution findings for ``program``; all-clear yields [].

    ``program_rules`` see the whole model and externals; ``leaf_rules`` get
    each reference expression and the set of known names. Rule order determines
    output order.
    """
    return ProgramContext(program, external_patterns).collect(program_rules, leaf_rules)
