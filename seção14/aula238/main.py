# Doctests

from seção14.aula237.calculadora import soma

# print(soma(10, 20))
# print(soma(-10, 20))
# print(soma(10.5, 20.10))


try:
    print(soma(15, '10'))
except AssertionError as e:
    print(f'Conta inválida: {e}.')
