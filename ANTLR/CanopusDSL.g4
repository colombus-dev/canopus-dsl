grammar CanopusDSL;

// ---------------------- Parser rules ----------------------

program: patternDef+ EOF;

patternDef: 'pattern' ID '=' patternExpr;

// A pattern can contain multiple middleExpr and start with 'start' or end with 'end'
patternExpr:
	START_OP '->' middleExpr '->' END_OP
	| START_OP '->' middleExpr
	| middleExpr '->' END_OP
	| middleExpr;

// A middle expressions is a sequence of multipExpr separated by ->
middleExpr: multipExpr ('->' multipExpr)*;

// A multiple expression is a primary expression with an optional multiplicity operator
multipExpr: primary multipOperator?;

// Primary (atomic) units of an expression
primary:
	'(' expr ('|' expr)+ ')'				# alternativeExpr
	| '[' condition (',' condition)* ']'	# elementExpr
	| ID									# id
	| WILDCARD								# wildcard; // TODO: remove wildcard from primary to avoid *+

// Multiplicity operator (like in regular expressions)
multipOperator: '*' | '+';

expr: primary ('->' primary)*;

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