# Zip e Zip_longest - Unindo iteráveis

"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

from itertools import zip_longest, count

### Código

cidades = ['Manaus', 'Belém', 'São Paulo', 'Curitiba', 'Salvador']

### Código

estados = ['Amazonas', 'Pará', 'São Paulo', 'Paraná', 'Bahia']

cidades_estados = zip(estados, cidades)  # Uni até o último item da menor lista

# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))
#
# for valor in cidades_estados:
#     print(valor[0], valor[1])

print(list(cidades_estados))

indice = count()

nomes = ['Ana Paula', 'Beatriz', 'Marcella', 'Monique', 'Alessandro', 'Beto']

presentes = ['Dado', 'Bola', 'Flor', 'Óculos', 'Pc']

nomes_presentes = zip(indice, nomes, presentes)  # Uni e inclui a lista mais longa

for indice, nomes, presentes in nomes_presentes:
    print(indice, nomes, presentes)
