
"""
# Funções - def
*args **kwargs
"""

# def funcao(a1, a2, a3=None):
#     print(a1, a2, a3)
#     return a1, a2, a3
#
# var = funcao(1, 2, a3='Beah')
# print(var[2])

def func(*args, **kwargs):
    print(args, kwargs['nome'], kwargs['sobrenome'])

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

func(*lista, *lista2, nome='Luíz', sobrenome='Miranda')
