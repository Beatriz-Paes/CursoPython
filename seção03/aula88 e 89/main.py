from CursoPython.seção03.aula88 import cnpj


while True:
    cnpj1 = input('Digite um CNPJ: ')
    if cnpj.valida(cnpj1):
        print(f'{cnpj1} é válido!')
    else:
        print(f'{cnpj1} é inválido!')

