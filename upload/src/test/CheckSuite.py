import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
#----------------TEST REDECLARED#----------------
    def test_Redeclared_variable_1(self):
        """Redeclared variable a"""
        input = """
            int a;
            float a;
            void main(){
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_Redeclared_variable_2(self):
        """Redeclared a in main"""
        input = """
           void main()
        {
            int a;
            int a;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_Redeclared_function_3(self):
        """Redeclared a in function"""
        input = """
           void main(int a)
        {
            int a;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_Redeclared_variable_4(self):
        """Redeclared a in main"""
        input = """
           void main()
        {
            int a;
            float a;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_Redeclared_variable_5(self):
        """Redeclared a in main"""
        input = """
           void main()
        {
            boolean a;
            float a;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_Redeclared_function_6(self):
        """Redeclared a in function"""
        input = """
        int a;
        int foo(int b,float c)
        {
            string c;
        }
        void main()
        {
            return 1;
        }
        
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_Redeclared_parameter_7(self):
        """Redeclared parameter"""
        input = """
           void main(int a,int a)
        {
            return;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_Redeclared_function_8(self):
        """Redeclared Function"""
        input = """
           int foo()
           {
               return;
           }
           float foo()
           {

           }
           int main()
           {
               foo(5);
           }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_Redeclared_parameter_9(self):
        """Redeclared Parameter"""
        input = """
           void main(int a,float b, boolean c, string b)
        {
            return 0;
        }
        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_Redeclared_function_10(self):
        """Redeclared Function"""
        input = """
        int foo()
           {
               return;
           }

        boolean foo()
           {

           }
           int main()
           {
               foo(5);
           }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,409))

#----------------TEST UNDECLARED----------------
    def test_Undeclared_Identifier_1(self):
        """Undeclared Identifier"""
        input = """
        int a;
        int b;
            void main(){
                        a=b+c;
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,410))
    def test_Undeclared_Identifier_2(self):
        """Undeclared Identifier"""
        input = """
        int a;
        int main()
        {
             b=5;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,411))
    def test_Undeclared_Identifier_3(self):
        """Undeclared Identifier"""
        input = """
        int a;
        int b;
        void main(){
            a=b;
        }
        int foo(float n)
        {
            n= a+b/c;
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_Undeclared_function_4(self):
        """Undeclared Function"""
        input = """
        
            void main(){
                        foo(5);
                        return;
            }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,413))
    def test_Undeclared_function_5(self):
        """Undeclared Function"""
        input = """
        
            void main(){
                        foo();
                        return;
            }
            int foo_5()
            {
                return 0;
            }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_Undeclared_Identifier_6(self):
        """Undeclared Identifier"""
        input = """
        int a;
        int b;
        void main(){
            a = b + 5;
            c = 5;
            string f;
            f = a/b;
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,415))
    def test_Undeclared_function_7(self):
        """Undeclared Function"""
        input = """
            void main(){
                        foo_5(10);
                        return;
            }
            int foo_5(int n)
            {
                n = m +1;
                return 0;
            }
        """
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input,expect,416))
    def test_Undeclared_function_8(self):
        """Undeclared Function"""
        input = """
            int a;
            float b;
            boolean check()
            {
                c = a+ b;
                return True;
                
            }
            int main()
            {
                a= a+ b;
                int c;
                c = a/b;
                return 0;
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,417))
    def test_Undeclared_function_9(self):
        """Undeclared Function"""
        input = """
            int a;
            boolean check;
            void main(){
                b = check;
                return 0;
            }
            int foo_5()
            {
                return 0;
            }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,418))
    def test_Undeclared_function_10(self):
        """Undeclared Function"""
        input = """
        
        boolean foo(int n)
        {
            return true;
        }
        int main()
        {
            foo(10);
            foo_1(10);
            return 0;
        }
        """
        expect = "Undeclared Function: foo_1"
        self.assertTrue(TestChecker.test(input,expect,419))
