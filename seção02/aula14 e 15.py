# Variáveis

"""
Deve iniciar com letra, pode conter números, separar_, letras maiusculas
"""

nome = 'Gabs'
idade = 25
altura = 1.50
e_maior = idade > 18
peso_kg = 50
imc = peso_kg / (altura**2)
print('Nome:', nome, type(nome))
print('Idade:', idade, type(idade))
print('Altura:', altura, type(altura))
print("Maior de 18?", e_maior, type(e_maior))
print(nome, 'tem', idade, 'anos e seu índice de massa corporal é:', imc)
