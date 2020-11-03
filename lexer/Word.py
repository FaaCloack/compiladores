from Token import Token


class Word(Token):
    def __init__(self, lexeme, tag, line):
        super(Word, self).__init__(lexeme, tag, line)

    def toString(self):
        return "Word - Lexeme = " + self.value
