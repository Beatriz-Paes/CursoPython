# built-in úteis

# isnumeric, isdigit, isdecimal

num1 = (input('Digite um número: '))
num2 = (input('Digite outro número: '))

# print(num1.isnumeric())
# print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    soma = int(num1) + int(num2)
    print(f'A soma é {soma}')
else:
    print('Não pude converter os números para realizar a soma')
