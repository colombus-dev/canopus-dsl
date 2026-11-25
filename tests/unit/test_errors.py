"""Parse-error collection: invalid input yields collected errors, never a raise."""

import pytest

from canopus_dsl import parse_string
from canopus_dsl.errors import ParseError


def test_valid_input_has_no_errors():
    """A clean program yields zero collected errors and a populated model."""
    listener = parse_string("pattern Q = [step = \"X\"]\n")
    assert listener.errors == []
    assert listener.program is not None
    assert len(listener.program.patterns) == 1


def test_bad_token_first_error_points_at_line_1():
    """A root identifier that is not a pattern/import is collected at line 1."""
    listener = parse_string("abcdef\n")
    assert len(listener.errors) >= 1
    assert isinstance(listener.errors[0], ParseError)
    assert listener.errors[0].line == 1


def test_multiple_bad_lines_each_get_an_error():
    """Errors are collected per offending statement, not abort-on-first."""
    listener = parse_string("abcdef\npattern =\n")
    lines = {err.line for err in listener.errors}
    assert 1 in lines
    assert 2 in lines


def test_unterminated_string_is_a_lexer_error_not_a_crash():
    """An unterminated string yields a collected error; parse does not raise."""
    listener = parse_string("pattern Q = [step = \"oops]\n")
    assert len(listener.errors) >= 1
    assert any("token recognition error" in e.message for e in listener.errors)


@pytest.mark.parametrize(
    "input_code",
    ["pattern P = *+\n", "pattern P = ()\n", "abcdef\n"],
)
def test_parse_errors_yield_no_program(input_code):
    """A parse error leaves program None; only clean parses expose a model."""
    listener = parse_string(input_code)
    assert len(listener.errors) >= 1
    assert listener.program is None


def test_walker_crash_with_prior_error_appends_construction_failure():
    """Construction failure inherits last error's line/column."""
    from canopus_dsl import ConcreteCanopusDSLListener
    def patch_exitPatternDef(_, __):
        raise RuntimeError("patch_exitPatternDef error")
    # Patch the listener to raise during walk
    original = ConcreteCanopusDSLListener.exitPatternDef
    ConcreteCanopusDSLListener.exitPatternDef = patch_exitPatternDef
    try:
        listener = parse_string("abcdef\npattern Q = *\n")
        assert len(listener.errors) == 2  # lexer error + construction failure
        assert listener.errors[-1].message.startswith("model construction failed")
        assert listener.errors[-1].line == 1  # inherited from the 'abcdef' error
    finally:
        ConcreteCanopusDSLListener.exitPatternDef = original


def test_walker_crash_without_prior_error_propagates():
    """Construction failure without prior errors raises."""
    from canopus_dsl import ConcreteCanopusDSLListener
    def patch_exitPatternDef(_, __):
        raise RuntimeError("patch_exitPatternDef error")
    # Patch the listener to raise during walk
    original = ConcreteCanopusDSLListener.exitPatternDef
    ConcreteCanopusDSLListener.exitPatternDef = patch_exitPatternDef
    try:
        # Clean input that triggers the walker crash
        import pytest
        with pytest.raises(RuntimeError, match="patch_exitPatternDef error"):
            parse_string("pattern Q = *\n")
    finally:
        ConcreteCanopusDSLListener.exitPatternDef = original
