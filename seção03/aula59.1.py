# Exercício - Minha solução (Não funcionou para todas as listas)

"""
-> É uma lista de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números de 1 a 10 e eles podem ser duplicados

Exercício

-> Crie uma função que encontra o primeiro número duplicado na lista interna

    requisitos:
        A ordem dos números duplicados é considerada a partir da segunda
        ocorrência (o número duplicado em si).
        Exemplo: [1, 2, 3, ->3<-, 2, 1] 3
        Se não encontrar duplicados na lista retorne -1
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def funcao():

    lista = lista_de_listas_de_inteiros[int(num) - 1]
    repetidos = list()
    # print(lista)
    for n, i in enumerate(lista):
        c = lista.count(i)

        if c > 1:
            repetidos.append(lista[n])

    l2 = set(repetidos)
    l2 = list(l2)

    for b in repetidos:
        for a in l2:
            if a == b:
                repetidos.remove(b)
    # print(repetidos, len(repetidos))

    if len(repetidos) != 0:
        print()
        return f'#O primeiro número que se repete na lista {lista} é: {repetidos[0]}'

    return -1


while True:
    print()
    num = (input('Qual lista deseja analisar (de 1 a 12): '))

    if not num.isdigit() or not 0 < int(num) < 13:
        print('Caracter inválido!')
        continue

    print(funcao())
