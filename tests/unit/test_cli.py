"""CLI behavior: exit codes, usage, diagnostics."""

import re
from pathlib import Path

from main import main

RESOURCES = Path("tests/resources")


def test_no_args_prints_usage_to_stderr_and_exit_2(capsys):
    code = main([])
    _out, err = capsys.readouterr()
    assert code == 2
    assert "usage: python main.py <file.canopus>" in err
    assert "Traceback" not in err


def test_mono_file_prints_model_exit_0(capsys):
    code = main(["main.py", str(RESOURCES / "test_mono.canopus")])
    out, err = capsys.readouterr()
    assert code == 0
    assert "pattern name= Q" in out
    assert err == ""


def test_import_file_exit_0_with_two_warnings(capsys):
    code = main(["main.py", str(RESOURCES / "test_import.canopus")])
    out, err = capsys.readouterr()
    assert code == 0
    assert out.count("Import ") == 2
    assert err.count("unresolved-import") == 2


def test_invalid_file_exit_1_with_line_col(capsys):
    code = main(["main.py", str(RESOURCES / "test_invalid.canopus")])
    _out, err = capsys.readouterr()
    assert code == 1
    assert re.search(r"line \d+:\d+: ", err)
    assert "Traceback" not in err


def test_unresolved_file_exit_1_naming_reference(capsys):
    code = main(["main.py", str(RESOURCES / "test_simple.canopus")])
    out, err = capsys.readouterr()
    assert code == 1
    assert "unknown-reference" in err
    assert "SP6" in err
    assert out == ""
