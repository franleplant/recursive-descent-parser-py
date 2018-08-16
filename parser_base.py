import json

class BaseParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0

    def get_token_index(self):
        return self.token_index

    def set_token_index(self, newValue):
        self.token_index = newValue
        return self.token_index

    def next_word(self):
        self.token_index += 1
        return self.get_word()

    def get_word(self):
        return self.tokens[self.token_index]

    def eat_word(self, expected_word):
        if self.get_word() == expected_word:
            self.next_word()
            return True

        return False

    def debug_state(self, msg):
        print("{0: ^10} {1: ^10} {2: <10}".format(self.get_token_index(), self.get_word(), msg))

    def fail(self, msg):
        raise Exception("Syntax Error in token '{0}'. Error Message: {1}".format(self.get_word(), msg))

    def parse(self):
        pass

tokens = ['name', '+', 'name', 'x', 'name', 'eof']
parser = BaseParser(tokens)

assert parser.get_word() == tokens[0]
assert parser.next_word() == tokens[1]
assert parser.next_word() == tokens[2]
assert parser.next_word() == tokens[3]
assert parser.next_word() == tokens[4]
assert parser.next_word() == tokens[5]
