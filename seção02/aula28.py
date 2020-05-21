"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)
> - Esquerda
< - Direita
^ - Centro
"""

num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = 'Beatriz Paes'
print(f'{nome:s}')
print(f'{num1:0>10}')
print(f'{num1:1^15}')
print(f'{nome:#^50}')

nomeformat = '{:@>15}'.format(nome)
print(nomeformat)
print('{1:$^20}'.format(nomeformat, nome))


print(nome.lower())  # Tudo minúsculo
print(nome.upper())  # Tudo maiúsculo
print(nome.title())  # Primeiras letras maiúsculas
