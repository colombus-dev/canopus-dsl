grammar CanopusDSL;

// ---------------------- Parser rules ----------------------

program: (importPatterns | patternDef)+ EOF;

importPatterns: 'import' ID (',' ID)*;

patternDef: 'pattern' ID '=' patternExpr;

// A pattern can contain multiple middleExpr and start with 'start' or end with 'end'
// (a pipeline needs at least one middleExpr between 'start' and 'end')
patternExpr:
	START_OP '->' middleExpr '->' END_OP
	| START_OP '->' middleExpr
	| middleExpr '->' END_OP
	| middleExpr;

// A middle expressions is a sequence of multipExpr separated by ->
middleExpr: multipExpr ('->' multipExpr)*;

// A multiple expression is a wildcard atom or a primary expression with an
// optional multiplicity operator; a wildcard never takes a quantifier.
multipExpr: WILDCARD # wildcardAtom | primary multipOperator? # quantified;

// Primary (atomic) units of an expression
primary:
	'(' expr ('|' expr)* ')'				# alternativeExpr
	| '[' condition (',' condition)* ']'	# elementExpr
	| ID									# id;

// Multiplicity operator (like in regular expressions)
multipOperator: '*' | '+';

expr: multipExpr ('->' multipExpr)*;

// Conditions inside [...]
condition: LABEL comparator STRING;

comparator: '=' | '!=';

// ---------------------- Lexer rules ----------------------

START_OP: 'start';
END_OP: 'end';

ID: [A-Z][a-zA-Z0-9_]*;
LABEL: [a-z][a-zA-Z0-9_]*;
STRING: '"' (~["\r\n])* '"';
WS: [ \t\r\n]+ -> skip;
WILDCARD: '*';
COMMENT: '#' ~[\r\n]* -> skip;