#----------------FUNCTION NOT RETURN----------------
    def test_function_not_return_1(self):
        """Function Main Not Return"""
        input = """
            int main(){
            }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,420))
    def test_function_not_return_2(self):
        """Function Not Return"""
        input = """
            int foo()
            {

            }
            void main(){
            }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,421))
    def test_function_not_return_3(self):
        """Function Not Return"""
        input = """
            int n;
            int k;
            int foo()
            {
                
            }
            void main(){
                foo();
                return;
            }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_function_not_return_4(self):
        """Function Not Return"""
        input = """
            int check()
            {

            }
            int main()
            {
                return 1;
            }
        """
        expect = "Function check Not Return "
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_function_not_return_5(self):
        """Function Not Return"""
        input = """
            string check;
            int test(int n)
            {
                
            }
            void main(){
            }
        """
        expect = "Function test Not Return "
        self.assertTrue(TestChecker.test(input,expect,424))
#----------------NO ENTRY POINT----------------
    def test_no_entry_point(self):
        """No Entry Point"""
        input = """
            string check;
            int test(int n)
            {
                return 1;
            }
            
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,425))
#----------------UNREACHABLE FUNCTION----------------
    def test_unreachable_function_1(self):
        """Unreachable Function"""
        input = """
            
            int test(int n)
            {
                return 1;
            }
            void main()
            {
                return;
            }
            
        """
        expect = "Unreachable Function: test"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_unreachable_function_2(self):
        """Unreachable Function"""
        input = """
            float foo()
            {
                int k;
                k = k +1;
                return k;
            }
            void main()
            {
                return;
            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_unreachable_function_3(self):
        """Unreachable Function"""
        input = """
            
            int foo(int n)
            {
                return 1;
            }
            boolean foo_2()
            {
                return false;
            }
            void main()
            {
                foo(5);
                return;
            }
            
        """
        expect = "Unreachable Function: foo_2"
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_unreachable_function_4(self):
        """Unreachable Function"""
        input = """
            
            int test(int n)
            {
                return 1;
            }
            void foo(int k)
            {
                return;
            }
            void main()
            {
                test(10);
                return;
            }
            
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,429))
#-------------------Break Not In Loop-----------------
    def test_Break_not_in_loop_1(self):
        """ Break Not In Loop """
        input = """
        void main(){
            if(true)
            {
                break;
            }
        }
        """
        expect= "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 430))
    def test_Break_not_in_loop_2(self):
        """Break Not In Loop """
        input = """
        void main(){
            int a;
            break;
        }
        """
        expect= "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test_Break_not_in_loop_3(self):
        """Break Not In Loop """
        input = """
        int foo()
        {
            break;
        }
        void main(){
            return 0;
        }
        """
        expect= "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_Break_not_in_loop_4(self):
        """Break Not In Loop"""
        input = """
        void main(){
            {
                break;
            }
        }
        """
        expect= "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test_Break_not_in_loop_5(self):
        """Break Not In Loop"""
        input = """
        float Div(int n, int m)
        {
            break;
            return 0;
        }
        void main(){
            int a;
            return;
        }
        """
        expect= "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 434))
#------------------- TEST CONTINUE NOT IN LOOP-----------------
    def test_Continue_not_in_loop_1(self):
        """Continue Not In Loop"""
        input = """
        void main(){
            continue;
        }
        """
        expect= "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 435))
    def test_Continue_not_in_loop_2(self):
        """Continue Not In Loop"""
        input = """
        void main(){
           { 
               continue;
           }
        }
        """
        expect= "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 436))
    def test_Continue_not_in_loop_3(self):
        """Continue Not In Loop"""
        input = """
        void main(){
            if (true)
                {
                    continue;
                }

        }
        """
        expect= "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test_Continue_not_in_loop_4(self):
        """Continue Not In Loop"""
        input = """
        int foo()
        {
            continue;
        }
        void main(){
            return;
        }
        """
        expect= "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test_Continue_not_in_loop_5(self):
        """Continue Not In Loop"""
        input = """
        int checkPrime()
        {
            return 0;
        }
        float foo()
        {
            continue;
        }
        void main(){
            return 0;
        }
        """
        expect= "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 439))
