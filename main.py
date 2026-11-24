"""Command-line entry point for the Canopus DSL compiler front end.

Exit codes:
    0 - clean model (warnings allowed)
    1 - parse errors or error-severity issues
    2 - usage error
Diagnostics always go to stderr while the model goes to stdout.
"""

import sys
from pathlib import Path

from canopus_dsl import parse_string, resolve, validate

USAGE = "usage: python main.py <file.canopus>"


def main(argv: list[str] | None = None) -> int:
    if not argv or len(argv) < 2:
        print(USAGE, file=sys.stderr)
        return 2

    try:
        content = Path(argv[1]).read_text()
    except OSError as exc:
        print(f"error: {argv[1]}: {exc.strerror}", file=sys.stderr)
        return 2

    listener = parse_string(content)
    for error in listener.errors:
        print(f"line {error.line}:{error.column}: {error.message}", file=sys.stderr)
    if listener.errors or not listener.program:
        return 1

    issues = validate(listener.program) + resolve(listener.program)
    for issue in issues:
        print(f"{issue.severity}: {issue.code}: {issue.message}", file=sys.stderr)
    if any(issue.severity == "error" for issue in issues):
        return 1

    for import_name in listener.program.imports:
        print("Import ", import_name)
    for pattern in listener.program.patterns:
        print("pattern name=", pattern.name)
        for group in pattern.sequence:
            print("\t- ", group)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
