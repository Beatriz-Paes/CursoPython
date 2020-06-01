"""
For / Else em Python
"""

variavel = ['bea', 'ana', 'maria']

for nome in variavel:
    if nome.startswith('b'):
        print(f'{nome} começa com b')
    else:
        print(f'{nome} não começa com j')

########################################################

variavel = ['bea', 'Ana', 'Maria']

comeca = False

for nome in variavel:
    if nome.lower().startswith('b'):
        comeca = True

if comeca:
    print('Existe uma palavra que começa com b')
else:
    print('Não existe uma palavra que começa com b')

########################################################
