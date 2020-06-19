# Levantamento de exceções (raise)


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as erro:
        print(f'Erro: {erro}, Não se divide por zero.')
        raise   # Relançar uma exceção


try:
    print(divide(2, 0))
except:
    print('erro')

print('#'*50)

def divisao(num1, num2):
    if num2 == 0:
        raise ValueError("num2 não pode ser zero.")

    return num1 / num2

try:
    print(divisao(2, 0))
except ValueError as erro:
    print('Você está tentando dividir por zero.')
    print('Log: ', erro)
