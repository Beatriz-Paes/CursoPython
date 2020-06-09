# Dicionários

# d1 = {'chave1':'valor da chave'}
# print(d1)
#
# d1['nova_chave'] = 'valor da nova chave'
# print(d1)
# print(d1['chave1'])


# d1 = dict(chave1='valor da chave', chave2='valor da outra chave')
# d1['nova chave'] = 'valor da nova chave'
# print(d1)
# print(d1['chave2'])

d1 = {
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4): 'tupla',
}

print(d1[(1, 2, 3, 4)])
print(len(d1))
#del d1['str']
print(d1)

for k in d1:
    print(k)
for v in d1.values():
    print(v)

for i in d1.items():
    print(i)

for x, y in d1.items():
    print(x, y)


cliente = {
    'cliente1' : {
        'nome' : 'Beah',
        'sobrenome': 'Paes',
    },
    'cliente2' : {
        'nome' : 'Larissa',
        'sobrenome' : 'Almeida',
    }
}

for clientes_k, clientes_v in cliente.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

import copy
d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ['Bea', 'Luiz']}
v = copy.deepcopy(d1)

v['d'][1] = 'Paes'
#v = d1.copy()
#v[1] = 'Beatriz'

print(d1)
print(v)

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)
print(d1)

d1.pop('c3')
print(d1)