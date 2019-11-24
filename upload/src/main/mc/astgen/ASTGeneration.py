# 1711020
from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import reduce
class ASTGeneration(MCVisitor):
    def visitProgram(self,ctx:MCParser.ProgramContext):
       return Program(self.visit(ctx.manydecls()))
    def visitManydecls(self,ctx:MCParser.ManydeclsContext):
        if ctx.manydecls():
            return list(y for x in [self.visit(ctx.decl())] for y in x)  + self.visit(ctx.manydecls())
            # return [y for x in lst for y in x]
            # return reduce(lambda x,y: x+y,lst)
        else:
            return list(y for x in [self.visit(ctx.decl())] for y in x) 
            # reduce(lambda x,y: x+y, [self.visit(ctx.decl())] ) 
    def visitDecl(self,ctx:MCParser.DeclContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        else:
            return [self.visit(ctx.func_decl())]
    def visitFunc_decl(self,ctx:MCParser.Func_declContext):
        if ctx.paradecl():
            return FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.paradecl()),self.visit(ctx.func_type()),self.visit(ctx.block_statement()))
        else:
            return FuncDecl(Id(ctx.ID().getText()),[],self.visit(ctx.func_type()),self.visit(ctx.block_statement()))
    def visitVar_decl(self,ctx:MCParser.Var_declContext):
        type_ = ctx.primitivetype()
        return [(VarDecl(self.visitVar(_v)[0],self.visit(type_)) if len(self.visit(_v))==1 else VarDecl(self.visitVar(_v)[0],ArrayType(self.visitVar(_v)[1],self.visit(type_)))) for _v in ctx.var() ]
    def visitVar(self,ctx:MCParser.VarContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        else:
            return [ctx.ID().getText(),ctx.INTLIT().getText()]
    def visitPrimitivetype(self,ctx:MCParser.PrimitivetypeContext):
        if ctx.INT()is not None:
            return IntType()
        elif ctx.BOOLEAN() is not None:
            return BoolType()
        elif ctx.FLOAT() is not None:
            return FloatType()
        elif ctx.STRING() is not None:
            return StringType()
    def visitFunc_type(self,ctx:MCParser.Func_typeContext):
        if ctx.primitivetype():
            return self.visit(ctx.primitivetype())
        else:
            if ctx.outparameter():
                return self.visit(ctx.outparameter())
            else:
                return VoidType()
    def visitOutparameter(self,ctx:MCParser.OutparameterContext):
        return ArrayPointerType(self.visit(ctx.primitivetype()))
    def visitParadecl(self,ctx:MCParser.ParadeclContext):
        return list(reduce(lambda x,y: x+self.visit(y),ctx.para()[1:],self.visit(ctx.para()[0])) if ctx.getChildCount()!=0 else [])
    def visitPara(self,ctx:MCParser.ParaContext):
        if ctx.getChildCount() == 2: 
            return [VarDecl(ctx.ID().getText(),self.visit(ctx.primitivetype()))]
        else: 
            return [VarDecl(ctx.ID().getText(),ArrayPointerType(self.visit(ctx.primitivetype())))]
        
    
#---------------statement--------------------
    def visitBlock_statement(self,ctx:MCParser.Block_statementContext):
        return Block([i for x in ctx.block() for i in self.visit(x)])
        
    def visitBlock(self,ctx:MCParser.BlockContext):
        if ctx.statement():
            return [self.visit(ctx.statement())]
        else:
            return self.visit(ctx.var_decl())
    def visitStatement(self,ctx:MCParser.StatementContext):
        return self.visit(ctx.getChild(0))
    def visitIf_statement(self,ctx:MCParser.If_statementContext):
        if ctx.ELSE():
            return If(self.visit(ctx.exp()),self.visit(ctx.statement(0)),self.visit(ctx.statement(1)))
        else:
            return If(self.visit(ctx.exp()),self.visit(ctx.statement(0)))
    def visitDowhile_statement(self,ctx:MCParser.Dowhile_statementContext):
        return Dowhile([self.visit(x) for x in ctx.statement()],self.visit(ctx.exp()))
    def visitFor_statement(self,ctx:MCParser.For_statementContext):
        return For(self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),self.visit(ctx.exp(2)),self.visit(ctx.statement()))
    def visitBreak_statement(self,ctx:MCParser.Break_statementContext):
        return Break()
    def visitContinue_statement(self,ctx:MCParser.Continue_statementContext):
        return Continue()
    def visitReturn_statement(self,ctx:MCParser.Return_statementContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        else:
            return Return()
    def visitExp_statement(self,ctx:MCParser.Exp_statementContext):
        return self.visit(ctx.exp())
    def visitExp(self,ctx:MCParser.ExpContext):
        #exp: exp1 ASSIGN exp | exp1;
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.ASSIGN().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp()))
        else:
            return self.visit(ctx.exp1())
    def visitExp1(self,ctx:MCParser.Exp1Context):
        #exp1: exp1 OR exp2 | exp2;
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.OR().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp2()))
        else:
            return self.visit(ctx.exp2())
    def visitExp2(self,ctx:MCParser.Exp2Context):
        #exp2: exp2 AND exp3 | exp3;
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.AND().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
        else:
            return self.visit(ctx.exp3())
    def visitExp3(self,ctx:MCParser.Exp3Context):
        #exp3: exp4 (EQUAL | NOTEQUAL) exp4 | exp4;
        if ctx.getChildCount() ==3:
            if ctx.EQUAL():
                return BinaryOp(ctx.EQUAL().getText(),self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1)))
            else:
                return BinaryOp(ctx.NOTEQUAL().getText(),self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1)))
        else:
            return self.visit(ctx.exp4(0))
    def visitExp4(self,ctx:MCParser.Exp4Context):
        #exp4: exp5 (LESS|LESSEQUAL|GREATER|GREATEREQUAL) exp5 | exp5;
        if ctx.getChildCount() ==3:
            if ctx.LESS():
                return BinaryOp(ctx.LESS().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
            if ctx.LESSEQUAL():
                return BinaryOp(ctx.LESSEQUAL().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
            if ctx.GREATER():
                return BinaryOp(ctx.GREATER().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
            if ctx.GREATEREQUAL():
                return BinaryOp(ctx.GREATEREQUAL().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        else:
            return self.visit(ctx.exp5(0))
    def visitExp5(self,ctx:MCParser.Exp5Context):
        #exp5: exp5 (ADD|SUB) exp6 | exp6;
        if ctx.getChildCount() == 3:
            if ctx.ADD():
                return BinaryOp(ctx.ADD().getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6()))
            else:
                return BinaryOp(ctx.SUB().getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp6())
    def visitExp6(self,ctx:MCParser.Exp6Context):
        #exp6: exp6 (DIV|MUL|MOD) exp7 | exp7;
        if ctx.getChildCount() ==3:
            if ctx.DIV():
                return BinaryOp(ctx.DIV().getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))
            if ctx.MUL():
                return BinaryOp(ctx.MUL().getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))
            if ctx.MOD():
                return BinaryOp(ctx.MOD().getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp7())
    def visitExp7(self,ctx:MCParser.Exp7Context):
        #exp7: (SUB|NOT) exp7 | exp8;
        if ctx.getChildCount() == 2: 
            if ctx.SUB():
                return UnaryOp(ctx.SUB().getText(),self.visit(ctx.exp7()))
            else:
                return UnaryOp(ctx.NOT().getText(),self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp8())
    def visitExp8(self,ctx:MCParser.Exp8Context):
        #exp8: exp9 '[' exp ']' | exp9;
        if ctx.exp():
            return ArrayCell(self.visit(ctx.exp9()),self.visit(ctx.exp()))
        else:
            return self.visit(ctx.exp9())
    def visitExp9(self,ctx:MCParser.Exp9Context):
        #exp9: '(' exp')' | operand;
        if ctx.operand():
            return self.visit(ctx.operand())
        else:
            return self.visit(ctx.exp())
    def visitOperand(self,ctx:MCParser.OperandContext):
        #operand: INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | funcall | ID ;
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        if ctx.BOOLEANLIT():
            return BooleanLiteral(ctx.BOOLEANLIT().getText())
        if ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        if ctx.funcall():
            return self.visit(ctx.funcall())
        if ctx.ID():
            return Id(ctx.ID().getText())
    def visitFuncall(self,ctx:MCParser.FuncallContext):
        #funcall: ID LB (exp (CM exp)*)?  RB;
        if ctx.getChildCount() == 3:
            return CallExpr(Id(ctx.ID().getText()),[])
        else:
            return CallExpr(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.exp()])
