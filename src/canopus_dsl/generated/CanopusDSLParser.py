# Generated from ./CanopusDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,3,2,47,8,2,1,3,1,3,1,3,5,3,52,8,3,10,3,12,3,55,9,3,1,4,
        1,4,3,4,59,8,4,1,5,1,5,1,5,1,5,4,5,65,8,5,11,5,12,5,66,1,5,1,5,1,
        5,1,5,1,5,1,5,5,5,75,8,5,10,5,12,5,78,9,5,1,5,1,5,1,5,1,5,3,5,84,
        8,5,1,6,1,6,1,7,1,7,1,7,5,7,91,8,7,10,7,12,7,94,9,7,1,8,1,8,1,8,
        1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,2,2,0,10,10,18,
        18,2,0,2,2,11,11,103,0,21,1,0,0,0,2,27,1,0,0,0,4,46,1,0,0,0,6,48,
        1,0,0,0,8,56,1,0,0,0,10,83,1,0,0,0,12,85,1,0,0,0,14,87,1,0,0,0,16,
        95,1,0,0,0,18,99,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,
        0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,26,5,0,0,1,26,1,1,
        0,0,0,27,28,5,1,0,0,28,29,5,14,0,0,29,30,5,2,0,0,30,31,3,4,2,0,31,
        3,1,0,0,0,32,33,5,12,0,0,33,34,5,3,0,0,34,35,3,6,3,0,35,36,5,3,0,
        0,36,37,5,13,0,0,37,47,1,0,0,0,38,39,5,12,0,0,39,40,5,3,0,0,40,47,
        3,6,3,0,41,42,3,6,3,0,42,43,5,3,0,0,43,44,5,13,0,0,44,47,1,0,0,0,
        45,47,3,6,3,0,46,32,1,0,0,0,46,38,1,0,0,0,46,41,1,0,0,0,46,45,1,
        0,0,0,47,5,1,0,0,0,48,53,3,8,4,0,49,50,5,3,0,0,50,52,3,8,4,0,51,
        49,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,7,1,0,0,
        0,55,53,1,0,0,0,56,58,3,10,5,0,57,59,3,12,6,0,58,57,1,0,0,0,58,59,
        1,0,0,0,59,9,1,0,0,0,60,61,5,4,0,0,61,64,3,14,7,0,62,63,5,5,0,0,
        63,65,3,14,7,0,64,62,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,
        0,0,0,67,68,1,0,0,0,68,69,5,6,0,0,69,84,1,0,0,0,70,71,5,7,0,0,71,
        76,3,16,8,0,72,73,5,8,0,0,73,75,3,16,8,0,74,72,1,0,0,0,75,78,1,0,
        0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,
        5,9,0,0,80,84,1,0,0,0,81,84,5,14,0,0,82,84,5,18,0,0,83,60,1,0,0,
        0,83,70,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,11,1,0,0,0,85,86,
        7,0,0,0,86,13,1,0,0,0,87,92,3,10,5,0,88,89,5,3,0,0,89,91,3,10,5,
        0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,15,
        1,0,0,0,94,92,1,0,0,0,95,96,5,15,0,0,96,97,3,18,9,0,97,98,5,16,0,
        0,98,17,1,0,0,0,99,100,7,1,0,0,100,19,1,0,0,0,8,23,46,53,58,66,76,
        83,92
    ]

