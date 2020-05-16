# Operadores aritméticos

"""
+, -, /, //, **, %, ()

"""

print('Adição', 10 + 10)
print('Subtração', 10 - 5)
print('Divisão real', 10 / 5)
print('Divisão inteira', 10 // 3)
print('Multiplicação', 10 * 10)
print('Potenciação', 10 ** 3)
print('Resto da divisão ou módulo', 10 % 3)
print('Precedência', ((10 ** 2) + (2 * 3)) / 3)

"""
Abaixo segue uma lista mais precisa de quais operadores
tem maior prioridade na hora de realizar contas mais
complexas (de maior para menor precedência).
"""

# ( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

# ** - Depois vem a exponenciação

# * / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

# +  - - Por fim, soma e subtração

# Contas com operadores de mesma precedência são realizadas da esquerda para a direita.