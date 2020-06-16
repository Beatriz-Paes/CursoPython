# Comportamento de geradores e iteradores

# Listas, tuples, str -> Sequences -> Iterável
nome = 'Beatriz Paes'
iterador = iter(nome)
gerador = [letra for letra in nome]

try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
except:
    pass

for valor in iterador:
    print(valor)

print(next(gerador))

# for letra in nome:
#     print(letra)
#
# print('#' * 80)
#
# for letra in nome:
#     print(letra)