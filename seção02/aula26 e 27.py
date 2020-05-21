# Exercícios Propostos

################################### Exercício 01 ########################################
"""
Faça um programa que peça ao usuário para digitar um número inteiro.
Informe se esse número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro
"""

num = input('Digite um número inteiro: ')
if num.isnumeric():
    verif = int(num) % 2
    if verif == 0:
        print(f'{num} é um número inteiro par.')
    else:
        print(f'{num} é um número inteiro ímpar.')
else:
    print('Você não digitou um número inteiro.')


################################### Exercício 02 ########################################
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia: 0-11, Boa tarde: 12-17 e Boa noite: 18-23.
"""

horas = input('Digite o horário atual (0-23): ')

if horas.isnumeric():
    horas = int(horas)

    if 0 <= horas <= 11:
        print('Bom dia!')
    elif 12 <= horas <= 17:
        print('Boa tarde!')
    elif 18 <= horas <= 23:
        print('Boa noite!')
    else:
        print('Horário deve estar entre 0 e 23.')

else:
    print('Você não digitou um  horário válido.')


################################### Exercício 03 ########################################
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto"; Se tiver entre 5 e 6 letras. escreva
"Seu nome é normal"; Maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu primeiro nome: ')

if nome.isalpha():
    if len(nome) <= 4:
        print('Seu nome é curto.')
    elif 5 <= len(nome) <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')
else:
    print('Nome inválido.')
