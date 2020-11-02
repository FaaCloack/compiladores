from Token import Token


class Word(Token):
    def __init__(self, lexeme, tag):
        super(Word, self).__init__(tag)
        self.lexeme = lexeme

    def toString(self):
        return "Word - Lexeme = " + self.lexeme
