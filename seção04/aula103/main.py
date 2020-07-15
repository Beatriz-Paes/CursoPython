# Sobreposição de membros
"""
Associação - Usa | Agregação - Tem | Composição - E dono | Herança - É
"""


from seção04.aula103.classes import *

c1 = Cliente('Beatriz', 25)
c1.comprar()

print()

c2 = ClienteVip('Marcella', 23, 'Araujo')
c2.falar()