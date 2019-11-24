# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *
import sys,os



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62")
        buf.write("\u017c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\2\3\2\7\2n\n\2\f\2\16\2q\13\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3|\n\3\f\3\16\3\177\13")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3")
        buf.write("(\3)\3)\3*\6*\u010c\n*\r*\16*\u010d\3+\3+\5+\u0112\n+")
        buf.write("\3+\7+\u0115\n+\f+\16+\u0118\13+\3+\3+\3+\3+\3+\5+\u011f")
        buf.write("\n+\3+\5+\u0122\n+\3+\6+\u0125\n+\r+\16+\u0126\5+\u0129")
        buf.write("\n+\5+\u012b\n+\3,\3,\3,\3,\7,\u0131\n,\f,\16,\u0134\13")
        buf.write(",\3,\3,\3,\3-\3-\5-\u013b\n-\3.\3.\7.\u013f\n.\f.\16.")
        buf.write("\u0142\13.\3/\3/\3/\3/\5/\u0148\n/\3\60\6\60\u014b\n\60")
        buf.write("\r\60\16\60\u014c\3\60\5\60\u0150\n\60\3\60\5\60\u0153")
        buf.write("\n\60\3\60\6\60\u0156\n\60\r\60\16\60\u0157\5\60\u015a")
        buf.write("\n\60\3\61\6\61\u015d\n\61\r\61\16\61\u015e\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\7\62\u0167\n\62\f\62\16\62\u016a")
        buf.write("\13\62\3\62\3\62\3\63\3\63\3\63\3\63\7\63\u0172\n\63\f")
        buf.write("\63\16\63\u0175\13\63\3\63\3\63\3\63\3\63\3\64\3\64\3")
        buf.write("o\2\65\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\2#\2%\22\'\23)\24+\25-\26")
        buf.write("/\27\61\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#")
        buf.write("I$K%M&O\'Q(S)U*W+Y,[-]._\2a/c\60e\61g\62\3\2\13\3\2\f")
        buf.write("\f\3\2\62;\4\2GGgg\t\2$$^^ddhhppttvv\6\2\n\f\16\17$$^")
        buf.write("^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\7\2ddh")
        buf.write("hppttvv\2\u0194\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2%\3\2\2")
        buf.write("\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2")
        buf.write("\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2")
        buf.write("\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2")
        buf.write("\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3")
        buf.write("\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U")
        buf.write("\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\3i\3\2\2\2")
        buf.write("\5w\3\2\2\2\7\u0082\3\2\2\2\t\u0086\3\2\2\2\13\u0089\3")
        buf.write("\2\2\2\r\u008e\3\2\2\2\17\u0093\3\2\2\2\21\u009b\3\2\2")
        buf.write("\2\23\u00a1\3\2\2\2\25\u00a8\3\2\2\2\27\u00ae\3\2\2\2")
        buf.write("\31\u00b7\3\2\2\2\33\u00bb\3\2\2\2\35\u00c2\3\2\2\2\37")
        buf.write("\u00c5\3\2\2\2!\u00cb\3\2\2\2#\u00d0\3\2\2\2%\u00d6\3")
        buf.write("\2\2\2\'\u00d8\3\2\2\2)\u00db\3\2\2\2+\u00de\3\2\2\2-")
        buf.write("\u00e1\3\2\2\2/\u00e4\3\2\2\2\61\u00e6\3\2\2\2\63\u00e9")
        buf.write("\3\2\2\2\65\u00eb\3\2\2\2\67\u00ee\3\2\2\29\u00f0\3\2")
        buf.write("\2\2;\u00f2\3\2\2\2=\u00f4\3\2\2\2?\u00f6\3\2\2\2A\u00f8")
        buf.write("\3\2\2\2C\u00fa\3\2\2\2E\u00fc\3\2\2\2G\u00fe\3\2\2\2")
        buf.write("I\u0100\3\2\2\2K\u0102\3\2\2\2M\u0104\3\2\2\2O\u0106\3")
        buf.write("\2\2\2Q\u0108\3\2\2\2S\u010b\3\2\2\2U\u012a\3\2\2\2W\u012c")
        buf.write("\3\2\2\2Y\u013a\3\2\2\2[\u013c\3\2\2\2]\u0147\3\2\2\2")
        buf.write("_\u014a\3\2\2\2a\u015c\3\2\2\2c\u0162\3\2\2\2e\u016d\3")
        buf.write("\2\2\2g\u017a\3\2\2\2ij\7\61\2\2jk\7,\2\2ko\3\2\2\2ln")
        buf.write("\13\2\2\2ml\3\2\2\2nq\3\2\2\2op\3\2\2\2om\3\2\2\2pr\3")
        buf.write("\2\2\2qo\3\2\2\2rs\7,\2\2st\7\61\2\2tu\3\2\2\2uv\b\2\2")
        buf.write("\2v\4\3\2\2\2wx\7\61\2\2xy\7\61\2\2y}\3\2\2\2z|\n\2\2")
        buf.write("\2{z\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0080\3")
        buf.write("\2\2\2\177}\3\2\2\2\u0080\u0081\b\3\2\2\u0081\6\3\2\2")
        buf.write("\2\u0082\u0083\7k\2\2\u0083\u0084\7p\2\2\u0084\u0085\7")
        buf.write("v\2\2\u0085\b\3\2\2\2\u0086\u0087\7k\2\2\u0087\u0088\7")
        buf.write("h\2\2\u0088\n\3\2\2\2\u0089\u008a\7g\2\2\u008a\u008b\7")
        buf.write("n\2\2\u008b\u008c\7u\2\2\u008c\u008d\7g\2\2\u008d\f\3")
        buf.write("\2\2\2\u008e\u008f\7x\2\2\u008f\u0090\7q\2\2\u0090\u0091")
        buf.write("\7k\2\2\u0091\u0092\7f\2\2\u0092\16\3\2\2\2\u0093\u0094")
        buf.write("\7d\2\2\u0094\u0095\7q\2\2\u0095\u0096\7q\2\2\u0096\u0097")
        buf.write("\7n\2\2\u0097\u0098\7g\2\2\u0098\u0099\7c\2\2\u0099\u009a")
        buf.write("\7p\2\2\u009a\20\3\2\2\2\u009b\u009c\7h\2\2\u009c\u009d")
        buf.write("\7n\2\2\u009d\u009e\7q\2\2\u009e\u009f\7c\2\2\u009f\u00a0")
        buf.write("\7v\2\2\u00a0\22\3\2\2\2\u00a1\u00a2\7u\2\2\u00a2\u00a3")
        buf.write("\7v\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6")
        buf.write("\7p\2\2\u00a6\u00a7\7i\2\2\u00a7\24\3\2\2\2\u00a8\u00a9")
        buf.write("\7d\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac")
        buf.write("\7c\2\2\u00ac\u00ad\7m\2\2\u00ad\26\3\2\2\2\u00ae\u00af")
        buf.write("\7e\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7v\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5")
        buf.write("\7w\2\2\u00b5\u00b6\7g\2\2\u00b6\30\3\2\2\2\u00b7\u00b8")
        buf.write("\7h\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7t\2\2\u00ba\32")
        buf.write("\3\2\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1")
        buf.write("\7p\2\2\u00c1\34\3\2\2\2\u00c2\u00c3\7f\2\2\u00c3\u00c4")
        buf.write("\7q\2\2\u00c4\36\3\2\2\2\u00c5\u00c6\7y\2\2\u00c6\u00c7")
        buf.write("\7j\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca \3\2\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd")
        buf.write("\7t\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf\7g\2\2\u00cf\"")
        buf.write("\3\2\2\2\u00d0\u00d1\7h\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3")
        buf.write("\7n\2\2\u00d3\u00d4\7u\2\2\u00d4\u00d5\7g\2\2\u00d5$\3")
        buf.write("\2\2\2\u00d6\u00d7\7?\2\2\u00d7&\3\2\2\2\u00d8\u00d9\7")
        buf.write("~\2\2\u00d9\u00da\7~\2\2\u00da(\3\2\2\2\u00db\u00dc\7")
        buf.write("(\2\2\u00dc\u00dd\7(\2\2\u00dd*\3\2\2\2\u00de\u00df\7")
        buf.write("?\2\2\u00df\u00e0\7?\2\2\u00e0,\3\2\2\2\u00e1\u00e2\7")
        buf.write("#\2\2\u00e2\u00e3\7?\2\2\u00e3.\3\2\2\2\u00e4\u00e5\7")
        buf.write(">\2\2\u00e5\60\3\2\2\2\u00e6\u00e7\7>\2\2\u00e7\u00e8")
        buf.write("\7?\2\2\u00e8\62\3\2\2\2\u00e9\u00ea\7@\2\2\u00ea\64\3")
        buf.write("\2\2\2\u00eb\u00ec\7@\2\2\u00ec\u00ed\7?\2\2\u00ed\66")
        buf.write("\3\2\2\2\u00ee\u00ef\7-\2\2\u00ef8\3\2\2\2\u00f0\u00f1")
        buf.write("\7/\2\2\u00f1:\3\2\2\2\u00f2\u00f3\7\61\2\2\u00f3<\3\2")
        buf.write("\2\2\u00f4\u00f5\7,\2\2\u00f5>\3\2\2\2\u00f6\u00f7\7\'")
        buf.write("\2\2\u00f7@\3\2\2\2\u00f8\u00f9\7#\2\2\u00f9B\3\2\2\2")
        buf.write("\u00fa\u00fb\7*\2\2\u00fbD\3\2\2\2\u00fc\u00fd\7+\2\2")
        buf.write("\u00fdF\3\2\2\2\u00fe\u00ff\7}\2\2\u00ffH\3\2\2\2\u0100")
        buf.write("\u0101\7\177\2\2\u0101J\3\2\2\2\u0102\u0103\7=\2\2\u0103")
        buf.write("L\3\2\2\2\u0104\u0105\7.\2\2\u0105N\3\2\2\2\u0106\u0107")
        buf.write("\7]\2\2\u0107P\3\2\2\2\u0108\u0109\7_\2\2\u0109R\3\2\2")
        buf.write("\2\u010a\u010c\t\3\2\2\u010b\u010a\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e")
        buf.write("T\3\2\2\2\u010f\u0111\5_\60\2\u0110\u0112\7\60\2\2\u0111")
        buf.write("\u0110\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u012b\3\2\2\2")
        buf.write("\u0113\u0115\5_\60\2\u0114\u0113\3\2\2\2\u0115\u0118\3")
        buf.write("\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0119")
        buf.write("\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011a\7\60\2\2\u011a")
        buf.write("\u012b\5_\60\2\u011b\u011c\5_\60\2\u011c\u0128\7\60\2")
        buf.write("\2\u011d\u011f\t\4\2\2\u011e\u011d\3\2\2\2\u011e\u011f")
        buf.write("\3\2\2\2\u011f\u0121\3\2\2\2\u0120\u0122\7/\2\2\u0121")
        buf.write("\u0120\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0124\3\2\2\2")
        buf.write("\u0123\u0125\t\3\2\2\u0124\u0123\3\2\2\2\u0125\u0126\3")
        buf.write("\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0129")
        buf.write("\3\2\2\2\u0128\u011e\3\2\2\2\u0128\u0129\3\2\2\2\u0129")
        buf.write("\u012b\3\2\2\2\u012a\u010f\3\2\2\2\u012a\u0116\3\2\2\2")
        buf.write("\u012a\u011b\3\2\2\2\u012bV\3\2\2\2\u012c\u0132\7$\2\2")
        buf.write("\u012d\u012e\7^\2\2\u012e\u0131\t\5\2\2\u012f\u0131\n")
        buf.write("\6\2\2\u0130\u012d\3\2\2\2\u0130\u012f\3\2\2\2\u0131\u0134")
        buf.write("\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133")
        buf.write("\u0135\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0136\7$\2\2")
        buf.write("\u0136\u0137\b,\3\2\u0137X\3\2\2\2\u0138\u013b\5!\21\2")
        buf.write("\u0139\u013b\5#\22\2\u013a\u0138\3\2\2\2\u013a\u0139\3")
        buf.write("\2\2\2\u013bZ\3\2\2\2\u013c\u0140\t\7\2\2\u013d\u013f")
        buf.write("\t\b\2\2\u013e\u013d\3\2\2\2\u013f\u0142\3\2\2\2\u0140")
        buf.write("\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\\\3\2\2\2\u0142")
        buf.write("\u0140\3\2\2\2\u0143\u0148\5S*\2\u0144\u0148\5U+\2\u0145")
        buf.write("\u0148\5Y-\2\u0146\u0148\5W,\2\u0147\u0143\3\2\2\2\u0147")
        buf.write("\u0144\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2")
        buf.write("\u0148^\3\2\2\2\u0149\u014b\t\3\2\2\u014a\u0149\3\2\2")
        buf.write("\2\u014b\u014c\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d")
        buf.write("\3\2\2\2\u014d\u0159\3\2\2\2\u014e\u0150\t\4\2\2\u014f")
        buf.write("\u014e\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0152\3\2\2\2")
        buf.write("\u0151\u0153\7/\2\2\u0152\u0151\3\2\2\2\u0152\u0153\3")
        buf.write("\2\2\2\u0153\u0155\3\2\2\2\u0154\u0156\t\3\2\2\u0155\u0154")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0155\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u015a\3\2\2\2\u0159\u014f\3\2\2\2")
        buf.write("\u0159\u015a\3\2\2\2\u015a`\3\2\2\2\u015b\u015d\t\t\2")
        buf.write("\2\u015c\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160\3\2\2\2\u0160")
        buf.write("\u0161\b\61\2\2\u0161b\3\2\2\2\u0162\u0168\7$\2\2\u0163")
        buf.write("\u0164\7^\2\2\u0164\u0167\t\5\2\2\u0165\u0167\n\6\2\2")
        buf.write("\u0166\u0163\3\2\2\2\u0166\u0165\3\2\2\2\u0167\u016a\3")
        buf.write("\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016b")
        buf.write("\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016c\b\62\4\2\u016c")
        buf.write("d\3\2\2\2\u016d\u0173\7$\2\2\u016e\u016f\7^\2\2\u016f")
        buf.write("\u0172\t\5\2\2\u0170\u0172\n\6\2\2\u0171\u016e\3\2\2\2")
        buf.write("\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3")
        buf.write("\2\2\2\u0173\u0174\3\2\2\2\u0174\u0176\3\2\2\2\u0175\u0173")
        buf.write("\3\2\2\2\u0176\u0177\7^\2\2\u0177\u0178\n\n\2\2\u0178")
        buf.write("\u0179\b\63\5\2\u0179f\3\2\2\2\u017a\u017b\13\2\2\2\u017b")
        buf.write("h\3\2\2\2\34\2o}\u010d\u0111\u0116\u011e\u0121\u0126\u0128")
        buf.write("\u012a\u0130\u0132\u013a\u0140\u0147\u014c\u014f\u0152")
        buf.write("\u0157\u0159\u015e\u0166\u0168\u0171\u0173\6\b\2\2\3,")
        buf.write("\2\3\62\3\3\63\4")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    LINECOMMENT = 2
    INT = 3
    IF = 4
    ELSE = 5
    VOID = 6
    BOOLEAN = 7
    FLOAT = 8
    STRING = 9
    BREAK = 10
    CONTINUE = 11
    FOR = 12
    RETURN = 13
    DO = 14
    WHILE = 15
    ASSIGN = 16
    OR = 17
    AND = 18
    EQUAL = 19
    NOTEQUAL = 20
    LESS = 21
    LESSEQUAL = 22
    GREATER = 23
    GREATEREQUAL = 24
    ADD = 25
    SUB = 26
    DIV = 27
    MUL = 28
    MOD = 29
    NOT = 30
    LB = 31
    RB = 32
    LP = 33
    RP = 34
    SM = 35
    CM = 36
    LS = 37
    RS = 38
    INTLIT = 39
    FLOATLIT = 40
    STRINGLIT = 41
    BOOLEANLIT = 42
    ID = 43
    LITERAL = 44
    WS = 45
    UNCLOSE_STRING = 46
    ILLEGAL_ESCAPE = 47
    ERROR_CHAR = 48

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'if'", "'else'", "'void'", "'boolean'", "'float'", 
            "'string'", "'break'", "'continue'", "'for'", "'return'", "'do'", 
            "'while'", "'='", "'||'", "'&&'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'+'", "'-'", "'/'", "'*'", "'%'", "'!'", "'('", 
            "')'", "'{'", "'}'", "';'", "','", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "LINECOMMENT", "INT", "IF", "ELSE", "VOID", "BOOLEAN", 
            "FLOAT", "STRING", "BREAK", "CONTINUE", "FOR", "RETURN", "DO", 
            "WHILE", "ASSIGN", "OR", "AND", "EQUAL", "NOTEQUAL", "LESS", 
            "LESSEQUAL", "GREATER", "GREATEREQUAL", "ADD", "SUB", "DIV", 
            "MUL", "MOD", "NOT", "LB", "RB", "LP", "RP", "SM", "CM", "LS", 
            "RS", "INTLIT", "FLOATLIT", "STRINGLIT", "BOOLEANLIT", "ID", 
            "LITERAL", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "LINECOMMENT", "INT", "IF", "ELSE", "VOID", 
                  "BOOLEAN", "FLOAT", "STRING", "BREAK", "CONTINUE", "FOR", 
                  "RETURN", "DO", "WHILE", "TRUE", "FALSE", "ASSIGN", "OR", 
                  "AND", "EQUAL", "NOTEQUAL", "LESS", "LESSEQUAL", "GREATER", 
                  "GREATEREQUAL", "ADD", "SUB", "DIV", "MUL", "MOD", "NOT", 
                  "LB", "RB", "LP", "RP", "SM", "CM", "LS", "RS", "INTLIT", 
                  "FLOATLIT", "STRINGLIT", "BOOLEANLIT", "ID", "LITERAL", 
                  "NUM", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[42] = self.STRINGLIT_action 
            actions[48] = self.UNCLOSE_STRING_action 
            actions[49] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text =self.text[1:-1] 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text =self.text.lstrip('"') 
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text =self.text.lstrip('"') 
     


