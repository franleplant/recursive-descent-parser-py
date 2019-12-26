# grammar
# Requires backtracking

# Goal -> Expr
# Expr -> Term Expr'
# Expr' -> + Term Expr'
#        | - Term Expr'
#        | Lambda
# Term -> Factor Term'
# Term' -> * Factor Term'
#        | % Factor Term'
#        | Lambda
# Factor -> ( Expr )
#         | num
#         | name

# TODOS
# -  mover prods a un archivo independinte
# - poner asserts aca
# - crear una version sin los print dbeugs y otro con
# - crear una version que construya el arbol
# - crear una version sin recursion y con stack

prods = {
    "S": [
        ["Expr"],
    ],

    "Expr": [
        ["Term", "Expr'"],
    ],

    "Expr'": [
        ["+", "Term", "Expr'"],
        ["-", "Term", "Expr'"],
        []
    ],

    "Term": [
        ["Factor", "Term'"],
    ],

    "Term'": [
        ["*", "Factor", "Term'"],
        ["%", "Factor", "Term'"],
        []
    ],

    "Factor": [
        ["(", "Expr", ")"],
        ["num"],
        ["name"],
    ],
}

def parser(prods, tokens):
    state = {
        "token_index": 0,
        "error": False,
        "derivaciones": [],
    }


    def parse():
        print(">>>TOKEN", tokens[state["token_index"]:])
        if procesar_no_terminal("S"):
            state["derivaciones"].reverse()
            # pertenece
            return state["derivaciones"]
        else:
            # no pertence
            return False

    # pni
    def procesar_no_terminal(no_terminal):
        print("procesar_no_terminal", no_terminal)
        backtrack_pivot = state["token_index"]

        for parte_derecha in prods[no_terminal]:
            state["token_index"] = backtrack_pivot
            if procesar_produccion(parte_derecha):
                state["derivaciones"].append((no_terminal, parte_derecha))
                print("derivaciones de", no_terminal, "->", parte_derecha)
                derivaciones = state["derivaciones"].copy()
                derivaciones.reverse()
                print("derivaciones", derivaciones)
                print("----------------")
                return True
        # Pensarlo como si devuelven la respuesta a la pregunta:
        # Funciono?
        return False


    # procesar
    # TODO how to build a very basic parse tree?
    def procesar_produccion(parte_derecha):
        print("  procesar_producion", parte_derecha)
        for simbolo in parte_derecha:
            print("    simbolo", simbolo)
            if es_terminal(simbolo):
                if get_token_tipo() == simbolo:
                    state["token_index"] += 1
                    print(">>>TOKEN avanza:", tokens[state["token_index"]:])
                else:
                    return False
            if es_no_terminal(simbolo):
                if procesar_no_terminal(simbolo) == False:
                    return False
        return True

    def get_token_tipo():
        token_index = state["token_index"]
        token_actual = tokens[token_index]
        (token_tipo, token_lexeme) = token_actual
        return token_tipo

    def es_no_terminal(simbolo):
        return simbolo in prods.keys()

    def es_terminal(simbolo):
        return not simbolo in prods.keys()


    return parse()





# a+b*c
tokens = [("name", "a"), ("+", "+"), ("name", "b"), ("*", "*"), ("name", "c"), ("eof", "eof")]
print(parser(prods, tokens))
