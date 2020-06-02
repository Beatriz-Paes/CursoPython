#  Expressão condicional com operador OR

nome = input('Qual o seu nome? ')

#  if nome:
#      print(nome)
#  else:
#      print('Você não digitou nada.')

print(nome or 'Você não digitou nada.')

a = 0
b = None
c = False
d = []
e = {}
f = 25
g = 'Beah'

variavel = a or b or c or d or e or f or g
print(variavel)