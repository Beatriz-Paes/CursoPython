# Geradores, Iteradores e iteráveis

import time
import sys

lista = [0, 1, 2, 3, 4, 5]  # É iterável
print(hasattr(lista, '__next__'))  # Não é um iterador
lista = iter(lista)  # É um iterador

l2 = 123456
print(hasattr(l2, '__iter__'))  # Não é iterável

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

lista0 = [x for x in range(1000)]
lista1 = (x for x in range(1000))


print(sys.getsizeof(lista0))
print(sys.getsizeof(lista1))