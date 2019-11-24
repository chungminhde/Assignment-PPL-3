#1711020
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

def testRedeclared(decls, decl, kind):
        if kind == "variable":
            if any((decl.variable == x.name) for x in decls):
                raise Redeclared(Variable(), decl.variable)
            else:
                return Symbol(decl.variable, decl.varType)
        if kind == "function":
            if any((decl.name.name == x.name) for x in decls):
                raise Redeclared(Function(), decl.name.name)
            else:
                return Symbol(decl.name.name, MType([x.varType for x in decl.param], decl.returnType))
        else:
            if any((decl.variable == x.name) for x in decls):
                raise Redeclared(Parameter(), decl.variable)
            else:
                return Symbol(decl.variable, decl.varType)

def getEnvironment(environment, local):
        for i in range(len(environment)):
            if environment[i].name == local.name:
                environment.pop(i)
                environment.append(local)
                return environment
        environment.append(local)
        return environment   

def testTrue(x):
        if type(x) is bool:
            return x
        else:
            return False

def checkPass(left, right):
    if type(left) is ArrayPointerType:
        return True if (type(right) in [ArrayPointerType, ArrayType]) and (type(left.eleType) == type(right.eleType)) else False
    else:
        return True if type(left) == type(right) else True if (type(left), type(right)) == (FloatType, IntType) else False
            
class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType())),
    Symbol("putInt",MType([IntType()],VoidType())),
    Symbol("getFloat",MType([], FloatType())),
    Symbol("putFloat",MType([FloatType()], VoidType())),
    Symbol("putFloatLn",MType([FloatType()], VoidType())),
    Symbol("putBool",MType([BoolType()],VoidType())),
    Symbol("putBoolLn",MType([BoolType()],VoidType())),
    Symbol("putString",MType([StringType()],VoidType())),
    Symbol("putStringLn",MType([StringType()],VoidType())),
    Symbol("putLn",MType([],VoidType()))
    ]
    
    def __init__(self,ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast
        self.funcDecls = []
        self.funcCall = []
 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)
    
    
    def visitProgram(self,ast, c): 
        c = c.copy()
        for decl in ast.decl:
            resulttest = testRedeclared(c, decl, "variable" if type(decl) is VarDecl else "function")
            c.append(resulttest)
            if type(decl) is FuncDecl:
                self.funcDecls.append(resulttest)
        find = self.lookup("main", self.funcDecls, lambda x: x.name)
        
        if find is None:
            raise NoEntryPoint()
        else:
            self.funcCall.append(find)

        resultUnreachable = [self.visit(x, c) for x in filter(lambda x: type(x) is FuncDecl, ast.decl)]
        
        for x in self.funcDecls:
            if not x in self.funcCall:
                raise UnreachableFunction(x.name)
        return ''

    def visitFuncDecl(self,ast,c):
        environment = c.copy()
        parameter = []
        listStament = []
        for x in ast.param:
            result = testRedeclared(parameter, x, "param")
            parameter.append(result)
            environment = getEnvironment(environment,result)
        returnFunc = self.visit(ast.body, (environment, parameter, False, (ast.name.name,ast.returnType)))
        if (not returnFunc) and not (type(ast.returnType) is VoidType):
            raise FunctionNotReturn(ast.name.name)
        return returnFunc

