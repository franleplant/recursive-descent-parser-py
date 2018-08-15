
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0

    def next_word(self):
        self.token_index += 1
        print("next word {0}".format(self.get_word()))
        return self.get_word()

    def get_word(self):
        return self.tokens[self.token_index]

    # TODO maybe add optional messages
    def fail(self):
        raise Exception("Syntax Error in token '{0}'".format(self.get_word()))

    # TODO each NonTerminal should return an entire sub tree
    def parse(self):
        expr = self.Expr()
        if expr != None:
            if self.get_word() == 'eof':
                return expr

        self.fail()

    # Expr ->  Term EPrime
    def Expr(self):
        print("Expr ->  Term EPrime")
        return ['TYPE: EXPR', self.Term(), self.EPrime()]

    # Term -> Factor TPrime
    def Term(self):
        print("Term -> Factor TPrime")
        return ['TYPE: TERM', self.Factor(), self.TPrime()]

    def EPrime(self):
        # EPrime -> + Term EPrime
        # EPrime -> - Term EPrime
        word = self.get_word()
        if word == '+' or word == '-':
            self.next_word()
            return ['TYPE: EPRIME', word, self.Term(), self.EPrime()]


        # EPrime -> Lambda
        # check the follow of EPrime
        if self.get_word() == ')' or self.get_word() == 'eof':
            return ['TYPE: EPRIME']

        self.fail()

    def TPrime(self):
        # Term -> x Factor TPrime
        # Term -> / Factor TPrime
        word = self.get_word()
        if word == 'x' or word == '/':
            self.next_word()
            return ['TYPE: TPRIME', word, self.Factor(), self.TPrime()]


        # TPrime -> Lambda
        # check the follow of TPrime
        word = self.get_word()
        if word == ')' or word == 'eof' or word == '+' or word == '-':
            return ['TYPE: TPRIME']

        self.fail()

    def Factor(self):
        print('Factor')
        # Factor -> ( Expr )
        if self.get_word() == '(':
            print("Factor -> ( Expr )")
            self.next_word()
            expr = self.Expr()
            if not self.get_word() == ')':
                self.fail()
            self.next_word()
            return ['TYPE: FACTOR', expr]

        # Factor -> num
        # Factor -> name
        word = self.get_word()
        if word == 'num' or word == 'name':
            print("Factor -> num | name")
            self.next_word()
            return ['TYPE: FACTOR', word]

        self.fail()










tokens = ['name', '+', 'name', 'x', 'name', 'eof']
parser = Parser(tokens)

assert parser.get_word() == tokens[0]
assert parser.next_word() == tokens[1]
assert parser.next_word() == tokens[2]
assert parser.next_word() == tokens[3]
assert parser.next_word() == tokens[4]
assert parser.next_word() == tokens[5]

parser = Parser(tokens)
res = parser.parse()
print(res)
assert res != None
