# Reduce

from dados import produtos, pessoas, lista
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preço'] + ac, produtos, 0)  # recebe uma função como parâmetro;
print(round(soma_precos / len(produtos)))  # Média de preços dos produtos

soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_idades / len(pessoas))
