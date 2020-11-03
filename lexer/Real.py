from Token import Token


class Real(Token):

    def __init__(self, value, line):
        super(Real, self).__init__(value, 13, line)

    def toString(self):
        return "Real - Value = " + self.value
