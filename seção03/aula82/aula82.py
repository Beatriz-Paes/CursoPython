# Pacotes e módulos em Python

from seção03.aula82.vendas.preco import aumento, reducao
import seção03.aula82.vendas.formata.preco as preco2

preco = 49.90
preco_com_aumento = aumento(preco, 15, formata=True)
print(preco_com_aumento)

##########################################################################

valor = 49.90
preco_com_reducao = reducao(valor, 15, formata=True)
print(preco_com_reducao)

print(preco2.real(50))
