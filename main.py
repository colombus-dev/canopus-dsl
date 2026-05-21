from pathlib import Path
import sys

from canopus_dsl import parse_string


def main(argv: list[str] | None = None):
    if not argv or len(argv) < 2:
        raise RuntimeError("Invalid cmd arguments")
    content = Path(argv[1]).read_text()
    listener = parse_string(content)
    if not listener.program:
        raise Exception("Failed to parse")
    # print the constructed model
    for importP in listener.program.imports:
        print("Import ", importP)
    for pattern in listener.program.patterns:
        print("pattern name=", pattern.name)
        for group in pattern.sequence:
            print("\t- ", group)


if __name__ == "__main__":
    main(sys.argv)
