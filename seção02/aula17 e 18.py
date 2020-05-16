# Desafio

"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual
* Obter o ano de nascimento baseado na idade e ano atual
* Obter o imc com duas casas decimais
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Marcella'
idade = 24
altura = 1.65
peso_kg = 70
ano_atual = 2020
ano_nasc = ano_atual - idade
imc = peso_kg / (altura ** 2)
print(f'{nome} tem {idade} anos, nasceu em {ano_nasc},'
      f' tem {altura} de altura, pesa {peso_kg} kg e seu IMC é {imc:.2f}.')
