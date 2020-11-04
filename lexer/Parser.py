import tag as Tag
import csv
import utils


class Parser():
    actions = []
    gotos = []
    productions = []

    def __init__(self, input):
        self.tables()
        self.grammar()
        self.parse(input)

    def tables(self):
        csv_actions = csv.DictReader(open('data/actions.csv', mode='r'))
        csv_gotos = csv.DictReader(open('data/gotos.csv', mode='r'))
        # build actions and gotos tables
        for row in csv_actions:
            self.actions.append(row)

        for row in csv_gotos:
            self.gotos.append(row)

    def grammar(self):
        # read grammar and buld productions
        file = open('data/grammar.txt', 'r')
        lines = file.readlines()
        for line in lines:
            values = line.split()
            rule = []
            rule.append(values[0])
            rule.append(len(values) - 2)
            self.productions.append(rule)
        # print(self.productions[2])

    def parse(self, input):
        stack = []
        non_terminals = utils.non_terminals
        terminals = utils.terminals

        # initial values
        stack.append(0)
        state = 0
        input_read = 0

        while stack:
            try:
                # print(stack)
                symbol = stack.pop()
                stack.append(symbol)
                input_char = input[input_read].tag
                line = input[input_read].line

                # accepted case
                if(input_char == '$' and self.actions[state][input_char] == 'acc'):
                    print('ACCEPTED')
                    break
                # non-terminals / goto
                if (non_terminals.get(symbol)):
                    state = int(self.gotos[state][symbol])
                    #print('goto ' + str(state))
                    stack.append(state)
                # terminals / actions
                else:
                    state = int(symbol)
                    if(self.actions[state][input_char][0] == 's'):
                        # shift
                        state = int(self.actions[state][input_char][1:])
                        #print('shift ' + str(state))
                        stack.append(input_char)
                        stack.append(state)
                        input_read = input_read + 1
                    else:
                        # reduce
                        prod = int(self.actions[state][input_char][1:])
                        #print('reduce ' + str(prod))
                        times = self.productions[prod][1] * 2
                        for i in range(times):
                            stack.pop()
                        state = int(stack.pop())
                        stack.append(state)
                        stack.append(self.productions[int(prod)][0])
            except:
                print('Error in line: ' + str(line) + ' \'' + input_char + '\' not expected')
                break
