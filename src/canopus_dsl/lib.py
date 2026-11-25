from typing import Any, Literal

from pydantic import BaseModel

from canopus_dsl.errors import ParseError
from canopus_dsl.generated.CanopusDSLListener import CanopusDSLListener
from canopus_dsl.generated.CanopusDSLParser import CanopusDSLParser

# Pydantic model

MultiplicityOperators = Literal["*", "+", "1"]


class Expr(BaseModel):
    multiplicity: MultiplicityOperators = "1"


class Condition(BaseModel):
    key: str
    op: str
    value: str


class ElementExpr(Expr):
    conditions: list[Condition]


class SequenceExpr(Expr):
    """A ``->`` step sequence: each group alternative is one mini-pipeline."""

    steps: list["Expr"]


class AlternativeExpr(Expr):
    alternatives: list["Expr"]  # single Expr or SequenceExpr per alternative


class IdExpr(Expr):
    name: str


class StartExpr(BaseModel):
    name: Literal["#start"] = "#start"


class EndExpr(BaseModel):
    name: Literal["#end"] = "#end"


class WildcardExpr(Expr):
    name: Literal["*"] = "*"


class Pattern(BaseModel):
    name: str
    sequence: list[Expr | StartExpr | EndExpr | WildcardExpr]


class Program(BaseModel):
    patterns: list[Pattern]
    imports: list[str]


# Concrete listener


class ConcreteCanopusDSLListener(CanopusDSLListener):
    def __init__(self) -> None:
        self.program: Program | None = None
        self.errors: list[ParseError] = []
        self.__values: list[Any] = []  # stack
        self.__patterns: list[Pattern] = []
        self.__imports: list[str] = []

    # ------------------------------------
    # program
    # ------------------------------------
    def exitProgram(self, ctx: CanopusDSLParser.ProgramContext) -> None:
        self.program = Program(patterns=self.__patterns, imports=self.__imports)

    # ------------------------------------
    # patternDef : 'pattern' ID '=' patternExpr
    # ------------------------------------
    def exitPatternDef(self, ctx: CanopusDSLParser.PatternDefContext) -> None:
        pattern_name = ctx.ID().getText()
        pattern_expr = self.__values.pop()
        pattern = Pattern(name=pattern_name, sequence=pattern_expr)
        self.__patterns.append(pattern)

    # ------------------------------------
    # patternExpr : START_OP '->' middleExpr '->' END_OP
    #             | START_OP '->' middleExpr
    #             | middleExpr '->' END_OP
    #             | middleExpr
    # ------------------------------------
    def exitPatternExpr(self, ctx: CanopusDSLParser.PatternExprContext) -> None:
        seq = self.__values.pop() if self.__values else []  # list of Expr
        if ctx.START_OP():
            seq = [StartExpr()] + seq
        if ctx.END_OP():
            seq = seq + [EndExpr()]
        self.__values.append(seq)

    # ------------------------------------
    # middleExpr : multipExpr ('->' multipExpr)*
    # ------------------------------------
    def exitMiddleExpr(self, ctx: CanopusDSLParser.MiddleExprContext) -> None:
        count = len(ctx.multipExpr())
        items = []

        # pop items in reverse construction order
        for _ in range(count):
            items.append(self.__values.pop())

        items.reverse()
        self.__values.append(items)

    # ------------------------------------
    # multipExpr : WILDCARD # wildcardAtom
    #            | primary multipOperator? # quantified
    # ------------------------------------
    def exitWildcardAtom(self, ctx: CanopusDSLParser.WildcardAtomContext) -> None:
        self.__values.append(WildcardExpr())

    def exitQuantified(self, ctx: CanopusDSLParser.QuantifiedContext) -> None:
        if ctx.multipOperator():
            last_expr: Expr = self.__values[-1]
            last_expr.multiplicity = ctx.multipOperator().getText()

    # ------------------------------------
    # alternativeExpr : '(' expr ('|' expr)* ')'
    # ------------------------------------
    def exitAlternativeExpr(self, ctx: CanopusDSLParser.AlternativeExprContext) -> None:
        expr_count = 1 + len(ctx.expr()) - 1
        items = []

        for _ in range(expr_count):
            items.append(self.__values.pop())

        items.reverse()

        alt = AlternativeExpr(alternatives=items)
        self.__values.append(alt)

    # ------------------------------------
    # elementExpr : '[' condition (',' condition)* ']'
    # ------------------------------------
    def exitElementExpr(self, ctx: CanopusDSLParser.ElementExprContext) -> None:
        cond_count = len(ctx.condition())
        conds = []

        for _ in range(cond_count):
            conds.append(self.__values.pop())

        conds.reverse()
        self.__values.append(ElementExpr(conditions=conds))

    # ------------------------------------
    # id : ID
    # ------------------------------------
    def exitId(self, ctx: CanopusDSLParser.IdContext) -> None:
        self.__values.append(IdExpr(name=ctx.ID().getText()))

    # ------------------------------------
    # expr : multipExpr ('->' multipExpr)*
    # (not directly used in final pattern, but used for alternatives)
    # ------------------------------------
    def exitExpr(self, ctx: CanopusDSLParser.ExprContext) -> None:
        count = len(ctx.multipExpr())
        items = []

        for _ in range(count):
            items.append(self.__values.pop())

        items.reverse()

        # a multi-step expr is a SequenceExpr; a single step stays the Expr
        if len(items) == 1:
            self.__values.append(items[0])
        else:
            self.__values.append(SequenceExpr(steps=items))

    # ------------------------------------
    # condition : ID comparator STRING
    # ------------------------------------
    def exitCondition(self, ctx: CanopusDSLParser.ConditionContext) -> None:
        key = ctx.LABEL().getText()
        op = ctx.comparator().getText()
        value = ctx.STRING().getText().strip('"')
        self.__values.append(Condition(key=key, op=op, value=value))

    # ------------------------------------
    # imports : 'import' ID (',' ID)*
    # ------------------------------------
    def exitImportPatterns(self, ctx: CanopusDSLParser.ImportPatternsContext) -> None:
        self.__imports.extend([import_id.getText() for import_id in ctx.ID()])