#----------------- TEST NOT LEFT VALUE----------------
    def test_Not_left_value_1(self):
        """Not Left Value"""
        input = """
        void main(){
            1 + 2 = 3;
        }
        """
        expect= "Not Left Value: BinaryOp(+,IntLiteral(1),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input, expect, 440))
    def test_Not_left_value_2(self):
        """Not Left Value"""
        input = """
        void main(){
           int a;
           a * 5 = 10;
        }
        """
        expect= "Not Left Value: BinaryOp(*,Id(a),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input, expect, 441))
    def test_Not_left_value_3(self):
        """Not Left Value"""
        input = """
        void main(){
           int a;
           float b;
           a / 10 = b +2;
        }
        """
        expect= "Not Left Value: BinaryOp(/,Id(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input, expect, 442))
    def test_Not_left_value_4(self):
        """Not Left Value"""
        input = """
        void main(){
           int arr[100];
           arr[99] + arr[100] = 100;
        }
        """
        expect= "Not Left Value: BinaryOp(+,ArrayCell(Id(arr),IntLiteral(99)),ArrayCell(Id(arr),IntLiteral(100)))"
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test_Not_left_value_5(self):
        """Not Left Value"""
        input = """
        int foo(int n)
        {
            n = n +1 ;
            return n;
        }
        void main(){
           foo(10) + 5 = foo(5) + 10;
        }
        """
        expect= "Not Left Value: BinaryOp(+,CallExpr(Id(foo),[IntLiteral(10)]),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input, expect, 444))
    def test_Not_left_value_6(self):
        """Not Left Value"""
        input = """
        int k;
        float m;

        void main(){
           m % 10 = k;
           return 0;
        }
        """
        expect= "Not Left Value: BinaryOp(%,Id(m),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input, expect, 445))
    def test_Not_left_value_7(self):
        """Not Left Value"""
        input = """
        int foo(int n)
        {
            return n;
        }
        void main(){
           foo(100) = 100;
        }
        """
        expect= "Not Left Value: CallExpr(Id(foo),[IntLiteral(100)])"
        self.assertTrue(TestChecker.test(input, expect, 446))
    def test_Not_left_value_8(self):
        """Not Left Value"""
        input = """int foo(int n)
        {
            return n;
        }
        void main(){
           foo(10) + foo(20) = 30;
        }
        """
        expect= "Not Left Value: BinaryOp(+,CallExpr(Id(foo),[IntLiteral(10)]),CallExpr(Id(foo),[IntLiteral(20)]))"
        self.assertTrue(TestChecker.test(input, expect, 447))
    def test_Not_left_value_9(self):
        """Not Left Value"""
        input = """
        int foo()
        {
            return 100;
        }
        void main(){
           int arr[10];
           arr[0] + foo() - 5 = 10;
        }
        """
        expect= "Not Left Value: BinaryOp(-,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),CallExpr(Id(foo),[])),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test_Not_left_value_10(self):
        """Not Left Value"""
        input = """
        void main(){
           5 * 10 + 100/40 -20 = -16.25 ;
           return;
        }
        """
        expect= "Not Left Value: BinaryOp(-,BinaryOp(+,BinaryOp(*,IntLiteral(5),IntLiteral(10)),BinaryOp(/,IntLiteral(100),IntLiteral(40))),IntLiteral(20))"
        self.assertTrue(TestChecker.test(input, expect, 449))
