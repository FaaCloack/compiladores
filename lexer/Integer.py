from Token import Token


class Integer(Token):

    def __init__(self, value):
        super(Integer, self).__init__(261)
        self.value = value

    def toString(self):
        return "Integer - Value = " + str(self.value)
