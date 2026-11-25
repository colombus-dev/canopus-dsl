"""Symbol resolution: references and imports resolved against known names."""

import pytest

from canopus_dsl import parse_string
from canopus_dsl.errors import Issue
from canopus_dsl.resolve import resolve


@pytest.mark.parametrize(
    "input_code,external_patterns,expected_issue_codes",
    [
        # Forward reference (should be legal)
        ("pattern A = B\npattern B = *\n", None, []),
        # Unknown reference
        ("pattern A = Nope\n", None, ["unknown-reference"]),
        # Nested alternative resolves
        ("""pattern A = (Q1 | (Q2 -> Q3))\n
         pattern Q1 = *\npattern Q2 = *\npattern Q3 = *\n""", None, []),
        # Ghost in nested alternative
        ("pattern A = (Q1 | Ghost)\npattern Q1 = *\n", None, ["unknown-reference"]),
        # Import resolves with externals
        ("import Q9\npattern A = Q9\n", {"Q9": object()}, []),
        # Import without externals is warning
        ("import Q9\npattern A = Q9\n", None, ["unresolved-import"]),
        # Import missing from externals is error
        ("import Q9\npattern A = Q9\n", {}, ["unknown-import"]),
        # Valid program with no issues
        ("pattern Q = start -> [step = \"X\"] -> end\n", None, []),
    ],
)
def test_resolution_scenarios(input_code, external_patterns, expected_issue_codes):
    """Test various resolution scenarios with parameterized inputs."""
    listener = parse_string(input_code)
    issues = resolve(listener.program, external_patterns=external_patterns)

    # Check that all expected issue codes are present
    found_codes = [issue.code for issue in issues]
    for expected_code in expected_issue_codes:
        assert expected_code in found_codes, (
            f"Expected issue code '{expected_code}' not found in {found_codes}"
        )

    # Check that no unexpected issue codes are present
    for issue in issues:
        assert issue.code in expected_issue_codes or issue.code in [
            "unknown-reference", "unresolved-import", "unknown-import"
        ], (
            f"Unexpected issue code '{issue.code}' found in {found_codes}"
        )


def test_forward_reference_is_legal():
    """A pattern may reference a pattern defined later in the file."""
    listener = parse_string("pattern A = B\npattern B = *\n")
    assert resolve(listener.program) == []


def test_unknown_reference_is_error():
    """A name that is neither defined nor imported is an unknown-reference."""
    listener = parse_string("pattern A = Nope\n")
    issues = resolve(listener.program)
    assert any(
        i.code == "unknown-reference"
        and i.severity == "error"
        and "Nope" in i.message
        for i in issues
    )


def test_nested_alternative_resolves():
    """References nested inside alternatives resolve when defined."""
    listener = parse_string(
        "pattern A = (Q1 | (Q2 -> Q3))\n"
        "pattern Q1 = *\npattern Q2 = *\npattern Q3 = *\n"
    )
    assert resolve(listener.program) == []


def test_ghost_in_nested_alternative():
    """An undefined name inside an alternative is still unknown-reference."""
    listener = parse_string("pattern A = (Q1 | Ghost)\npattern Q1 = *\n")
    issues = resolve(listener.program)
    assert any(
        i.code == "unknown-reference" and "Ghost" in i.message for i in issues
    )


def test_ghost_in_sequence_alternative():
    """An undefined name inside a multi-step alternative is unknown-reference."""
    listener = parse_string(
        "pattern A = (Q1 -> Ghost | Q2)\n"
        "pattern Q1 = *\npattern Q2 = *\n"
    )
    issues = resolve(listener.program)
    assert any(
        i.code == "unknown-reference" and "Ghost" in i.message for i in issues
    )


def test_import_resolves_with_externals():
    """An import satisfied by external_patterns resolves cleanly."""
    listener = parse_string("import Q9\npattern A = Q9\n")
    assert resolve(listener.program, external_patterns={"Q9": object()}) == []


def test_import_without_externals_is_warning():
    """Without externals an import cannot be verified: warning, not error."""
    listener = parse_string("import Q9\npattern A = Q9\n")
    issues = resolve(listener.program)
    assert any(
        i.code == "unresolved-import" and i.severity == "warning" for i in issues
    )
    assert not any(i.severity == "error" for i in issues)


def test_import_missing_from_externals_is_error():
    """externals given but missing the import: unknown-import, error."""
    listener = parse_string("import Q9\npattern A = Q9\n")
    issues = resolve(listener.program, external_patterns={})
    assert any(
        i.code == "unknown-import" and i.severity == "error" for i in issues
    )


def test_custom_program_rule():
    """Custom program rules can be passed to resolve."""
    expected_issue = Issue(
        code="my-custom-error",
        severity="error",
        message="Just my custom error message",
    )
    def my_program_rule(_ctx) -> list[Issue]:
        return [
            expected_issue
        ]

    # This test verifies the function accepts custom rules
    listener = parse_string("pattern Q = *\n")
    issues = resolve(listener.program, program_rules=[my_program_rule])
    assert len(issues) == 1
    assert issues[0] == expected_issue


def test_custom_leaf_rule():
    """Custom leaf rules can be passed to resolve."""
    expected_issue = Issue(
            code="my-custom-error",
            severity="error",
            message="Just my custom error message",
        )
    def my_leaf_rule(_node, _pattern, _ctx) -> list[Issue]:
        return [
            expected_issue
        ]

    # This test verifies the function accepts custom rules
    listener = parse_string("pattern Q = *\n")
    issues = resolve(listener.program, leaf_rules=[my_leaf_rule])
    assert len(issues) == 1
    assert issues[0] == expected_issue