class CanopusDSLParser ( Parser ):

    grammarFileName = "CanopusDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'pattern'", "'='", "'->'", "'('", "'|'", 
                     "')'", "'['", "','", "']'", "'+'", "'!='", "'start'", 
                     "'end'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "START_OP", "END_OP", "ID", "LABEL", "STRING", "WS", 
                      "WILDCARD" ]

    RULE_program = 0
    RULE_patternDef = 1
    RULE_patternExpr = 2
    RULE_middleExpr = 3
    RULE_multipExpr = 4
    RULE_primary = 5
    RULE_multipOperator = 6
    RULE_expr = 7
    RULE_condition = 8
    RULE_comparator = 9

    ruleNames =  [ "program", "patternDef", "patternExpr", "middleExpr", 
                   "multipExpr", "primary", "multipOperator", "expr", "condition", 
                   "comparator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    START_OP=12
    END_OP=13
    ID=14
    LABEL=15
    STRING=16
    WS=17
    WILDCARD=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CanopusDSLParser.EOF, 0)

        def patternDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CanopusDSLParser.PatternDefContext)
            else:
                return self.getTypedRuleContext(CanopusDSLParser.PatternDefContext,i)


        def getRuleIndex(self):
            return CanopusDSLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = CanopusDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.patternDef()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 25
            self.match(CanopusDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CanopusDSLParser.ID, 0)

        def patternExpr(self):
            return self.getTypedRuleContext(CanopusDSLParser.PatternExprContext,0)


        def getRuleIndex(self):
            return CanopusDSLParser.RULE_patternDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternDef" ):
                listener.enterPatternDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternDef" ):
                listener.exitPatternDef(self)




    def patternDef(self):

        localctx = CanopusDSLParser.PatternDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_patternDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(CanopusDSLParser.T__0)
            self.state = 28
            self.match(CanopusDSLParser.ID)
            self.state = 29
            self.match(CanopusDSLParser.T__1)
            self.state = 30
            self.patternExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START_OP(self):
            return self.getToken(CanopusDSLParser.START_OP, 0)

        def middleExpr(self):
            return self.getTypedRuleContext(CanopusDSLParser.MiddleExprContext,0)


        def END_OP(self):
            return self.getToken(CanopusDSLParser.END_OP, 0)

        def getRuleIndex(self):
            return CanopusDSLParser.RULE_patternExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternExpr" ):
                listener.enterPatternExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternExpr" ):
                listener.exitPatternExpr(self)




    def patternExpr(self):

        localctx = CanopusDSLParser.PatternExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_patternExpr)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(CanopusDSLParser.START_OP)
                self.state = 33
                self.match(CanopusDSLParser.T__2)
                self.state = 34
                self.middleExpr()
                self.state = 35
                self.match(CanopusDSLParser.T__2)
                self.state = 36
                self.match(CanopusDSLParser.END_OP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(CanopusDSLParser.START_OP)
                self.state = 39
                self.match(CanopusDSLParser.T__2)
                self.state = 40
                self.middleExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.middleExpr()
                self.state = 42
                self.match(CanopusDSLParser.T__2)
                self.state = 43
                self.match(CanopusDSLParser.END_OP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.middleExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MiddleExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multipExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CanopusDSLParser.MultipExprContext)
            else:
                return self.getTypedRuleContext(CanopusDSLParser.MultipExprContext,i)


        def getRuleIndex(self):
            return CanopusDSLParser.RULE_middleExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMiddleExpr" ):
                listener.enterMiddleExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMiddleExpr" ):
                listener.exitMiddleExpr(self)




    def middleExpr(self):

        localctx = CanopusDSLParser.MiddleExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_middleExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.multipExpr()
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 49
                    self.match(CanopusDSLParser.T__2)
                    self.state = 50
                    self.multipExpr() 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultipExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(CanopusDSLParser.PrimaryContext,0)


        def multipOperator(self):
            return self.getTypedRuleContext(CanopusDSLParser.MultipOperatorContext,0)


        def getRuleIndex(self):
            return CanopusDSLParser.RULE_multipExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultipExpr" ):
                listener.enterMultipExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultipExpr" ):
                listener.exitMultipExpr(self)




    def multipExpr(self):

        localctx = CanopusDSLParser.MultipExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_multipExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.primary()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==18:
                self.state = 57
                self.multipOperator()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CanopusDSLParser.RULE_primary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AlternativeExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CanopusDSLParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CanopusDSLParser.ExprContext)
            else:
                return self.getTypedRuleContext(CanopusDSLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlternativeExpr" ):
                listener.enterAlternativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlternativeExpr" ):
                listener.exitAlternativeExpr(self)


    class ElementExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CanopusDSLParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CanopusDSLParser.ConditionContext)
            else:
                return self.getTypedRuleContext(CanopusDSLParser.ConditionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementExpr" ):
                listener.enterElementExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementExpr" ):
                listener.exitElementExpr(self)


    class IdContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CanopusDSLParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CanopusDSLParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class WildcardContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CanopusDSLParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WILDCARD(self):
            return self.getToken(CanopusDSLParser.WILDCARD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWildcard" ):
                listener.enterWildcard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWildcard" ):
                listener.exitWildcard(self)



    def primary(self):

        localctx = CanopusDSLParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = CanopusDSLParser.AlternativeExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(CanopusDSLParser.T__3)
                self.state = 61
                self.expr()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 62
                    self.match(CanopusDSLParser.T__4)
                    self.state = 63
                    self.expr()
                    self.state = 66 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==5):
                        break

                self.state = 68
                self.match(CanopusDSLParser.T__5)
                pass
            elif token in [7]:
                localctx = CanopusDSLParser.ElementExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(CanopusDSLParser.T__6)
                self.state = 71
                self.condition()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 72
                    self.match(CanopusDSLParser.T__7)
                    self.state = 73
                    self.condition()
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 79
                self.match(CanopusDSLParser.T__8)
                pass
            elif token in [14]:
                localctx = CanopusDSLParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.match(CanopusDSLParser.ID)
                pass
            elif token in [18]:
                localctx = CanopusDSLParser.WildcardContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.match(CanopusDSLParser.WILDCARD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultipOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WILDCARD(self):
            return self.getToken(CanopusDSLParser.WILDCARD, 0)

        def getRuleIndex(self):
            return CanopusDSLParser.RULE_multipOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultipOperator" ):
                listener.enterMultipOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultipOperator" ):
                listener.exitMultipOperator(self)




    def multipOperator(self):

        localctx = CanopusDSLParser.MultipOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_multipOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not(_la==10 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CanopusDSLParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(CanopusDSLParser.PrimaryContext,i)


        def getRuleIndex(self):
            return CanopusDSLParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = CanopusDSLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.primary()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 88
                self.match(CanopusDSLParser.T__2)
                self.state = 89
                self.primary()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL(self):
            return self.getToken(CanopusDSLParser.LABEL, 0)

        def comparator(self):
            return self.getTypedRuleContext(CanopusDSLParser.ComparatorContext,0)


        def STRING(self):
            return self.getToken(CanopusDSLParser.STRING, 0)

        def getRuleIndex(self):
            return CanopusDSLParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = CanopusDSLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(CanopusDSLParser.LABEL)
            self.state = 96
            self.comparator()
            self.state = 97
            self.match(CanopusDSLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CanopusDSLParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)




    def comparator(self):

        localctx = CanopusDSLParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not(_la==2 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





