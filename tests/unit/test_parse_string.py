"""parse_string coverage: resource-fixture parsing plus grammar-level behavior.

Grammar-level rules (ADR-0002, ADR-0005):
- ``*+``/``**`` are parse errors, not a quantified wildcard (grammar owns it).
- ``start -> end`` (empty middle) is a parse error — an anchored pipeline needs
  at least one expression between the anchors.
- quantified primaries are legal *inside* group alternatives.
- single-element parens ``(Q1)`` parse.
- imports may follow pattern definitions; order is preserved.
"""

from pathlib import Path

import pytest

from canopus_dsl import parse_string
from canopus_dsl.lib import (
    AlternativeExpr,
    ElementExpr,
    EndExpr,
    IdExpr,
    StartExpr,
    WildcardExpr,
)


@pytest.mark.parametrize(
    ("file_name", "expected_patterns", "expected_imports"),
    [
        ("test_simple.canopus", 10, []),
        ("test_import.canopus", 5, ["Q3", "Q4"]),
        ("test_mono.canopus", 1, []),
    ],
)
def test_parse_resource_file(
    file_name: str,
    expected_patterns: int,
    expected_imports: list[str],
    canopus_patterns_resources_path: Path,
) -> None:
    """Each resource DSL parses to a program with the expected patterns/imports."""
    listener = parse_string((canopus_patterns_resources_path / file_name).read_text())
    assert listener.program is not None
    assert len(listener.program.patterns) == expected_patterns
    assert listener.program.imports == expected_imports


def test_parse_invalid_resource(canopus_patterns_resources_path: Path) -> None:
    """Garbage input does not crash; it yields a program with no patterns."""
    listener = parse_string(
        (canopus_patterns_resources_path / "test_invalid.canopus").read_text()
    )
    assert listener.program is not None
    assert listener.program.patterns == []


# --- parse errors -----------------------------------------------------------


@pytest.mark.parametrize(
    "input_code",
    [
        "pattern P = *+\n",
        "pattern P = **\n",
        "pattern P = ()\n",
        "abcdef\n",
        "pattern P = start -> end\n",
        "pattern P = start -> end -> end\n",
    ],
)
def test_invalid_inputs_are_parse_errors(input_code):
    """The grammar rejects the input; errors are collected, never raised."""
    listener = parse_string(input_code)
    assert len(listener.errors) >= 1


# --- grammar acceptance -----------------------------------------------------


def test_bare_wildcard_and_quantified_element_regression():
    """A bare wildcard keeps parsing next to a quantified element."""
    listener = parse_string('pattern Q = * -> [step = "X"]*\n')
    assert listener.errors == []
    seq = listener.program.patterns[0].sequence
    assert isinstance(seq[0], WildcardExpr)
    assert seq[0].multiplicity == "1"
    assert isinstance(seq[1], ElementExpr)
    assert seq[1].multiplicity == "*"


def test_quantifier_inside_group_alternative():
    """Quantified primaries are legal inside group alternatives."""
    listener = parse_string('pattern P = (Q1* | [step = "X"]+)\npattern Q1 = *\n')
    assert listener.errors == []
    alt = listener.program.patterns[0].sequence[0]
    assert isinstance(alt, AlternativeExpr)
    assert isinstance(alt.alternatives[0], IdExpr)
    assert alt.alternatives[0].name == "Q1"
    assert alt.alternatives[0].multiplicity == "*"
    assert isinstance(alt.alternatives[1], ElementExpr)
    assert alt.alternatives[1].multiplicity == "+"


def test_single_element_parens_legal():
    """(Q1) is a one-alternative group, not an error."""
    listener = parse_string("pattern P = (Q1)\npattern Q1 = *\n")
    assert listener.errors == []
    alt = listener.program.patterns[0].sequence[0]
    assert isinstance(alt, AlternativeExpr)
    assert len(alt.alternatives) == 1
    assert isinstance(alt.alternatives[0], IdExpr)
    assert alt.alternatives[0].name == "Q1"


def test_import_after_pattern_and_order_preserved():
    """Imports may follow patterns; the import list keeps its exact order."""
    listener = parse_string("pattern A = *\nimport Q9\n")
    assert listener.errors == []
    assert [p.name for p in listener.program.patterns] == ["A"]
    assert listener.program.imports == ["Q9"]


def test_anchored_pipeline_unchanged():
    """The full anchored pipeline shape is preserved through the regen."""
    listener = parse_string(
        'pattern Q = start -> [step="Visualization"]+ -> * -> '
        '[algoName != "read_csv", step="Data Loading"] -> end\n'
    )
    assert listener.errors == []
    seq = listener.program.patterns[0].sequence
    assert len(seq) == 5
    assert isinstance(seq[0], StartExpr)
    assert isinstance(seq[1], ElementExpr) and seq[1].multiplicity == "+"
    assert isinstance(seq[2], WildcardExpr)
    assert isinstance(seq[3], ElementExpr) and len(seq[3].conditions) == 2
    assert isinstance(seq[4], EndExpr)
