from Token import Token


class Real(Token):

    def __init__(self, value):
        super(Real, self).__init__(262)
        self.value = value

    def toString(self):
        return "Real - Value = " + str(self.value)
