from Token import Token


class String(Token):

    def __init__(self, value, line):
        super(String, self).__init__(value, 'string', line)

    def toString(self):
        return "String - Value = " + self.value
