from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from canopus_dsl import ConcreteCanopusDSLListener
from canopus_dsl.generated.CanopusDSLLexer import CanopusDSLLexer
from canopus_dsl.generated.CanopusDSLParser import CanopusDSLParser


def parse_string(content: str) -> ConcreteCanopusDSLListener:
    """Parse the given string aand return the initialized canopus listener.

    Once initialized, the retrieved patterns are accessible via the `patterns` attribute.

    Args:
        content (str): the string to parse

    Returns:
        ConcreteCanopusDSLListener: the initialized canopus listener
    """
    # read the canopus file and parse its content
    input = InputStream(content)
    lexer = CanopusDSLLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CanopusDSLParser(stream)
    tree = parser.program()
    # initialize the listener
    canopus_listener = ConcreteCanopusDSLListener()
    walker = ParseTreeWalker()
    walker.walk(canopus_listener, tree)  # type: ignore
    return canopus_listener
