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
        4,1,20,119,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,4,0,30,8,0,11,0,12,0,31,1,0,1,0,1,1,1,1,1,1,1,1,5,1,40,8,
        1,10,1,12,1,43,9,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,64,8,3,1,4,1,4,1,4,5,4,69,8,4,
        10,4,12,4,72,9,4,1,5,1,5,3,5,76,8,5,1,6,1,6,1,6,1,6,4,6,82,8,6,11,
        6,12,6,83,1,6,1,6,1,6,1,6,1,6,1,6,5,6,92,8,6,10,6,12,6,95,9,6,1,
        6,1,6,1,6,1,6,3,6,101,8,6,1,7,1,7,1,8,1,8,1,8,5,8,108,8,8,10,8,12,
        8,111,9,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,
        14,16,18,20,0,2,2,0,11,11,19,19,2,0,4,4,12,12,121,0,25,1,0,0,0,2,
        35,1,0,0,0,4,44,1,0,0,0,6,63,1,0,0,0,8,65,1,0,0,0,10,73,1,0,0,0,
        12,100,1,0,0,0,14,102,1,0,0,0,16,104,1,0,0,0,18,112,1,0,0,0,20,116,
        1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,
        25,26,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,28,30,3,4,2,0,29,28,1,
        0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,0,33,
        34,5,0,0,1,34,1,1,0,0,0,35,36,5,1,0,0,36,41,5,15,0,0,37,38,5,2,0,
        0,38,40,5,15,0,0,39,37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,
        1,0,0,0,42,3,1,0,0,0,43,41,1,0,0,0,44,45,5,3,0,0,45,46,5,15,0,0,
        46,47,5,4,0,0,47,48,3,6,3,0,48,5,1,0,0,0,49,50,5,13,0,0,50,51,5,
        5,0,0,51,52,3,8,4,0,52,53,5,5,0,0,53,54,5,14,0,0,54,64,1,0,0,0,55,
        56,5,13,0,0,56,57,5,5,0,0,57,64,3,8,4,0,58,59,3,8,4,0,59,60,5,5,
        0,0,60,61,5,14,0,0,61,64,1,0,0,0,62,64,3,8,4,0,63,49,1,0,0,0,63,
        55,1,0,0,0,63,58,1,0,0,0,63,62,1,0,0,0,64,7,1,0,0,0,65,70,3,10,5,
        0,66,67,5,5,0,0,67,69,3,10,5,0,68,66,1,0,0,0,69,72,1,0,0,0,70,68,
        1,0,0,0,70,71,1,0,0,0,71,9,1,0,0,0,72,70,1,0,0,0,73,75,3,12,6,0,
        74,76,3,14,7,0,75,74,1,0,0,0,75,76,1,0,0,0,76,11,1,0,0,0,77,78,5,
        6,0,0,78,81,3,16,8,0,79,80,5,7,0,0,80,82,3,16,8,0,81,79,1,0,0,0,
        82,83,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,85,1,0,0,0,85,86,5,
        8,0,0,86,101,1,0,0,0,87,88,5,9,0,0,88,93,3,18,9,0,89,90,5,2,0,0,
        90,92,3,18,9,0,91,89,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,
        0,0,0,94,96,1,0,0,0,95,93,1,0,0,0,96,97,5,10,0,0,97,101,1,0,0,0,
        98,101,5,15,0,0,99,101,5,19,0,0,100,77,1,0,0,0,100,87,1,0,0,0,100,
        98,1,0,0,0,100,99,1,0,0,0,101,13,1,0,0,0,102,103,7,0,0,0,103,15,
        1,0,0,0,104,109,3,12,6,0,105,106,5,5,0,0,106,108,3,12,6,0,107,105,
        1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,17,1,
        0,0,0,111,109,1,0,0,0,112,113,5,16,0,0,113,114,3,20,10,0,114,115,
        5,17,0,0,115,19,1,0,0,0,116,117,7,1,0,0,117,21,1,0,0,0,10,25,31,
        41,63,70,75,83,93,100,109
    ]

