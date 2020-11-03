from Token import Token


class Integer(Token):

    def __init__(self, value, line):
        super(Integer, self).__init__(value, 12, line)

    def toString(self):
        return "Integer - Value = " + self.value
