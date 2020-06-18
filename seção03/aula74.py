# Map

from dados import pessoas, lista, produtos

# nova_lista = [x * 2 for x in lista]
nova_lista = map(lambda x: x * 2, lista)

print(lista)
print(list(nova_lista))

for produto in produtos:
    print(produto)

#####################################################


# def aumenta_preco(p):
#     p['preço'] = round(p['preço'] * 1.05, 2)    # Acréscimo de 5% no preço
#     return p
#
#
# novos_produtos = map(aumenta_preco, produtos)
#
# for produto in novos_produtos:
#     print(produto)

#####################################################

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)
