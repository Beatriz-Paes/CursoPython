"""
Desempacotamento de listas
"""
lista = ['Beah', 'Well', 'Ana', 'Rob', 'Dani', 'Lari']

n1, n2, *outra_lista, ultimo = lista

print(n1, n2, outra_lista, outra_lista[-2], ultimo)
