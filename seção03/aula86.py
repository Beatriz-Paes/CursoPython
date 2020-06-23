# Problemas dos parâmetros mutáveis em funções

# listas, dicionários - exemplos de objetos mutáveis
# tuplas, str's, números, booleanos, None - exemplos de objetos não mutáveis


def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes1 = ['Fabrício']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduarda'], lista_clientes1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Marcella'])
clientes3 = lista_de_clientes(['Anne', 'Túlio', 'Larissa'])

print(clientes1)
print(clientes2)
print(clientes3)
