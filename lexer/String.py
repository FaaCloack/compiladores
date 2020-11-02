from Token import Token


class String(Token):

    def __init__(self, value):
        super(String, self).__init__(291)
        self.value = value

    def toString(self):
        return "String - Value = " + self.value
