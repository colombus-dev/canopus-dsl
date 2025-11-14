# Generated from ./CanopusDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CanopusDSLParser import CanopusDSLParser
else:
    from CanopusDSLParser import CanopusDSLParser

# This class defines a complete listener for a parse tree produced by CanopusDSLParser.
class CanopusDSLListener(ParseTreeListener):

    # Enter a parse tree produced by CanopusDSLParser#program.
    def enterProgram(self, ctx:CanopusDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by CanopusDSLParser#program.
    def exitProgram(self, ctx:CanopusDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by CanopusDSLParser#patternDef.
    def enterPatternDef(self, ctx:CanopusDSLParser.PatternDefContext):
        pass

    # Exit a parse tree produced by CanopusDSLParser#patternDef.
    def exitPatternDef(self, ctx:CanopusDSLParser.PatternDefContext):
        pass


    # Enter a parse tree produced by CanopusDSLParser#patternExpr.
    def enterPatternExpr(self, ctx:CanopusDSLParser.PatternExprContext):
        pass

    # Exit a parse tree produced by CanopusDSLParser#patternExpr.
    def exitPatternExpr(self, ctx:CanopusDSLParser.PatternExprContext):
        pass


    # Enter a parse tree produced by CanopusDSLParser#middleExpr.
    def enterMiddleExpr(self, ctx:CanopusDSLParser.MiddleExprContext):
        pass

    # Exit a parse tree produced by CanopusDSLParser#middleExpr.
    def exitMiddleExpr(self, ctx:CanopusDSLParser.MiddleExprContext):
        pass


    # Enter a parse tree produced by CanopusDSLParser#multipExpr.
    def enterMultipExpr(self, ctx:CanopusDSLParser.MultipExprContext):
        pass

    # Exit a parse tree produced by CanopusDSLParser#multipExpr.
    def exitMultipExpr(self, ctx:CanopusDSLParser.MultipExprContext):
        pass


    # Enter a parse tree produced by CanopusDSLParser#alternativeExpr.
    def enterAlternativeExpr(self, ctx:CanopusDSLParser.AlternativeExprContext):
        pass

    # Exit a parse tree produced by CanopusDSLParser#alternativeExpr.
    def exitAlternativeExpr(self, ctx:CanopusDSLParser.AlternativeExprContext):
        pass


    # Enter a parse tree produced by CanopusDSLParser#elementExpr.
    def enterElementExpr(self, ctx:CanopusDSLParser.ElementExprContext):
        pass

    # Exit a parse tree produced by CanopusDSLParser#elementExpr.
    def exitElementExpr(self, ctx:CanopusDSLParser.ElementExprContext):
        pass


    # Enter a parse tree produced by CanopusDSLParser#id.
    def enterId(self, ctx:CanopusDSLParser.IdContext):
        pass

    # Exit a parse tree produced by CanopusDSLParser#id.
    def exitId(self, ctx:CanopusDSLParser.IdContext):
        pass


    # Enter a parse tree produced by CanopusDSLParser#wildcard.
    def enterWildcard(self, ctx:CanopusDSLParser.WildcardContext):
        pass

    # Exit a parse tree produced by CanopusDSLParser#wildcard.
    def exitWildcard(self, ctx:CanopusDSLParser.WildcardContext):
        pass


    # Enter a parse tree produced by CanopusDSLParser#multipOperator.
    def enterMultipOperator(self, ctx:CanopusDSLParser.MultipOperatorContext):
        pass

    # Exit a parse tree produced by CanopusDSLParser#multipOperator.
    def exitMultipOperator(self, ctx:CanopusDSLParser.MultipOperatorContext):
        pass


    # Enter a parse tree produced by CanopusDSLParser#expr.
    def enterExpr(self, ctx:CanopusDSLParser.ExprContext):
        pass

    # Exit a parse tree produced by CanopusDSLParser#expr.
    def exitExpr(self, ctx:CanopusDSLParser.ExprContext):
        pass


    # Enter a parse tree produced by CanopusDSLParser#condition.
    def enterCondition(self, ctx:CanopusDSLParser.ConditionContext):
        pass

    # Exit a parse tree produced by CanopusDSLParser#condition.
    def exitCondition(self, ctx:CanopusDSLParser.ConditionContext):
        pass


    # Enter a parse tree produced by CanopusDSLParser#comparator.
    def enterComparator(self, ctx:CanopusDSLParser.ComparatorContext):
        pass

    # Exit a parse tree produced by CanopusDSLParser#comparator.
    def exitComparator(self, ctx:CanopusDSLParser.ComparatorContext):
        pass



del CanopusDSLParser