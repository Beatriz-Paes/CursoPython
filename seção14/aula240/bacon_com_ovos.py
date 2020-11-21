# Unittest #2 com TDD
"""
1 - Receber um número inteiro
2 - Saber se o número NÃO é multiplo de 3 e 5:
    Passa fome
3 - Saber se o número é múltiplo somente de 3:
    bacon
4 - Saber se o número é múltiplo somente de 5:
    ovos
5 - Saber se o número é múltiplo de 3 e 5:
    bacon com ovos

"""


def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser inteiro.'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
    if n % 3 == 0:
        return 'Bacon'
    if n % 5 == 0:
        return 'Ovos'

    return 'Passar fome'
