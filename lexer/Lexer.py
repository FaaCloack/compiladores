import tag as Tag
from Word import Word
from String import String
from Token import Token
from Integer import Integer
from Real import Real
from Parser import Parser
import utils


class Lexer():
    table = utils.table
    symbols = utils.symbols
    channel_values = []
    big_string = ''
    reading_string = False

    def __init__(self, filename):
        self.filename = filename
        file = open(filename, 'r')
        lines = file.readlines()
        l = 1
        for line in lines:
            values = line.split()
            self.scan(values, l)
            l = l + 1
        # Go to Parser
        self.channel_values.append(Token('$', '$', l))
        Parser(self.channel_values)

    def scan(self, values, line):
        comment = False

        for v in values:
            word = v.lower()
            # print(word)
            if comment:
                if word[0] == '*':
                    comment = False
            else:
                # check for strings
                if self.reading_string:
                    self.words(v, line)
                else:
                    # check for integers
                    if word.isdigit():
                        self.channel_values.append(Integer(int(word), line))
                        #print(Integer(int(word), line).toString())
                    # check for symbols
                    elif word in self.symbols:
                        self.channel_values.append(Token(word, word, line))
                        #print(Token(word, self.symbols.get(word), line).toString())
                    # check for reserver words
                    elif word in self.table:
                        self.channel_values.append(Word(word, word, line))
                        #print(Word(word, self.table.get(word), line).toString())
                    # check for comments
                    elif word == '(*':
                        comment = True
                    elif word == '*)':
                        comment = False
                    elif word[0].isdigit():
                        self.real(word, line)
                        # func real
                    else:
                        self.words(v, line)

    def words(self, word, line):
        str = ''
        for w in word:
            if w in self.symbols and self.reading_string == False:
                if str != '':
                    if str.lower() in self.table:
                        self.channel_values.append(Word(str, str.lower(), line))
                        #print(Word(str, self.table.get(str.lower()), line).toString())
                    else:
                        self.channel_values.append(Word(str, 'identifier', line))
                        #print(Word(str, Tag.IDENTIFIER, line).toString())
                    str = ''
                self.channel_values.append(Token(w, w, line))
                #print(Token(w, self.symbols.get(w), line).toString())
            else:
                str += w
                if w == "'" and self.reading_string == False:
                    self.reading_string = True
                elif w == "'" and self.reading_string:
                    self.big_string += str
                    self.channel_values.append(String(self.big_string, line))
                    #print(String(self.big_string, line).toString())
                    self.reading_string = False
                    str = ''
                    self.big_string = ''

        if self.reading_string:
            self.big_string += str + ' '
        else:
            if str != '':
                self.channel_values.append(Word(str, 'identifier', line))
                #print(Word(str, Tag.IDENTIFIER, line).toString())

    def real(self, word, line):
        str = ''
        for w in word:
            if w == '.':
                str += w
            elif w in self.symbols:
                if str != '':
                    self.channel_values.append(Real(float(str), line))
                    #print(Real(float(str), line).toString())
                    str = ''
                self.channel_values.append(Token(w, w, line))
                #print(Token(w, self.symbols.get(w), line).toString())
            elif w.isdigit():
                str += w
            else:
                print(word + ' is not a valid contruction')
                return

        if str != '':
            self.channel_values.append(Real(float(str), line))
            #print(Real(float(str), line).toString())
