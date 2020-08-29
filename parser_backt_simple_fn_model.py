# Simple parser with backtracking without any
# class construct  but with the similar overall encapsulation.
# This meant for early students with litle knowledge of programming

# This is the exact thing I will ask students to do


producciones = {
    'S': [
        ['a', 'S', 'a'],
        ['a', 'a'],
    ]
}

no_terminales = ['S']

def es_no_terminal(simbolo):
    return simbolo in no_terminales

def es_terminal(simbolo):
    return not es_no_terminal(simbolo)



# grammar:
# S -> aSa | aa
def Parser(tokens):
    self = {
        'tokens': tokens,
        'index': 0,
        'error': False,
    }

    # Llamado "algoritmo" en el material
    def parse():
        pni('S')
        token_actual = self['tokens'][self['index']]
        if token_actual != 'eof' or self['error']:
            print('Unexpected input termination')
            return False

        return True

    def procesar(parteDerecha):
        # print('procesar', parteDerecha)
        for simbolo in parteDerecha:
            # print('procesar simbolo', simbolo)
            token_actual = self['tokens'][self['index']]
            self['error'] = False
            if es_terminal(simbolo):
                if simbolo == token_actual:
                    self['index'] += 1
                    # print('avanzo', self)
                else:
                    self['error'] = True
                    break

            elif es_no_terminal(simbolo):
                pni(simbolo)
                if self['error']:
                    break


    # Llamado "Pni"
    def pni(noTerminal):
        # print('pni', noTerminal)
        for parteDerecha in producciones[noTerminal]:
            pivote_retroceso = self['index']
            procesar(parteDerecha)
            if self['error'] == True:
                self['index'] = pivote_retroceso
                # print('backtrack', self)
            else:
                break


    return parse()



cases = [
    (True, ['a', 'a', 'eof']),
    (True, ['a', 'a', 'a', 'a', 'eof']),
    (True, ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'eof']),

    (False, ['a', 'eof']),
    (False, ['a', 'a', 'a', 'eof']),
]


def test_case(tokens):
    print('input:', tokens)
    res = Parser(tokens)
    return res

for (i, test) in enumerate(cases):
    print('\ntest', i)
    expected, case = test
    assert expected == test_case(case)
