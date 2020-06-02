#  Desafio de contadores
"""
for / while
* Criar dois contadores, um que conte de maneira progressiva e o outro de maneira regressiva
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
#  Minha solução:
print('Minha solução:')

cont1 = list(range(0, 9))

c1 = 0
c2 = 10
while c1 in cont1:
    print(c1, c2)
    c1 += 1
    c2 -= 1
print('')

#  Solução do curso:
print('Solução do curso: ')

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
