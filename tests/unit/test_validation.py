"""Semantic validation: model invariants reported as Issues, never raised."""

import pytest

from canopus_dsl import parse_string
from canopus_dsl.errors import Issue
from canopus_dsl.validation import validate


@pytest.mark.parametrize(
    "input_code,expected_codes",
    [
        # Duplicate pattern names
        ("pattern Q = *\npattern Q = *\n", ["duplicate-pattern"]),
        # Wildcard quantifiers
        ("pattern P = *+\n", ["wildcard-quantifier"]),
        ("pattern P = **\n", ["wildcard-quantifier"]),
        # Valid inputs
        ('pattern Q = start -> [step = "X"] -> end\n', []),
        ("pattern A = *\npattern B = *\n", []),
    ],
)
def test_validation_scenarios(input_code, expected_codes):
    """Test various validation scenarios with parameterized inputs."""
    listener = parse_string(input_code)
    issues = validate(listener.program)

    # Check that all expected issue codes are present
    found_codes = [issue.code for issue in issues]
    for expected_code in expected_codes:
        assert expected_code in found_codes, (
            f"Expected issue code '{expected_code}' not found in {found_codes}"
        )

    # Check that no unexpected issue codes are present
    for issue in issues:
        assert issue.code in expected_codes or issue.code in [
            "duplicate-pattern",
            "wildcard-quantifier",
        ], f"Unexpected issue code '{issue.code}' found in {found_codes}"


def test_clean_program_yields_no_issues():
    """A normal pipeline program validates with zero noise."""
    listener = parse_string('pattern Q = start -> [step = "X"] -> end\n')
    assert validate(listener.program) == []


def test_custom_program_rule():
    """Custom program rules can be passed to validate."""
    expected_issue = Issue(
        code="my-custom-error",
        severity="error",
        message="Just my custom error message",
    )
    def my_program_rule(_program) -> list[Issue]:
        return [
            expected_issue
        ]

    # This test verifies the function accepts custom rules
    listener = parse_string("pattern Q = *\n")
    issues = validate(listener.program, program_rules=[my_program_rule])
    assert len(issues) == 1
    assert issues[0] == expected_issue


def test_custom_leaf_rule():
    """Custom leaf rules can be passed to validate."""
    expected_issue = Issue(
            code="my-custom-error",
            severity="error",
            message="Just my custom error message",
        )
    def my_leaf_rule(_node, _pattern_name) -> list[Issue]:
        return [
            expected_issue
        ]

    # This test verifies the function accepts custom rules
    listener = parse_string("pattern Q = *\n")
    issues = validate(listener.program, leaf_rules=[my_leaf_rule])
    assert len(issues) == 1
    assert issues[0] == expected_issue
