// Generated from ./CanopusDSL.g4 by ANTLR 4.13.2
// jshint ignore: start
import antlr4 from 'antlr4';
import CanopusDSLListener from './CanopusDSLListener.js';
const serializedATN = [4,1,20,117,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,
4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,4,0,25,8,0,11,
0,12,0,26,1,0,1,0,1,1,1,1,1,1,1,1,5,1,35,8,1,10,1,12,1,38,9,1,1,2,1,2,1,
2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,59,
8,3,1,4,1,4,1,4,5,4,64,8,4,10,4,12,4,67,9,4,1,5,1,5,1,5,3,5,72,8,5,3,5,74,
8,5,1,6,1,6,1,6,1,6,5,6,80,8,6,10,6,12,6,83,9,6,1,6,1,6,1,6,1,6,1,6,1,6,
5,6,91,8,6,10,6,12,6,94,9,6,1,6,1,6,1,6,3,6,99,8,6,1,7,1,7,1,8,1,8,1,8,5,
8,106,8,8,10,8,12,8,109,9,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,
6,8,10,12,14,16,18,20,0,2,2,0,11,11,19,19,2,0,4,4,12,12,119,0,24,1,0,0,0,
2,30,1,0,0,0,4,39,1,0,0,0,6,58,1,0,0,0,8,60,1,0,0,0,10,73,1,0,0,0,12,98,
1,0,0,0,14,100,1,0,0,0,16,102,1,0,0,0,18,110,1,0,0,0,20,114,1,0,0,0,22,25,
3,2,1,0,23,25,3,4,2,0,24,22,1,0,0,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,
0,0,0,26,27,1,0,0,0,27,28,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,31,5,1,0,
0,31,36,5,15,0,0,32,33,5,2,0,0,33,35,5,15,0,0,34,32,1,0,0,0,35,38,1,0,0,
0,36,34,1,0,0,0,36,37,1,0,0,0,37,3,1,0,0,0,38,36,1,0,0,0,39,40,5,3,0,0,40,
41,5,15,0,0,41,42,5,4,0,0,42,43,3,6,3,0,43,5,1,0,0,0,44,45,5,13,0,0,45,46,
5,5,0,0,46,47,3,8,4,0,47,48,5,5,0,0,48,49,5,14,0,0,49,59,1,0,0,0,50,51,5,
13,0,0,51,52,5,5,0,0,52,59,3,8,4,0,53,54,3,8,4,0,54,55,5,5,0,0,55,56,5,14,
0,0,56,59,1,0,0,0,57,59,3,8,4,0,58,44,1,0,0,0,58,50,1,0,0,0,58,53,1,0,0,
0,58,57,1,0,0,0,59,7,1,0,0,0,60,65,3,10,5,0,61,62,5,5,0,0,62,64,3,10,5,0,
63,61,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,9,1,0,0,0,67,
65,1,0,0,0,68,74,5,19,0,0,69,71,3,12,6,0,70,72,3,14,7,0,71,70,1,0,0,0,71,
72,1,0,0,0,72,74,1,0,0,0,73,68,1,0,0,0,73,69,1,0,0,0,74,11,1,0,0,0,75,76,
5,6,0,0,76,81,3,16,8,0,77,78,5,7,0,0,78,80,3,16,8,0,79,77,1,0,0,0,80,83,
1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,
8,0,0,85,99,1,0,0,0,86,87,5,9,0,0,87,92,3,18,9,0,88,89,5,2,0,0,89,91,3,18,
9,0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,
0,94,92,1,0,0,0,95,96,5,10,0,0,96,99,1,0,0,0,97,99,5,15,0,0,98,75,1,0,0,
0,98,86,1,0,0,0,98,97,1,0,0,0,99,13,1,0,0,0,100,101,7,0,0,0,101,15,1,0,0,
0,102,107,3,10,5,0,103,104,5,5,0,0,104,106,3,10,5,0,105,103,1,0,0,0,106,
109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,17,1,0,0,0,109,107,1,0,0,
0,110,111,5,16,0,0,111,112,3,20,10,0,112,113,5,17,0,0,113,19,1,0,0,0,114,
115,7,1,0,0,115,21,1,0,0,0,11,24,26,36,58,65,71,73,81,92,98,107];


const atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

const decisionsToDFA = atn.decisionToState.map( (ds, index) => new antlr4.dfa.DFA(ds, index) );

const sharedContextCache = new antlr4.atn.PredictionContextCache();

export default class CanopusDSLParser extends antlr4.Parser {

