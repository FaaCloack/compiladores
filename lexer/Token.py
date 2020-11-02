class Token(object):

    def __init__(self, tag):
        self.tag = tag

    def toString(self):
        return "Token - Value = " + str(self.tag)
