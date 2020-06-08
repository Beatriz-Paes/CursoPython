# Expressões lambda (funções anônimas)

# def func(arg, arg2):
#     return arg * arg2
#
# var = func(2, 2)
# print(var)

a = lambda x, y: x * y
print(a(2, 2))

lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 7],
    ['p4', 50],
    ['p5', 8]
]

# def func(item):
#     return item[1]

lista.sort(key=lambda item: item[1], reverse=True)
print(lista)

print(sorted(lista, key=lambda i: i[1]))  # Ordena sem alterar a lista.
print(lista)
