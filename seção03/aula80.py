# Modulos padrão do Python
# Modulos são arquivos .py e servem para expandir
# as funcionalidades padrão da linguagem.
# https://docs.python.org//py-modindex.html

# import sys
# print(sys.platform)

from sys import platform as so
import random
# ou -> from random import randint


print(so)   # Verifica em qual plataforma o python está sendo executado

for n in range(10):
    print(random.randint(0, 10))    # A cada iteração mostra um número aleatório entre 0 e 10
