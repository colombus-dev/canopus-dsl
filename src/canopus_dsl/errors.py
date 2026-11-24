"""Collected diagnostics: parse errors are gathered, never raised.

:class:`ParseError` is one collected diagnostic. The lexer and parser use a
silent error listener that appends to a shared list, so ``parse_string``
keeps its signature and an invalid parse yields a populated ``.errors``.
"""

from dataclasses import dataclass
from typing import Literal

from antlr4.error.ErrorListener import ErrorListener
from pydantic import BaseModel


class ParseError(BaseModel):
    line: int
    column: int
    message: str


@dataclass(frozen=True)
class Issue:
    """One validation/resolution finding: error-severity fails a run, warning does not."""

    code: str
    severity: Literal["error", "warning"]
    message: str


class CollectingErrorListener(ErrorListener):
    """Silent ANTLR listener that records every diagnostic instead of printing."""

    def __init__(self, collected_errors: list[ParseError]) -> None:
        """Create a new :class:`CollectingErrorListener` with a list of collected errors
        passed by reference.

        Args:
            collected_errors (list[ParseError]): the list to populate with collected errors
        """
        self.__collected_errors = collected_errors

    def syntaxError(
        self,
        recognizer,
        offendingSymbol,
        line: int,
        column: int,
        msg: str,
        e,
    ) -> None:
        self.__collected_errors.append(
            ParseError(line=line, column=column, message=msg)
        )
