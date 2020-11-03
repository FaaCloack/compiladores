class Token(object):

    def __init__(self, token, tag, line):
        self.value = token
        self.tag = tag
        self.line = line

    def toString(self):
        return "Token - Value = " + self.value
