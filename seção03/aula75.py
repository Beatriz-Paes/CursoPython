# Filter

from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
# nova_lista = [x for x in lista if x > 5]

print(list(nova_lista))

##################################################

# outra_lista = filter(lambda p: p['preço'] > 50, produtos)
#
# for produto in outra_lista:
#     print(produto)

# def filtra(produto):
#     if produto['preço'] > 50:
#         return True
#
#
# outra_lista = filter(filtra, produtos)
#
# for produto in outra_lista:
#     print(produto)


def filtra(pessoa):
    if 18 <= pessoa['idade'] <= 30:
        return True


outra_lista = filter(filtra, pessoas)

for p in outra_lista:
    print(p)
