#  Desafio - Validar um CPF - Minha solução

"""
CPF = 662.749.742-53
-------------------------------------------------
6 * 10 = 60             #    6 * 11 = 66 <-
6 * 9 = 54              #    6 * 10 = 60
2 * 8 = 16              #    2 * 9 = 18
7 * 7 = 49              #    7 * 8 = 56
4 * 6 = 24              #    4 * 7 = 28
9 * 5 = 45              #    9 * 6 = 54
7 * 4 = 28              #    7 * 5 = 35
4 * 3 = 12              #    4 * 4 = 16
2 * 2 = 4               #    2 * 3 = 6
                        # -> 5 * 2 = 10
         294            #             349
11 - (294 % 11) = 5     #     11 - (349 % 11) = 3
5 < 9 = 5               #
Digito 1 = 5            #   Digito 2 = 3


"""
multi1 = list(range(10, 1, -1))
multi2 = list(range(11, 1, -1))

while True:
    conta = 0
    acumulador = 0
    calculo = 0
    cpf_ = (input('Digite seu CPF (Apenas números): '))

    if cpf_.isdigit() and len(cpf_) == 11:
        novo_cpf = list(cpf_[0:9])
    else:
        print('Inválido!')
        print()
        continue

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

    if list(cpf_) == novo_cpf:
        print('Válido!')
    else:
        print('Inválido!')
    print()
