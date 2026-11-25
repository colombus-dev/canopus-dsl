from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker

from canopus_dsl import ConcreteCanopusDSLListener
from canopus_dsl.errors import CollectingErrorListener, ParseError
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
    errors: list[ParseError] = []
    input = InputStream(content)
    lexer = CanopusDSLLexer(input)
    lexer.removeErrorListeners()
    lexer.addErrorListener(CollectingErrorListener(errors))
    stream = CommonTokenStream(lexer)
    parser = CanopusDSLParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CollectingErrorListener(errors))
    tree = parser.program()
    # initialize the listener
    canopus_listener = ConcreteCanopusDSLListener()
    walker = ParseTreeWalker()
    try:
        walker.walk(canopus_listener, tree)  # type: ignore
    except Exception as exc:
        # Error recovery can fire listener callbacks on partial rule contexts
        # (e.g. exitPatternDef with a missing ID). A clean parse must never
        # take this branch. We should restructure the listener if it does.
        if not errors:
            raise
        last_error = errors[-1]
        errors.append(
            ParseError(
                line=last_error.line,
                column=last_error.column,
                message=f"model construction failed: {exc}",
            )
        )
    canopus_listener.errors = errors
    if errors:
        # A parse error means no clean model: callers gate on program is not
        # None instead of duplicating error checks (ADR-0005).
        canopus_listener.program = None
    return canopus_listener
