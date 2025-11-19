from pydantic import BaseModel
from typing import Any, List, Literal

from canopus_dsl.generated.CanopusDSLParser import CanopusDSLParser
from canopus_dsl.generated.CanopusDSLListener import CanopusDSLListener

# Pydantic model

MultiplicityOperators = Literal["*", "+", "1"]


class Expr(BaseModel):
    multiplicity: MultiplicityOperators = "1"


class Condition(BaseModel):
    key: str
    op: str
    value: str


class ElementExpr(Expr):
    conditions: List[Condition]


class AlternativeExpr(Expr):
    alternatives: List["Expr"]  # forward reference


class IdExpr(Expr):
    name: str


class StartExpr(BaseModel):
    name: Literal["#start"] = "#start"


class EndExpr(BaseModel):
    name: Literal["#end"] = "#end"


class WildcardExpr(BaseModel):
    name: Literal["*"] = "*"


class Pattern(BaseModel):
    name: str
    sequence: List[Expr | StartExpr | EndExpr | WildcardExpr]


class Program(BaseModel):
    patterns: List[Pattern]
    imports: List[str]


# Concrete listener


class ConcreteCanopusDSLListener(CanopusDSLListener):
    def __init__(self):
        self.program: Program | None = None
        self.__values: List[Any] = []  # stack
        self.__patterns: List[Pattern] = []
        self.__imports: List[str] = []

    # ------------------------------------
    # program
    # ------------------------------------
    def exitProgram(self, ctx: CanopusDSLParser.ProgramContext):
        self.program = Program(patterns=self.__patterns, imports=self.__imports)

    # ------------------------------------
    # patternDef : 'pattern' ID '=' patternExpr
    # ------------------------------------
    def exitPatternDef(self, ctx: CanopusDSLParser.PatternDefContext):
        pattern_name = ctx.ID().getText()
        pattern_expr = self.__values.pop()
        pattern = Pattern(name=pattern_name, sequence=pattern_expr)
        self.__patterns.append(pattern)

    # ------------------------------------
    # patternExpr : START_OP '->' middleExpr '->' END_OP
    #             | START_OP '->' END_OP
    # ------------------------------------
    def exitPatternExpr(self, ctx: CanopusDSLParser.PatternExprContext):
        seq = self.__values.pop() if self.__values else []  # list of Expr
        if ctx.START_OP():
            seq = [StartExpr()] + seq
        if ctx.END_OP():
            seq = seq + [EndExpr()]
        self.__values.append(seq)

    # ------------------------------------
    # middleExpr : primary ('->' primary)*
    # ------------------------------------
    def exitMiddleExpr(self, ctx: CanopusDSLParser.MiddleExprContext):
        count = len(ctx.multipExpr())
        items = []

        # pop items in reverse construction order
        for _ in range(count):
            items.append(self.__values.pop())

        items.reverse()
        self.__values.append(items)

    # ------------------------------------
    # multipExpr : primary multipOperator?
    # ------------------------------------
    def exitMultipExpr(self, ctx: CanopusDSLParser.MultipExprContext):
        if ctx.multipOperator():
            last_expr: Expr = self.__values[-1]
            last_expr.multiplicity = ctx.multipOperator().getText()

    # ------------------------------------
    # alternativeExpr : '(' expr ('|' expr)+ ')'
    # ------------------------------------
    def exitAlternativeExpr(self, ctx: CanopusDSLParser.AlternativeExprContext):
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
    def exitElementExpr(self, ctx: CanopusDSLParser.ElementExprContext):
        cond_count = len(ctx.condition())
        conds = []

        for _ in range(cond_count):
            conds.append(self.__values.pop())

        conds.reverse()
        self.__values.append(ElementExpr(conditions=conds))

    # ------------------------------------
    # id : ID
    # ------------------------------------
    def exitId(self, ctx: CanopusDSLParser.IdContext):
        self.__values.append(IdExpr(name=ctx.ID().getText()))

    # ------------------------------------
    # wildcard : '*'
    # ------------------------------------
    def exitWildcard(self, ctx: CanopusDSLParser.WildcardContext):
        self.__values.append(WildcardExpr())

    # ------------------------------------
    # expr : primary ('->' primary)*
    # (not directly used in final pattern, but used for alternatives)
    # ------------------------------------
    def exitExpr(self, ctx: CanopusDSLParser.ExprContext):
        count = len(ctx.primary())
        items = []

        for _ in range(count):
            items.append(self.__values.pop())

        items.reverse()

        # if only one primary, expr = that primary
        if len(items) == 1:
            self.__values.append(items[0])
        else:
            # treat full expr as sequence of primaries
            self.__values.append(items)

    # ------------------------------------
    # condition : ID comparator STRING
    # ------------------------------------
    def exitCondition(self, ctx: CanopusDSLParser.ConditionContext):
        key = ctx.LABEL().getText()
        op = ctx.comparator().getText()
        value = ctx.STRING().getText().strip('"')
        self.__values.append(Condition(key=key, op=op, value=value))

    # ------------------------------------
    # imports : 'import' ID (',' ID)*
    # ------------------------------------
    def exitImportPatterns(self, ctx: CanopusDSLParser.ImportPatternsContext):
        self.__imports.extend([import_id.getText() for import_id in ctx.ID()])
