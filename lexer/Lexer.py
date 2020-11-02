import tag as Tag
from Word import Word
from String import String
from Token import Token
from Integer import Integer
from Real import Real


class Lexer():
    hash_table = {}
    channel_values = []
    symbols = ['(', ')', '<', '>', '=', '-', '+', ':', ';', '/', '*', ',', '.']
    big_string = ''
    reading_string = False

    def __init__(self, filename):
        self.filename = filename
        program = Word("program", Tag.PROGRAM)
        constante = (Word("constante", Tag.CONSTANT))
        self.reserve(Word("==", Tag.EQ))
        self.reserve(Word("<>", Tag.NEQ))
        self.reserve(Word("<=", Tag.LE))
        self.reserve(Word(">=", Tag.GE))
        self.reserve(Word("minus", Tag.MINUS))
        self.reserve(Word(":=", Tag.ASSIGN))
        self.reserve(Word("true", Tag.TRUE))
        self.reserve(Word("false", Tag.FALSE))
        self.reserve(Word("program", Tag.PROGRAM))
        self.reserve(Word("constante", Tag.CONSTANT))
        self.reserve(Word("var", Tag.VAR))
        self.reserve(Word("begin", Tag.BEGIN))
        self.reserve(Word("end", Tag.END))
        self.reserve(Word("integer", Tag.INTEGER))
        self.reserve(Word("real", Tag.REAL))
        self.reserve(Word("boolean", Tag.BOOLEAN))
        self.reserve(Word("string", Tag.STRING))
        self.reserve(Word("writeln", Tag.WRITELN))
        self.reserve(Word("readln", Tag.READLN))
        self.reserve(Word("do", Tag.DO))
        self.reserve(Word("repeat", Tag.REPEAT))
        self.reserve(Word("until", Tag.UNTIL))
        self.reserve(Word("for", Tag.FOR))
        self.reserve(Word("to", Tag.TO))
        self.reserve(Word("downto", Tag.DOWNTO))
        self.reserve(Word("if", Tag.IF))
        self.reserve(Word("then", Tag.THEN))
        self.reserve(Word("else", Tag.ELSE))
        self.reserve(Word("not", Tag.NOT))
        self.reserve(Word("div", Tag.DIV))
        self.reserve(Word("mod", Tag.MOD))
        self.reserve(Word("and", Tag.AND))
        self.reserve(Word("or", Tag.OR))
        self.reserve(Word("while", Tag.WHILE))
        channel_values = open(filename).read().split()
        self.scan(channel_values)

    def reserve(self, word):
        self.hash_table[word.lexeme] = word

    def scan(self, values):
        comment = False

        for v in values:
            word = v.lower()
            # print(word)
            if comment:
                if word[0] == '*':
                    comment = False
            else:
                # check for reserved words
                if self.reading_string:
                    self.words(v)
                else:
                    if word in self.hash_table:
                        w = self.hash_table[word]
                        print(w.toString())
                    else:
                        # check for integers
                        if word.isdigit():
                            print(Integer(int(word)).toString())
                        # check for symbols
                        elif word in self.symbols:
                            print(Token(word).toString())
                        # check for comments
                        elif word == '(*':
                            comment = True
                        elif word == '*)':
                            comment = False
                        elif word[0].isdigit():
                            self.real(word)
                            # func real
                        else:
                            self.words(v)

    def words(self, word):
        str = ''
        for w in word:
            if w in self.symbols and self.reading_string == False:
                if str != '':
                    print(Word(str, Tag.ID).toString())
                    str = ''
                print(Token(w).toString())
            else:
                str += w
                if w == "'" and self.reading_string == False:
                    self.reading_string = True
                elif w == "'" and self.reading_string:
                    self.big_string += str
                    print(String(self.big_string).toString())
                    self.reading_string = False
                    str = ''
                    self.big_string = ''

        if self.reading_string:
            self.big_string += str + ' '
        else:
            if str != '':
                print(Word(str, Tag.ID).toString())

    def real(self, word):
        str = ''
        for w in word:
            if w == '.':
                str += w
            elif w in self.symbols:
                if str != '':
                    print(Real(float(str)).toString())
                    str = ''
                print(Token(w).toString())
            elif w.isdigit():
                str += w
            else:
                print(word + ' is not a valid contruction')
                return

        if str != '':
            print(Real(float(str)).toString())
