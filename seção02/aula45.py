#  Gerador de CPF - (A partir da minha solução do desafio anterior)

#  Meu gerador:


from random import randint
numero = str(randint(100000000, 999999999))

multi1 = list(range(10, 1, -1))
multi2 = list(range(11, 1, -1))

conta = 0
acumulador = 0
calculo = 0

novo_cpf = list(numero[0:9])

#  Cálculo para dígito 1:
for n, i in enumerate(novo_cpf):
    i = int(i)
    conta = i * multi1[n]
    acumulador = acumulador + conta
calculo = 11 - (acumulador % 11)

if calculo > 9:
    novo_cpf.insert(9, '0')
else:
    novo_cpf.insert(9, str(calculo))

#  Cálculo para dígito 2:
conta = 0
acumulador = 0
calculo = 0

for n, i in enumerate(novo_cpf):
    i = int(i)
    conta = i * multi2[n]
    acumulador = acumulador + conta
calculo = 11 - (acumulador % 11)

if calculo > 9:
    novo_cpf.insert(10, '0')
else:
    novo_cpf.insert(10, str(calculo))

print(''.join(novo_cpf))

################################################################################

# Gerador do curso:

'''
from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf = numero                   # 9 números aleatórios
reverso = 10                        # Contador reverso
total = 0                           # O total das multiplicações

# Loop do CPF
for index in range(19):
    if index > 8:                   # Primeiro índice vai de 0 a 9,
        index -= 9                  # São os 9 primeiros digitos do CPF

    total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

    reverso -= 1                    # Decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:                   # Se o digito for > que 9 o valor é 0
            d = 0
        total = 0                   # Zera o total
        novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

print(novo_cpf)
'''