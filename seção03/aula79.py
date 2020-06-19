# Uso de Try e Except como condicional


# numero = float(input('Digite um número: '))  # Para resolver o problema de operar com str, fiz um cast para float
# print(numero * 5)                            # Mas, e se o usuário digitar "dois"?

# Vamos então criar uma função para tentar resolver:


def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:

    numero = converte_numero(input('Digite um número: '))
    if numero is not None:
        print(numero * 10)
    else:
        print('Isso não é número.')