#---------------TEST TYPE MISMATCH IN STATEMENT----------------
    def test_type_mismatch_in_statement_1(self):
        """Type Mismatch In Statement For If Statement"""
        input = """
        void main(){
           int a;
           if(a)
           {
               a = 10;
           }
        }
        """
        expect= "Type Mismatch In Statement: If(Id(a),Block([BinaryOp(=,Id(a),IntLiteral(10))]))"
        self.assertTrue(TestChecker.test(input, expect, 450))
    def test_type_mismatch_in_statement_2(self):
        """Type Mismatch In Statement For If Statement"""
        input = """
        void main(){
            float k;
            if (k)
            {
                k = 0.0;
            }
           
        }
        """
        expect= "Type Mismatch In Statement: If(Id(k),Block([BinaryOp(=,Id(k),FloatLiteral(0.0))]))"
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test_type_mismatch_in_statement_3(self):
        """Type Mismatch In Statement For If Statement"""
        input = """
        void main(){
           string str;
           if(str)
           {
               str = "ABCD";
           }
        }
        """
        expect= "Type Mismatch In Statement: If(Id(str),Block([BinaryOp(=,Id(str),StringLiteral(ABCD))]))"
        self.assertTrue(TestChecker.test(input, expect, 452))
    def test_type_mismatch_in_statement_4(self):
        """Type Mismatch In Statement For For Statement"""
        input = """
        void main(){
           for(1;2;3)
           {

           }
        }
        """
        expect= "Type Mismatch In Statement: For(IntLiteral(1);IntLiteral(2);IntLiteral(3);Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test_type_mismatch_in_statement_5(self):
        """Type Mismatch In Statement For For Statement"""
        input = """
        void main(){
           for(true;1<5;3)
           {

           }
        }
        """
        expect= "Type Mismatch In Statement: For(BooleanLiteral(true);BinaryOp(<,IntLiteral(1),IntLiteral(5));IntLiteral(3);Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 454))
    def test_type_mismatch_in_statement_6(self):
        """Type Mismatch In Statement For For Statement"""
        input = """
        void main(){
           for(1;2<3;false)
           {
               int a;
           }
        }
        """
        expect= "Type Mismatch In Statement: For(IntLiteral(1);BinaryOp(<,IntLiteral(2),IntLiteral(3));BooleanLiteral(false);Block([VarDecl(a,IntType)]))"
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test_type_mismatch_in_statement_7(self):
        """Type Mismatch In Statement For For Statment"""
        input = """
        void main(){
           string str;
           for(str;5<10;100)
           {
               return;
           }
        }
        """
        expect= "Type Mismatch In Statement: For(Id(str);BinaryOp(<,IntLiteral(5),IntLiteral(10));IntLiteral(100);Block([Return()]))"
        self.assertTrue(TestChecker.test(input, expect, 456))
    def test_type_mismatch_in_statement_8(self):
        """Type Mismatch In Statement For Dowhile Statement"""
        input = """
        void main(){
           do
           {
               int a;
               float b;
               a= 10;
               b = 5.0;
           }
           while(5);
        }
        """
        expect= "Type Mismatch In Statement: Dowhile([Block([VarDecl(a,IntType),VarDecl(b,FloatType),BinaryOp(=,Id(a),IntLiteral(10)),BinaryOp(=,Id(b),FloatLiteral(5.0))])],IntLiteral(5))"
        self.assertTrue(TestChecker.test(input, expect, 457))
    def test_type_mismatch_in_statement_9(self):
        """Type Mismatch In Statement For Dowhile Statement"""
        input = """
        void main(){
           do
           {
               int a;
               return 100;
           }
           while(5.5);
        }
        """
        expect= "Type Mismatch In Statement: Dowhile([Block([VarDecl(a,IntType),Return(IntLiteral(100))])],FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input, expect, 458))
    def test_type_mismatch_in_statement_10(self):
        """Type Mismatch In Statement For Dowhile Statement"""
        input = """
        void main(){
           do
           {
               float n;
               continue;
           }
           while("ABCD");
        }
        """
        expect= "Type Mismatch In Statement: Dowhile([Block([VarDecl(n,FloatType),Continue()])],StringLiteral(ABCD))"
        self.assertTrue(TestChecker.test(input, expect, 459))
    def test_type_mismatch_in_statement_11(self):
        """Type Mismatch In Statement For Dowhile Statement"""
        input = """
        void main(){
           
           do{
               if(true)
               {
                   break;
               }
           }
           while(1);
        }
        """
        expect= "Type Mismatch In Statement: Dowhile([Block([If(BooleanLiteral(true),Block([Break()]))])],IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 460))
    def test_type_mismatch_in_statement_12(self):
        """Type Mismatch In Statement Return Void"""
        input = """
        void main(){
           return a;
        }
        """
        expect= "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 461))
    def test_type_mismatch_in_statement_13(self):
        """Type Mismatch In Statement For Return Statement"""
        input = """
        void foo(){
            return 100;
        }
        void main(){
           return;
        }
        """
        expect= "Type Mismatch In Statement: Return(IntLiteral(100))"
        self.assertTrue(TestChecker.test(input, expect, 462))
    def test_type_mismatch_in_statement_14(self):
        """Type Mismatch In Statement For Return Statement"""
        input = """
        void foo()
        {
            return "ABCD";
        }
        void main(){
           foo();
        }
        """
        expect= "Type Mismatch In Statement: Return(StringLiteral(ABCD))"
        self.assertTrue(TestChecker.test(input, expect, 463))
    def test_type_mismatch_in_statement_15(self):
        """Type Mismatch In Statement For Return Statement"""
        input = """
        int foo()
        {
            return 5.5;
        }
        void main(){
           foo();
        }
        """
        expect= "Type Mismatch In Statement: Return(FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input, expect, 464))
    def test_type_mismatch_in_statement_16(self):
        """Type Mismatch In Statement For Return Statement"""
        input = """
        float foo(int n)
        {
            return true;
        }
        void main(){
           return;
        }
        """
        expect= "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 465))
    def test_type_mismatch_in_statement_17(self):
        """Type Mismatch In Statement For Return Statement"""
        input = """
        string checkString(string str)
           {
               return false;
           }
        void main(){
           checkString("ABCD");
        }
        """
        expect= "Type Mismatch In Statement: Return(BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input, expect, 466))
    def test_type_mismatch_in_statement_18(self):
        """Type Mismatch In Statement For Return Statement"""
        input = """
        int main(){
           return;
        }
        """
        expect= "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 467))
    def test_type_mismatch_in_statement_19(self):
        """Type Mismatch In Statement For Return Statement"""
        input = """
        void main(){
           int a;
           float b;
           string c;
           boolean d;
           return a=b=c=d;
        }
        """
        expect= "Type Mismatch In Statement: Return(BinaryOp(=,Id(a),BinaryOp(=,Id(b),BinaryOp(=,Id(c),Id(d)))))"
        self.assertTrue(TestChecker.test(input, expect, 468))
    def test_type_mismatch_in_statement_20(self):
        """Type Mismatch In Statement For Return Statement"""
        input = """
        int foo()
        {
            int n;
            int k;
            if (n<k)
            {
                return true;
            }
            else
            {
                k = k -1;
            }
        }
        void main(){
            return 0; 
        }
        """
        expect= "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 469))
