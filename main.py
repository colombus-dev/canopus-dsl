import sys

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from canopus import ConcreteCanopusDSLListener
from canopus.generated.CanopusDSLLexer import CanopusDSLLexer
from canopus.generated.CanopusDSLParser import CanopusDSLParser


def main(argv: list[str] | None = None):
    if not argv or len(argv) < 2:
        raise RuntimeError("Invalid cmd arguments")
    # read the canopus file and parse its content
    input = FileStream(argv[1])
    lexer = CanopusDSLLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CanopusDSLParser(stream)
    tree = parser.program()
    # initialize the listener
    my_listener = ConcreteCanopusDSLListener()
    walker = ParseTreeWalker()
    walker.walk(my_listener, tree)  # type: ignore
    # print the constructed model
    for pattern in my_listener.patterns:
        print("pattern name=", pattern.name)
        for group in pattern.sequence:
            print("\t- ", group)


if __name__ == "__main__":
    main(sys.argv)