    static grammarFileName = "CanopusDSL.g4";
    static literalNames = [ null, "'import'", "','", "'pattern'", "'='",
                            "'->'", "'('", "'|'", "')'", "'['", "']'", "'+'",
                            "'!='", "'start'", "'end'", null, null, null,
                            null, "'*'" ];
    static symbolicNames = [ null, null, null, null, null, null, null, null,
                             null, null, null, null, null, "START_OP", "END_OP",
                             "ID", "LABEL", "STRING", "WS", "WILDCARD",
                             "COMMENT" ];
    static ruleNames = [ "program", "importPatterns", "patternDef", "patternExpr",
                         "middleExpr", "multipExpr", "primary", "multipOperator",
                         "expr", "condition", "comparator" ];

    constructor(input) {
        super(input);
        this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
        this.ruleNames = CanopusDSLParser.ruleNames;
        this.literalNames = CanopusDSLParser.literalNames;
        this.symbolicNames = CanopusDSLParser.symbolicNames;
    }



	program() {
	    let localctx = new ProgramContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 0, CanopusDSLParser.RULE_program);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 24;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        do {
	            this.state = 24;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case 1:
	                this.state = 22;
	                this.importPatterns();
	                break;
	            case 3:
	                this.state = 23;
	                this.patternDef();
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            this.state = 26;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        } while(_la===1 || _la===3);
	        this.state = 28;
	        this.match(CanopusDSLParser.EOF);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	importPatterns() {
	    let localctx = new ImportPatternsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 2, CanopusDSLParser.RULE_importPatterns);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 30;
	        this.match(CanopusDSLParser.T__0);
	        this.state = 31;
	        this.match(CanopusDSLParser.ID);
	        this.state = 36;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===2) {
	            this.state = 32;
	            this.match(CanopusDSLParser.T__1);
	            this.state = 33;
	            this.match(CanopusDSLParser.ID);
	            this.state = 38;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	patternDef() {
	    let localctx = new PatternDefContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 4, CanopusDSLParser.RULE_patternDef);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 39;
	        this.match(CanopusDSLParser.T__2);
	        this.state = 40;
	        this.match(CanopusDSLParser.ID);
	        this.state = 41;
	        this.match(CanopusDSLParser.T__3);
	        this.state = 42;
	        this.patternExpr();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	patternExpr() {
	    let localctx = new PatternExprContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 6, CanopusDSLParser.RULE_patternExpr);
	    try {
	        this.state = 58;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,3,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 44;
	            this.match(CanopusDSLParser.START_OP);
	            this.state = 45;
	            this.match(CanopusDSLParser.T__4);
	            this.state = 46;
	            this.middleExpr();
	            this.state = 47;
	            this.match(CanopusDSLParser.T__4);
	            this.state = 48;
	            this.match(CanopusDSLParser.END_OP);
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 50;
	            this.match(CanopusDSLParser.START_OP);
	            this.state = 51;
	            this.match(CanopusDSLParser.T__4);
	            this.state = 52;
	            this.middleExpr();
	            break;

	        case 3:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 53;
	            this.middleExpr();
	            this.state = 54;
	            this.match(CanopusDSLParser.T__4);
	            this.state = 55;
	            this.match(CanopusDSLParser.END_OP);
	            break;

	        case 4:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 57;
	            this.middleExpr();
	            break;

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	middleExpr() {
	    let localctx = new MiddleExprContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 8, CanopusDSLParser.RULE_middleExpr);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 60;
	        this.multipExpr();
	        this.state = 65;
	        this._errHandler.sync(this);
	        var _alt = this._interp.adaptivePredict(this._input,4,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                this.state = 61;
	                this.match(CanopusDSLParser.T__4);
	                this.state = 62;
	                this.multipExpr();
	            }
	            this.state = 67;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,4,this._ctx);
	        }

	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	multipExpr() {
	    let localctx = new MultipExprContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 10, CanopusDSLParser.RULE_multipExpr);
	    var _la = 0;
	    try {
	        this.state = 73;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case 19:
	            localctx = new WildcardAtomContext(this, localctx);
	            this.enterOuterAlt(localctx, 1);
	            this.state = 68;
	            this.match(CanopusDSLParser.WILDCARD);
	            break;
	        case 6:
	        case 9:
	        case 15:
	            localctx = new QuantifiedContext(this, localctx);
	            this.enterOuterAlt(localctx, 2);
	            this.state = 69;
	            this.primary();
	            this.state = 71;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===11 || _la===19) {
	                this.state = 70;
	                this.multipOperator();
	            }

	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	primary() {
	    let localctx = new PrimaryContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 12, CanopusDSLParser.RULE_primary);
	    var _la = 0;
	    try {
	        this.state = 98;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case 6:
	            localctx = new AlternativeExprContext(this, localctx);
	            this.enterOuterAlt(localctx, 1);
	            this.state = 75;
	            this.match(CanopusDSLParser.T__5);
	            this.state = 76;
	            this.expr();
	            this.state = 81;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            while(_la===7) {
	                this.state = 77;
	                this.match(CanopusDSLParser.T__6);
	                this.state = 78;
	                this.expr();
	                this.state = 83;
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            }
	            this.state = 84;
	            this.match(CanopusDSLParser.T__7);
	            break;
	        case 9:
	            localctx = new ElementExprContext(this, localctx);
	            this.enterOuterAlt(localctx, 2);
	            this.state = 86;
	            this.match(CanopusDSLParser.T__8);
	            this.state = 87;
	            this.condition();
	            this.state = 92;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            while(_la===2) {
	                this.state = 88;
	                this.match(CanopusDSLParser.T__1);
	                this.state = 89;
	                this.condition();
	                this.state = 94;
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            }
	            this.state = 95;
	            this.match(CanopusDSLParser.T__9);
	            break;
	        case 15:
	            localctx = new IdContext(this, localctx);
	            this.enterOuterAlt(localctx, 3);
	            this.state = 97;
	            this.match(CanopusDSLParser.ID);
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	multipOperator() {
	    let localctx = new MultipOperatorContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 14, CanopusDSLParser.RULE_multipOperator);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 100;
	        _la = this._input.LA(1);
	        if(!(_la===11 || _la===19)) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	expr() {
	    let localctx = new ExprContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 16, CanopusDSLParser.RULE_expr);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 102;
	        this.multipExpr();
	        this.state = 107;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===5) {
	            this.state = 103;
	            this.match(CanopusDSLParser.T__4);
	            this.state = 104;
	            this.multipExpr();
	            this.state = 109;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	condition() {
	    let localctx = new ConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 18, CanopusDSLParser.RULE_condition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 110;
	        this.match(CanopusDSLParser.LABEL);
	        this.state = 111;
	        this.comparator();
	        this.state = 112;
	        this.match(CanopusDSLParser.STRING);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	comparator() {
	    let localctx = new ComparatorContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 20, CanopusDSLParser.RULE_comparator);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 114;
	        _la = this._input.LA(1);
	        if(!(_la===4 || _la===12)) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


}

CanopusDSLParser.EOF = antlr4.Token.EOF;
CanopusDSLParser.T__0 = 1;
CanopusDSLParser.T__1 = 2;
CanopusDSLParser.T__2 = 3;
CanopusDSLParser.T__3 = 4;
CanopusDSLParser.T__4 = 5;
CanopusDSLParser.T__5 = 6;
CanopusDSLParser.T__6 = 7;
CanopusDSLParser.T__7 = 8;
CanopusDSLParser.T__8 = 9;
CanopusDSLParser.T__9 = 10;
CanopusDSLParser.T__10 = 11;
CanopusDSLParser.T__11 = 12;
CanopusDSLParser.START_OP = 13;
CanopusDSLParser.END_OP = 14;
CanopusDSLParser.ID = 15;
CanopusDSLParser.LABEL = 16;
CanopusDSLParser.STRING = 17;
CanopusDSLParser.WS = 18;
CanopusDSLParser.WILDCARD = 19;
CanopusDSLParser.COMMENT = 20;

CanopusDSLParser.RULE_program = 0;
CanopusDSLParser.RULE_importPatterns = 1;
CanopusDSLParser.RULE_patternDef = 2;
CanopusDSLParser.RULE_patternExpr = 3;
CanopusDSLParser.RULE_middleExpr = 4;
CanopusDSLParser.RULE_multipExpr = 5;
CanopusDSLParser.RULE_primary = 6;
CanopusDSLParser.RULE_multipOperator = 7;
CanopusDSLParser.RULE_expr = 8;
CanopusDSLParser.RULE_condition = 9;
CanopusDSLParser.RULE_comparator = 10;

class ProgramContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CanopusDSLParser.RULE_program;
    }

	EOF() {
	    return this.getToken(CanopusDSLParser.EOF, 0);
	};

	importPatterns = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ImportPatternsContext);
	    } else {
	        return this.getTypedRuleContext(ImportPatternsContext,i);
	    }
	};

	patternDef = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(PatternDefContext);
	    } else {
	        return this.getTypedRuleContext(PatternDefContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterProgram(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitProgram(this);
		}
	}


}



class ImportPatternsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CanopusDSLParser.RULE_importPatterns;
    }

	ID = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CanopusDSLParser.ID);
	    } else {
	        return this.getToken(CanopusDSLParser.ID, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterImportPatterns(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitImportPatterns(this);
		}
	}


}



class PatternDefContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CanopusDSLParser.RULE_patternDef;
    }

	ID() {
	    return this.getToken(CanopusDSLParser.ID, 0);
	};

	patternExpr() {
	    return this.getTypedRuleContext(PatternExprContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterPatternDef(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitPatternDef(this);
		}
	}


}



class PatternExprContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CanopusDSLParser.RULE_patternExpr;
    }

	START_OP() {
	    return this.getToken(CanopusDSLParser.START_OP, 0);
	};

	middleExpr() {
	    return this.getTypedRuleContext(MiddleExprContext,0);
	};

	END_OP() {
	    return this.getToken(CanopusDSLParser.END_OP, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterPatternExpr(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitPatternExpr(this);
		}
	}


}



class MiddleExprContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CanopusDSLParser.RULE_middleExpr;
    }

	multipExpr = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(MultipExprContext);
	    } else {
	        return this.getTypedRuleContext(MultipExprContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterMiddleExpr(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitMiddleExpr(this);
		}
	}


}



class MultipExprContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CanopusDSLParser.RULE_multipExpr;
    }



		copyFrom(ctx) {
			super.copyFrom(ctx);
		}

}


class QuantifiedContext extends MultipExprContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	primary() {
	    return this.getTypedRuleContext(PrimaryContext,0);
	};

	multipOperator() {
	    return this.getTypedRuleContext(MultipOperatorContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterQuantified(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitQuantified(this);
		}
	}


}

CanopusDSLParser.QuantifiedContext = QuantifiedContext;

class WildcardAtomContext extends MultipExprContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	WILDCARD() {
	    return this.getToken(CanopusDSLParser.WILDCARD, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterWildcardAtom(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitWildcardAtom(this);
		}
	}


}

CanopusDSLParser.WildcardAtomContext = WildcardAtomContext;

class PrimaryContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CanopusDSLParser.RULE_primary;
    }



		copyFrom(ctx) {
			super.copyFrom(ctx);
		}

}


class AlternativeExprContext extends PrimaryContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	expr = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ExprContext);
	    } else {
	        return this.getTypedRuleContext(ExprContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterAlternativeExpr(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitAlternativeExpr(this);
		}
	}


}

CanopusDSLParser.AlternativeExprContext = AlternativeExprContext;

class ElementExprContext extends PrimaryContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	condition = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ConditionContext);
	    } else {
	        return this.getTypedRuleContext(ConditionContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterElementExpr(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitElementExpr(this);
		}
	}


}

CanopusDSLParser.ElementExprContext = ElementExprContext;

class IdContext extends PrimaryContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	ID() {
	    return this.getToken(CanopusDSLParser.ID, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterId(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitId(this);
		}
	}


}

CanopusDSLParser.IdContext = IdContext;

class MultipOperatorContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CanopusDSLParser.RULE_multipOperator;
    }

	WILDCARD() {
	    return this.getToken(CanopusDSLParser.WILDCARD, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterMultipOperator(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitMultipOperator(this);
		}
	}


}



class ExprContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CanopusDSLParser.RULE_expr;
    }

	multipExpr = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(MultipExprContext);
	    } else {
	        return this.getTypedRuleContext(MultipExprContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterExpr(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitExpr(this);
		}
	}


}



class ConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CanopusDSLParser.RULE_condition;
    }

	LABEL() {
	    return this.getToken(CanopusDSLParser.LABEL, 0);
	};

	comparator() {
	    return this.getTypedRuleContext(ComparatorContext,0);
	};

	STRING() {
	    return this.getToken(CanopusDSLParser.STRING, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitCondition(this);
		}
	}


}



class ComparatorContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CanopusDSLParser.RULE_comparator;
    }


	enterRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.enterComparator(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CanopusDSLListener ) {
	        listener.exitComparator(this);
		}
	}


}




CanopusDSLParser.ProgramContext = ProgramContext;
CanopusDSLParser.ImportPatternsContext = ImportPatternsContext;
CanopusDSLParser.PatternDefContext = PatternDefContext;
CanopusDSLParser.PatternExprContext = PatternExprContext;
CanopusDSLParser.MiddleExprContext = MiddleExprContext;
CanopusDSLParser.MultipExprContext = MultipExprContext;
CanopusDSLParser.PrimaryContext = PrimaryContext;
CanopusDSLParser.MultipOperatorContext = MultipOperatorContext;
CanopusDSLParser.ExprContext = ExprContext;
CanopusDSLParser.ConditionContext = ConditionContext;
CanopusDSLParser.ComparatorContext = ComparatorContext;