#-----------------TEST TYPE MISMATCH IN EXPRESSION----------------
    def test_type_mismatch_in_expression_1(self):
        """Type Mismatch In Expression For ArrayPointer"""
        input = """
        void main(){
           int arr[100];
           float a;
           arr[a] = 10;
        }
        """
        expect= "Type Mismatch In Expression: ArrayCell(Id(arr),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 470))
    def test_type_mismatch_in_expression_2(self):
        """Type Mismatch In Expression For ArrayPointer"""
        input = """
        void main(){
           string str;
           int arr[100];
           arr[str] = arr[99];
           return;
        }
        """
        expect= "Type Mismatch In Expression: ArrayCell(Id(arr),Id(str))"
        self.assertTrue(TestChecker.test(input, expect, 471))
    def test_type_mismatch_in_expression_3(self):
        """Type Mismatch In Expression For ArrayPointer"""
        input = """
        void main(){
           int arr[10];
           arr[true] = 1;
           return 0;
        }
        """
        expect= "Type Mismatch In Expression: ArrayCell(Id(arr),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 472))
    def test_type_mismatch_in_expression_4(self):
        """Type Mismatch In Expression For ArrayPointer"""
        input = """
        void main(){
           int arr[100];
           arr[1.0] = 5;
        }
        """
        expect= "Type Mismatch In Expression: ArrayCell(Id(arr),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 473))
    def test_type_mismatch_in_expression_5(self):
        """Type Mismatch In Expression For Binary"""
        input = """
        void main(){
           1 - true;
           return;
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(-,IntLiteral(1),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 474))
    def test_type_mismatch_in_expression_6(self):
        """Type Mismatch In Expression For Unary"""
        input = """
        void main(){
           int a;
           a=100;
           !a;
           return;
        }
        """
        expect= "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 475))
    def test_type_mismatch_in_expression_7(self):
        """Type Mismatch In Expression For Binary"""
        input = """
        void main(){
           string str;
           int a;
           str < a;
           return 10;
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(<,Id(str),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 476))
    def test_type_mismatch_in_expression_8(self):
        """Type Mismatch In Expression Binary"""
        input = """
        void main(){
           5 > "abcd";
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(>,IntLiteral(5),StringLiteral(abcd))"
        self.assertTrue(TestChecker.test(input, expect, 477))
    def test_type_mismatch_in_expression_9(self):
        """Type Mismatch In Expression For Binary"""
        input = """
        void main(){
           boolean check;
           check = false;
           check % 10;

        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(%,Id(check),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input, expect, 478))
    def test_type_mismatch_in_expression_10(self):
        """Type Mismatch In Expression For Binary"""
        input = """
        void main(){
           float x;
           x = true;
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(=,Id(x),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 479))
    def test_type_mismatch_in_expression_11(self):
        """Type Mismatch In Expression For Function"""
        input = """
        int foo(int a, int b, string c)
        {
            return a;
        }
        void main(){
           foo(5,6,10);
        }
        """
        expect= "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(5),IntLiteral(6),IntLiteral(10)])"
        self.assertTrue(TestChecker.test(input, expect, 480))
    def test_type_mismatch_in_expression_12(self):
        """Type Mismatch In Expression For Function"""
        input = """
        int foo(int a, int b)
        {
            int c;
            c = (a + b) /2;
            return c;
        }
        void main(){
           foo(5);
        }
        """
        expect= "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input, expect, 481))
    def test_type_mismatch_in_expression_13(self):
        """Type Mismatch In Expression For Function"""
        input = """
        int foo(int a, int b)
        {
            if (a<b)
            {
                return 1;
            } 
            else
            {
                return 0;
            }
        }
        void main(){
           foo(2,3,5);
        }
        """
        expect= "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(2),IntLiteral(3),IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input, expect, 482))
    def test_type_mismatch_in_expression_14(self):
        """Type Mismatch In Expression For Function"""
        input = """
        int foo(string str)
        {
            return 1;
        }
        void main(){
           foo(100);
           return;
        }
        """
        expect= "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(100)])"
        self.assertTrue(TestChecker.test(input, expect, 483))
    def test_type_mismatch_in_expression_15(self):
        """Type Mismatch In Expression For Function"""
        input = """
        int foo(string n)
        {
            return 0;
        }
        void main(){
           foo(true);
           return;
        }
        """
        expect= "Type Mismatch In Expression: CallExpr(Id(foo),[BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input, expect, 484))
    def test_type_mismatch_in_expression_16(self):
        """Type Mismatch In Expression"""
        input = """
        void main(){
           int a;
           boolean b;
           a= 100;
           b = a;
           return;
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(=,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 485))
    def test_type_mismatch_in_expression_17(self):
        """ """
        input = """
        int a;
        void main(){
           a(100);
           return;
        }
        """
        expect= "Type Mismatch In Expression: CallExpr(Id(a),[IntLiteral(100)])"
        self.assertTrue(TestChecker.test(input, expect, 486))