#--------------Stament: If, For, Dowhile, Return, Break, Continue, Block--------------

    def visitIf(self, ast, c):
        if not type(self.visit(ast.expr, c)) is BoolType:
            raise TypeMismatchInStatement(ast)
        isReturn1 = self.visit(ast.thenStmt, c)
        if ast.elseStmt is None:
            return False
        else:
            isReturn2 = self.visit(ast.elseStmt, c)
            return testTrue(isReturn1) and testTrue(isReturn2)

    def visitFor(self, ast, c):
        expr1 = self.visit(ast.expr1, c)
        expr2 = self.visit(ast.expr2, c)
        expr3 = self.visit(ast.expr3, c)
        if type(expr1) != IntType or type(expr2) != BoolType or type(expr3) != IntType:
            raise TypeMismatchInStatement(ast)
        testTrue(self.visit(ast.loop, (c[0], c[1], True, c[3])))
        return False

    def visitDowhile(self, ast, c):
        returnDowhile = False
        expr = self.visit(ast.exp, c)
        if type(expr) is BoolType:
            pass
        else:
            raise TypeMismatchInStatement(ast)
        for x in ast.sl:
            returnDowhile = self.visit(x, (c[0], c[1], True, c[3]))
            if testTrue(returnDowhile):
                returnDowhile = true
        return returnDowhile

    def visitContinue(self, ast, c):
        if c[2] == False:
            raise ContinueNotInLoop()
        else:
            return False

    def visitReturn(self, ast, c):
        if type(c[3][1]) is VoidType:
            if ast.expr is None:
                return True
            else:
                raise TypeMismatchInStatement(ast)
        else:
            if ast.expr is None:
                raise TypeMismatchInStatement(ast)
            elif checkPass(c[3][1], self.visit(ast.expr, c)):
                return True
            else:
                raise TypeMismatchInStatement(ast)


    def visitBreak(self, ast, c):
        if c[2] == False:
            raise BreakNotInLoop()
        else:
            return False

    def visitBlock(self, ast, c):
        localScope = c[1].copy()
        environment = c[0].copy()
        returnBlock = False
        for x in ast.member:
            if type(x) is VarDecl:
                result = testRedeclared(localScope, x, "variable")
                localScope.append(result)
                environment = getEnvironment(environment, result)
            else:
                returnBlock = self.visit(x, (environment, [], c[2], c[3]))
                if (testTrue(returnBlock)):
                    returnBlock = True
        return returnBlock

#----------------Expr---------------------
    def visitUnaryOp(self, ast, c):
        expr = self.visit(ast.body, c)
        op = ast.op
        if op == '-':
            if type(expr) in [FloatType,IntType]:
                return expr
            else:
                raise TypeMismatchInExpression(ast)
        else:
            if type(expr) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

    def visitArrayCell(self, ast, c):
        arr = self.visit(ast.arr, c)
        idx = self.visit(ast.idx, c)
        if type(arr) in [ArrayType, ArrayPointerType] and type(idx) is IntType:
            return arr.eleType
        else:
            raise TypeMismatchInExpression(ast)

    def visitBinaryOp(self, ast, c):
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        op = ast.op
        typeBinary = None
        if op == '=':
            if (not type(ast.left) in [Id, ArrayCell]):
                raise NotLeftValue(ast.left)
            elif type(left) in [MType, VoidType, ArrayType, ArrayPointerType] or not checkPass(left, right):
                raise TypeMismatchInExpression(ast)            
            else:
                return left
        if type(left) is IntType and type(right) is IntType:
            typeBinary = IntType()
        elif (type(left), type(right)) in [(IntType, FloatType), (FloatType, IntType), (FloatType, FloatType)]:
            typeBinary = FloatType()
        elif (type(left), type(right)) == (BoolType, BoolType):
            typeBinary = BoolType()
        else:
            typeBinary = None
        if typeBinary is None:
            raise TypeMismatchInExpression(ast)
        if op in ['>', '>=', '<', '<=']:
            if type(typeBinary) is IntType or type(typeBinary) is FloatType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['+', '-', '*', '/']:
            if type(typeBinary) is IntType or type(typeBinary) is FloatType:
                return typeBinary
            else:
                raise TypeMismatchInExpression(ast)
        elif op in ['%']:
            if type(typeBinary) is IntType:
                return IntType()
            else:
                TypeMismatchInExpression(ast)
        elif op in ['||', '&&']:
            if type(typeBinary) is BoolType:
                return BoolType()
            else:
                TypeMismatchInExpression(ast)
        elif op in ["!=", "=="]:
            if type(typeBinary) in [IntType, BoolType]:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
                
    def visitCallExpr(self, ast, c):
        at = [self.visit(x, c) for x in ast.param]
        res = self.lookup(ast.method.name, c[0], lambda x: x.name)
        if res is None:
            raise Undeclared(Function(), ast.method.name)
        elif (not type(res.mtype) is MType) or (len(res.mtype.partype) != len(at)):
            raise TypeMismatchInExpression(ast)
        else:
            if c[3][0] != res.name: 
                self.funcCall.append(res)
            typePara = zip(res.mtype.partype, at)
            for left, right in typePara:
                if not checkPass(left, right):
                    raise TypeMismatchInExpression(ast)
            return res.mtype.rettype

    def visitId(self, ast, c):
        checkDeclared = self.lookup(ast.name, c[0], lambda x: x.name)
        if checkDeclared is None:
            raise Undeclared(Identifier(), ast.name)
        else:
            return checkDeclared.mtype

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()