# Gerador de CNPJ a partir do código anterior

from seção03.aula90 import cnpj


cnpj1 = input('Digite um CNPJ: ')
if cnpj.valida(cnpj1):
    print(f'{cnpj1} é válido!')
else:
    print(f'{cnpj1} é inválido!')

for i in range(50):
    novo_cnpj = cnpj.gerador()
    formatado = cnpj.formata(novo_cnpj)
    print(formatado)
