# Funções - def

"""
def funcao(var):
    print('Isso será executado')
    return var
    print('Isso não será executado')  # Não é mais executado.

variavel = funcao('Valor que eu quero')

print(variavel)
"""
#################################################################3
'''
def divisao(n1, n2):

    if n2 > 0:
        return n1 / n2

divide = divisao(10, 0)

if divide:
    print(divide)
else:
    print('Conta inválida')
'''
def f(var):
    print(var)


def dumb():
    return f
print(type(f))

var = dumb()('E colocar o valor aqui')

###############################################

def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

divide = divisao(10, 0)

if divide:
    print(divide)
else:
    print('Conta inválida')

###############################################

def funcao():
    return 'Luiz', 'Otávio'
print(funcao())

var = funcao()
print(var, type(var))
print(var[0])