class CanopusDSLParser ( Parser ):

    grammarFileName = "CanopusDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'import'", "','", "'pattern'", "'='", 
                     "'->'", "'('", "'|'", "')'", "'['", "']'", "'+'", "'!='", 
                     "'start'", "'end'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "START_OP", "END_OP", "ID", "LABEL", 
                      "STRING", "WS", "WILDCARD", "COMMENT" ]

    RULE_program = 0
    RULE_importPatterns = 1
    RULE_patternDef = 2
    RULE_patternExpr = 3
    RULE_middleExpr = 4
    RULE_multipExpr = 5
    RULE_primary = 6
    RULE_multipOperator = 7
    RULE_expr = 8
    RULE_condition = 9
    RULE_comparator = 10

    ruleNames =  [ "program", "importPatterns", "patternDef", "patternExpr", 
                   "middleExpr", "multipExpr", "primary", "multipOperator", 
                   "expr", "condition", "comparator" ]

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
    T__11=12
    START_OP=13
    END_OP=14
    ID=15
    LABEL=16
    STRING=17
    WS=18
    WILDCARD=19
    COMMENT=20

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

        def importPatterns(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CanopusDSLParser.ImportPatternsContext)
            else:
                return self.getTypedRuleContext(CanopusDSLParser.ImportPatternsContext,i)


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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 22
                self.importPatterns()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.patternDef()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

            self.state = 33
            self.match(CanopusDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportPatternsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CanopusDSLParser.ID)
            else:
                return self.getToken(CanopusDSLParser.ID, i)

        def getRuleIndex(self):
            return CanopusDSLParser.RULE_importPatterns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportPatterns" ):
                listener.enterImportPatterns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportPatterns" ):
                listener.exitImportPatterns(self)




    def importPatterns(self):

        localctx = CanopusDSLParser.ImportPatternsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_importPatterns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(CanopusDSLParser.T__0)
            self.state = 36
            self.match(CanopusDSLParser.ID)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 37
                self.match(CanopusDSLParser.T__1)
                self.state = 38
                self.match(CanopusDSLParser.ID)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 4, self.RULE_patternDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(CanopusDSLParser.T__2)
            self.state = 45
            self.match(CanopusDSLParser.ID)
            self.state = 46
            self.match(CanopusDSLParser.T__3)
            self.state = 47
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
        self.enterRule(localctx, 6, self.RULE_patternExpr)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(CanopusDSLParser.START_OP)
                self.state = 50
                self.match(CanopusDSLParser.T__4)
                self.state = 51
                self.middleExpr()
                self.state = 52
                self.match(CanopusDSLParser.T__4)
                self.state = 53
                self.match(CanopusDSLParser.END_OP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(CanopusDSLParser.START_OP)
                self.state = 56
                self.match(CanopusDSLParser.T__4)
                self.state = 57
                self.middleExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.middleExpr()
                self.state = 59
                self.match(CanopusDSLParser.T__4)
                self.state = 60
                self.match(CanopusDSLParser.END_OP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
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
        self.enterRule(localctx, 8, self.RULE_middleExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.multipExpr()
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 66
                    self.match(CanopusDSLParser.T__4)
                    self.state = 67
                    self.multipExpr() 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self.enterRule(localctx, 10, self.RULE_multipExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.primary()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11 or _la==19:
                self.state = 74
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
        self.enterRule(localctx, 12, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = CanopusDSLParser.AlternativeExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(CanopusDSLParser.T__5)
                self.state = 78
                self.expr()
                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 79
                    self.match(CanopusDSLParser.T__6)
                    self.state = 80
                    self.expr()
                    self.state = 83 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==7):
                        break

                self.state = 85
                self.match(CanopusDSLParser.T__7)
                pass
            elif token in [9]:
                localctx = CanopusDSLParser.ElementExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(CanopusDSLParser.T__8)
                self.state = 88
                self.condition()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 89
                    self.match(CanopusDSLParser.T__1)
                    self.state = 90
                    self.condition()
                    self.state = 95
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 96
                self.match(CanopusDSLParser.T__9)
                pass
            elif token in [15]:
                localctx = CanopusDSLParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.match(CanopusDSLParser.ID)
                pass
            elif token in [19]:
                localctx = CanopusDSLParser.WildcardContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 99
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
        self.enterRule(localctx, 14, self.RULE_multipOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not(_la==11 or _la==19):
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
        self.enterRule(localctx, 16, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.primary()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 105
                self.match(CanopusDSLParser.T__4)
                self.state = 106
                self.primary()
                self.state = 111
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
        self.enterRule(localctx, 18, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(CanopusDSLParser.LABEL)
            self.state = 113
            self.comparator()
            self.state = 114
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
        self.enterRule(localctx, 20, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not(_la==4 or _la==12):
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





