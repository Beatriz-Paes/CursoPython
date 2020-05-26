# Índices e fatiamento de strings

"""
Manipulando strings
* Strings índices
* Fatiamento de strings (inicio:fim:passo)
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""

# positivos [012345678]
texto = 'Python s2'
# negativos -[987654321]

print(texto[2])
print(texto[8])
url = 'www.google.com.br/'
print(url[:-1])

nova_string = texto[2:6]
print(nova_string)
print(texto[:6])
print(texto[7:])
print(texto[0:6:2])
print(len(texto))
