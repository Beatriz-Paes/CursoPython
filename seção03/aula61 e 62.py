# Exercício proposto (Não consegui fazer)
"""
Separar em grupos de 0 a 9
usando List comprehension
lista = ['0123456789', '0123456789', '0123456789', '0123456789', '0123456789', '0123456789']
retorno final = '0123456789.0123456789.0123456789.0123456789.0123456789'
"""

string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

lista = [string[n: n + 10] for n in range(0, len(string), 10)]
retorno = '.'.join(lista)
print(retorno)
