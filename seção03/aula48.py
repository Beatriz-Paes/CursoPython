# Exercícios propostos - Minha solução

############################################Exercício 01###################################################
"""
1. Crie uma função que exibe uma saudação com os parâmetros saudação e nome
"""

print('Exercício 01:')
from datetime import datetime
hora = datetime.today()

def boasvindas(saudacao, nome):

    if not nome.isalpha():
        print('Nome inválido.')

    elif 00 <= hora.hour < 12:
        saudacao = 'Bom Dia'

    elif 12 <= hora.hour < 18:
        saudacao = 'Boa Tarde'
    else:
        saudacao = 'Boa noite'

    return f'{saudacao}, {nome}!'

print(boasvindas(saudacao='Olá', nome=input('Qual o seu nome? ')))

############################################Exercício 02###################################################

"""
Crie uma função que recebe 3 números como parâmetros e exiba
a soma entre eles
"""

print()
print('Exercício 02:')

def soma(a, b, c):

    if a.isdigit() and b.isdigit() and c.isdigit():
        return int(a)+ int(b) + int(c)

    else:
        return 'ERROR'

print(soma(a=input('a: '), b=input('b: '), c=input('c: ')))

############################################Exercício 03###################################################

"""
Crie uma função que receba 2 números. O primeiro é um valor e o segundo
é um percentual (ex: 10%). Retorne o valor do primeiro somado ao aumento do percentual do mesmo.
"""

print()
print('Exercício 03:')

def funcao(a, b):
    if a.isdigit and b.isdigit:
        a, b = int(a), int(b)
        return a + (b/100) * a
    else:
        return 'ERROR'
print(funcao(a=input('a: '), b=input('b: ')))

############################################Exercício 04###################################################

"""
Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne FIZZ,
se o parâmetro da função for divisível por 5, retorne Buzz. Se o parâmetro da função for divisível
por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
"""

print()
print('Exercício 04:')

def fizzbuzz(numero):
    if not numero.isdigit:
        return 'ERROR'
    else:
        numero = int(numero)
        if numero % 2 == 0:
            return 'Fizz'
        elif numero % 5 == 0 and not numero % 3 == 0:
            return 'Buzz'
        elif numero % 5 == 0 and numero % 3 == 0:
            return 'FizzBuzz'
        else:
            return numero
print(fizzbuzz(numero=input('Número: ')))