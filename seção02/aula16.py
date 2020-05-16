# Introdução a formatação de strings

nome = 'Gabs'
idade = 25
altura = 1.50
peso_kg = 50
imc = peso_kg / (altura**2)

print(nome, 'tem', idade, 'anos e seu índice de massa corporal é:', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} de idade e seu imc é {:.2f}'.format(nome, idade, imc))
