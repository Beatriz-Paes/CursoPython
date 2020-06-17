# Count - Itertools

from itertools import count

# contador = count(start=10, step=0.1)
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(round(next(contador), 3))

contador = count(start=1)

lista = ['Beatriz', 'Larissa', 'Wesley']
lista.insert(1, 'Pedro')
lista = zip(contador, lista)

print(list(lista))
