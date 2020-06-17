# Groupby - Agrupando valores

alunos = [
    {'nome': 'Beatriz', 'nota': 'D'},
    {'nome': 'Roberta', 'nota': 'A'},
    {'nome': 'Geovana', 'nota': 'B'},
    {'nome': 'Fernando', 'nota': 'C'},
    {'nome': 'Rogério', 'nota': 'A'},
    {'nome': 'Jonathas', 'nota': 'A'},
    {'nome': 'Joyce', 'nota': 'D'},
    {'nome': 'Gabriela', 'nota': 'B'},
    {'nome': 'Frank', 'nota': 'C'},
    {'nome': 'Brian', 'nota': 'A'},
]

from itertools import groupby, tee

ordena = lambda item: item['nota']
alunos.sort(key=ordena)     # Ordenar os dados antes de agrupar
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, val_agrupados in alunos_agrupados:
    va1, va2 = tee(val_agrupados)

    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t {aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota: {agrupamento}')
    print()
