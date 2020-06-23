# Criar, ler, escrever, apagar arquivos

# file = open('abc.txt', 'w+')
# file.write('Linha 1\n')     # Escrevendo linhas
# file.write('Linha 2\n')
# file.write('Linha 3\n')
#
# file.seek(0, 0)     # Voltando o cursor para o início do arquivo
# print('Lendo linhas:')
# print(file.read())      # Lendo o arquivo
# print('#'*50)
#
# file.seek(0, 0)
# print(file.readline(), end='')      # Ler uma linha
# print(file.readline(), end='')      # Ler a próxima linha
#
# file.seek(0, 0)
# print(file.readlines())             # Ler as linhas em uma lista
#
# file.close()                        # Fecha o arquivo

################################################################################

# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0, 0)
#     print(file.read())
#
# finally:
#     file.close()

################################################################################

with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0, 0)
    print(file.read())

################################################################################

with open('abc.txt', 'r') as file:
    print(file.read())

with open('abc.txt', 'a') as file:
    file.write('Outra linha\n')
    file.seek(0)

################################################################################

import os
import json

d1 = {
    'Pessoa1': {'nome': 'Luiz', 'idade': 32},
    'Pessoa2': {'nome': 'Beatriz', 'idade': 25},
    }

d1_json = json.dumps(d1, indent=True)

with open('abc.txt', 'w+') as file:
    file.write(d1_json)

################################################################################

os.remove('abc.txt')        # Apagando o arquivo
