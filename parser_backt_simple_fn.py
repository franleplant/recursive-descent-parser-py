# Simpre parser with backtracking without any
# class construct  but with the similar overall encapsulation.
# This meant for early students with litle knowledge of programming
import json

from parser_base import BaseParser

# grammar:
# S -> aSa | aa
def Parser(tokens):
    self = {
        'backtrack_id': 0,
        'tokens': tokens,
        'token_index': 0,
    }

    def get_token_index():
        return self['token_index']

    def set_token_index(newValue):
        self['token_index'] = newValue
        return newValue

    def get_word():
        tokens = self['tokens']
        token_index = self['token_index']
        return tokens[token_index]

    def next_word():
        self['token_index'] += 1
        return get_word()


    #TODO not use
    def eat_word(expected_word):
        if get_word() == expected_word:
            next_word()
            return True

        return False

    def get_backtrack_id():
        id = self['backtrack_id']
        self['backtrack_id'] += 1
        return id

    def parse():
        result = S()
        if get_word() != 'eof' or result == None:
            print('Unexpected input termination')
            return None

        return result

    def S():
        result = None

        backtrack_pivot = get_token_index()
        backtrack_id = get_backtrack_id()

        # S -> a S a
        if eat_word('a'):
            s = S()
            if s != None:
                if eat_word('a'):
                    return {'type': 'S', 'children': ['a', s, 'a']}

        # BACTRACK
        set_token_index(backtrack_pivot)

        # S -> a a
        if eat_word('a'):
            if eat_word('a'):
                return {'type': 'S', 'children': ['a', 'a']}

        # BACTRACK
        return None


    return parse()




def test_case(tokens):
    print('\ninput:', tokens)
    res = Parser(tokens)
    print(json.dumps(res, indent=2))
    return res

assert None != test_case(['a', 'a', 'eof'])
assert None != test_case(['a', 'a', 'a', 'a', 'eof'])
assert None != test_case(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'eof'])

# FAIL
assert None == test_case(['a', 'eof'])
assert None == test_case(['a', 'a', 'a', 'eof'])
