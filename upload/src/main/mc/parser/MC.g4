//1711020
grammar MC;

@lexer::header {
from lexererr import *
import sys,os
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    else:
        return super().emit();
}

options{
	language=Python3;
}




//3.1
COMMENT: '/*' .*? '*/' ->skip;
LINECOMMENT: '//'  (~[\n])* ->skip ;

//3.2
INT: 'int' ;
IF: 'if' ;
ELSE: 'else' ;
VOID: 'void' ;
BOOLEAN: 'boolean' ;
FLOAT: 'float' ;
STRING: 'string' ;
BREAK: 'break' ;
CONTINUE: 'continue' ;
FOR: 'for' ;
RETURN: 'return' ;
DO: 'do' ;
WHILE: 'while' ;
fragment TRUE: 'true' ;
fragment FALSE: 'false' ;
primitivetype:  INT | BOOLEAN |  FLOAT | STRING ;
// 3.3 Operators

ASSIGN: '=';
OR: '||';
AND: '&&';
EQUAL: '==';
NOTEQUAL: '!=';
LESS: '<';
LESSEQUAL: '<=';
GREATER: '>';
GREATEREQUAL: '>=';
ADD: '+';
SUB: '-';
DIV: '/';
MUL: '*';
MOD: '%';
NOT: '!';

//Separator
LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
SM: ';' ;
CM: ',' ;
LS: '[' ;
RS: ']' ;
//literal TOKEN
INTLIT: [0-9]+;
// [0-9]+ (('e'| 'E')? ('-')? [0-9]+)?
FLOATLIT: NUM ('.')? | NUM* ('.') NUM | NUM ('.')(('e'| 'E')? ('-')? [0-9]+)?;
STRINGLIT: '"' ('\\' [bfrnt\\"] | ~[\b\f\r\n\t\\"])* '"' {self.text =self.text[1:-1] } ;
BOOLEANLIT: TRUE|FALSE;
ID: [a-zA-Z_][0-9a-zA-Z_]*;

arraypointertype: inparameter  | outparameter;
inparameter: primitivetype ID LS RS ;
outparameter: primitivetype LS RS ;

program  : manydecls EOF;
manydecls: decl manydecls|decl;
decl: var_decl | func_decl;
//LITERAL
LITERAL: INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT ;
//VARIABLE DECLARATION
var_decl: primitivetype var (CM var)*  SM;
var: ID | ID '[' INTLIT ']' ;

// FUNCTION DECLARATION
func_decl: func_type ID LB paradecl? RB block_statement ;
func_type: primitivetype | VOID | outparameter ;
paradecl: para (CM para)* ;
para: primitivetype ID | primitivetype ID LS RS ;

block_statement: LP block* RP   ;
block: statement | var_decl;
statement: if_statement | dowhile_statement | for_statement | break_statement | continue_statement | return_statement | exp_statement | block_statement  ;
//7.1 THE IF STATEMENT
if_statement: IF LB exp RB statement
                | IF LB exp RB statement ELSE statement ;
dowhile_statement: DO statement+ WHILE exp  SM;
for_statement: FOR LB exp SM exp SM exp RB statement;
break_statement:  BREAK SM;
continue_statement: CONTINUE SM;
return_statement: 'return' SM | 'return' exp SM;
exp_statement: exp SM;
invocation: ID LB (exp? | exp (CM exp)+) RB ;
// expression decl;
exp: exp1 ASSIGN exp | exp1;
exp1: exp1 OR exp2 | exp2;
exp2: exp2 AND exp3 | exp3;
exp3: exp4 (EQUAL | NOTEQUAL) exp4 | exp4;
exp4: exp5 (LESS|LESSEQUAL|GREATER|GREATEREQUAL) exp5 | exp5;
exp5: exp5 (ADD|SUB) exp6 | exp6;
exp6: exp6 (DIV|MUL|MOD) exp7 | exp7;
exp7: (SUB|NOT) exp7 | exp8;
exp8: exp9 '[' exp ']' | exp9;
exp9: '(' exp')' | operand;
operand: INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | funcall | ID ;
funcall: ID LB (exp (CM exp)*)?  RB;

fragment NUM: [0-9]+ (('e'| 'E')? ('-')? [0-9]+)?;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
UNCLOSE_STRING: '"'('\\' [bfrnt\\"] | ~[\b\f\r\n\t\\"])* {self.text =self.text.lstrip('"') } ;
ILLEGAL_ESCAPE: '"'('\\' [bfrnt\\"] | ~[\b\f\r\n\t\\"])* '\\' ~[bfrnt] {self.text =self.text.lstrip('"') } ;
ERROR_CHAR: .;