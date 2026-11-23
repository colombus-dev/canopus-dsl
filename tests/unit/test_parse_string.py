from pathlib import Path

import pytest

from canopus_dsl import parse_string


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
