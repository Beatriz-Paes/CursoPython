"""
Split, Join, Enumerate
Split - Dividir uma string - str
Join - Juntar uma lista - str
Enumerate - Enumerar elementos da lista # list / iteráveis
"""
######################################################################
string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista = string.split(' ')
lista2 = string.split(',')

print(lista)
print(lista2)

palavra = ''
contagem = 0
for valor in lista:
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x).')

######################################################################

string2 = ' '.join(lista)
print(string2)

######################################################################
lista3 = [
    [1, 2, 3],
    [1, 2],
    [5, 6, 7, 8]
]
for v1, v2 in enumerate(lista):
    print(v1, v2)