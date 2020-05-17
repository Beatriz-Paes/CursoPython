"""
Operadores lógicos
and, or, not
in e not in
"""

# (verdadeiro E falso) = falso
#comp1 and comp2

# (verdadeiro ou falso) = verdadeiro
#comp1 and comp2

# not = inversor ou negação
a = ''
b = 3

"""
if not b > a:
   print('b é maior que a.')
######################################

if not a:
    print('Por favor digite um valor!')
else:
    print('a é maior que b.')
######################################

nome = input('Qual o seu nome? ')

if 'u' in nome:
    print('Existe a letra u no seu nome.')
"""

usuario = input('Nome de usuário: ')
senha = int(input('Digite sua senha: '))

usuario_bd = 'beatriz'
senha_bd = 123456

if usuario == usuario_bd and senha == senha_bd:
    print(f'Olá {usuario}, você está conectado.')
else:
    print('Usuário ou senha incorretos.')
