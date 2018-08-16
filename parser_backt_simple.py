import json

from parser_base import BaseParser

# grammar:
# S -> aSa | aa
class Parser(BaseParser):
    def __init__(self, *args):
        BaseParser.__init__(self, *args)
        self.backtrack_id = 0

    def get_backtrack_id(self):
        id = self.backtrack_id
        self.backtrack_id += 1
        return id

    def parse(self):
        result = self.S()
        self.debug_state('final_state')
        if self.get_word() != 'eof':
            print('Unexpected input termination 2')
            return None

        if result == None:
            print('Unexpected input termination 1')

        return result

        # expr = self.Expr()
        # if expr != None:
            # if self.get_word() == 'eof':
                # return expr

        # # In parsers that have backtracking you need to return None
        # # indicating that the branch failed
        # self.fail()

    def S(self):
        result = None

        backtrack_pivot = self.get_token_index()
        backtrack_id = self.get_backtrack_id()

        self.debug_state('{0} S -> a S a'.format(backtrack_id))
        if self.eat_word('a'):
            s = self.S()
            if s != None:
                if self.eat_word('a'):
                    return {'type': 'S', 'children': ['a', s, 'a']}

        self.set_token_index(backtrack_pivot)
        self.debug_state("{0} S -> a S a [ BACKTRACK ]".format(backtrack_id))

        self.debug_state('{0} S -> a a'.format(backtrack_id))
        if self.eat_word('a'):
            if self.eat_word('a'):
                return {'type': 'S', 'children': ['a', 'a']}

        self.debug_state('BACKTRACK remove subtree')
        return None





def test_case(tokens):
    print('\ninput:', tokens)
    parser = Parser(tokens)
    res = parser.parse()
    print(json.dumps(res, indent=2))
    return res

assert None != test_case(['a', 'a', 'eof'])
assert None != test_case(['a', 'a', 'a', 'a', 'eof'])
assert None != test_case(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'eof'])

# FAIL
assert None == test_case(['a', 'eof'])
assert None == test_case(['a', 'a', 'a', 'eof'])