#--------------TEST SIMPLE PROGRAM------------------
    def test_simple_program_1(self):
        """Simple Program"""
        input = """
        boolean isPrime(int n)
        {
            if (n=2)
            {
                return true;
            }
            else
                {
                    if(n<2)
                    {
                        return false;
                    }
                    else
                    {
                        return 1;
                    }
                }

        }
        void main(){
         isPrime(5);
         return;
        }
        """
        expect= "Type Mismatch In Statement: If(BinaryOp(=,Id(n),IntLiteral(2)),Block([Return(BooleanLiteral(true))]),Block([If(BinaryOp(<,Id(n),IntLiteral(2)),Block([Return(BooleanLiteral(false))]),Block([Return(IntLiteral(1))]))]))"
        self.assertTrue(TestChecker.test(input, expect, 487))
    def test_simple_program_2(self):
        """"""
        input = """
        int foo(int x)
        {
            int i;
            for (i=0.0;i<10;i=i+1)
            {
                x = x + i;
            }
        }
        void main(){
           foo(10);
           return;
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(=,Id(i),FloatLiteral(0.0))"
        self.assertTrue(TestChecker.test(input, expect, 488))
    def test_simple_program_3(self):
        """ Simple Program"""
        input = """
        void main(){
           int x;
           x = 1; 
           do
           {
               if (x<10)
               {
                   x = true;
                   break;
               }
               continue;
           }
           while(true);
           
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(=,Id(x),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 489))
    def test_simple_program_4(self):
        """Simple Program """
        input = """
        int foo(int n)
        {
            if (n< 100)
            {
                return 100*n+200%10+5000/200+1.5/n%1000;
            }
        }
        void main(){
           foo(10);
           return;
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(*,IntLiteral(100),Id(n)),BinaryOp(%,IntLiteral(200),IntLiteral(10))),BinaryOp(/,IntLiteral(5000),IntLiteral(200))),BinaryOp(%,BinaryOp(/,FloatLiteral(1.5),Id(n)),IntLiteral(1000)))"
        self.assertTrue(TestChecker.test(input, expect, 490))
    def test_simple_program_5(self):
        """Simple Program """
        input = """
        int foo(int a,float b, int c, string d)
        {
            if (a<b)
            {
                return 1;
            }
            else
            {
                return 0;
            }
            do
            {
                c = c-1;
            }
            while(a<c);
        }
        void main(){
           int a;
           float b;
           string c;
           boolean d;
           foo(a,b,c,d);
        }
        """
        expect= "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b),Id(c),Id(d)])"
        self.assertTrue(TestChecker.test(input, expect, 491))
    def test_simple_program_6(self):
        """Simple Program"""
        input = """
        void main(){
           int a;
           string str;
           foo(a,str);
           float b;
           b = 10.1;
        }
        """
        expect= "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 492))
    def test_simple_program_7(self):
        """Simple Program"""
        input = """
        float c;
        void main(){
           int c; 
           c = 10;
           string c;
        }
        """
        expect= "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 493))
    def test_simple_program_8(self):
        """Simple Program"""
        input = """
        int a;
        void main(){
           a= 10.1;
           for (1;true;100)
           {
               break;
           }
           do
           {
               continue;
           }
           while(true);
        }
        """
        expect= "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(10.1))"
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test_simple_program_9(self):
        """Simple Program"""
        input = """
        int foo(int n)
        {
            int a;
            a=getInt();
            if (n<a)
            {
                n = n + 10;
            }
            else
            {
                return n;
            }
        }
        """
        expect= "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 495))
    def test_simple_program_10(self):
        """Simple Program"""
        input = """
        int foo(int n)
        {
            n = n + 10;
            int k;
            for(k;k<n;k=k+1)
            {
                break;
            }
        }
        void main(){
           foo(5);
           return;
        }
        """
        expect= "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 496))
    def test_simple_program_11(self):
        """Simple Program"""
        input = """
        float a;
        boolean check;
        void main(){
           int k;
           if (check)
           {
               c= a;
               return;
           }
           else
           {
               check = true;
           }
        }
        """
        expect= "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 497))
    def test_simple_program_12(self):
        """Simple Program"""
        input = """
        void check(string str)
        {
            if (true)
            {
                return str;
            }
        }
        void main(){
           check("100");
           return 1;
        }
        """
        expect= "Type Mismatch In Statement: Return(Id(str))"
        self.assertTrue(TestChecker.test(input, expect, 498))
    def test_simple_program_13(self):
        """Simple Program"""
        input = """
        int foo(int k)
        {
            k = k /10;
            return k;
        }
        void main(){
            int a;
           if (a<5)
           {
               break;
               foo(100);
           }
           else
           {
               foo(10);
           }
           do
           {
               continue;
           }
           while(true);
        }
        """
        expect= "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 499))