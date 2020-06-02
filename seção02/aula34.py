"""
Listas
fatiamento
append, insert, pop, del, clear, extend, +
min, max

lista = [1,2,3,4, 'Bea', True, 10,6]
"""

#         0    1    2    3    4     5
lista = ['a', 'b', 'c', 'd', 'e', 10.5, 'Beatriz']
lista[6] = 'Luiz'
print(lista[-1])
print(lista)
print(lista[0:3])
print(lista[0:])
print(lista[::2])
print(lista[::-1])

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l3 = l1 + l2
print(l1, l2)
print('l1+l3', l3)

l1.extend(l2)
print('l1.extend(l2)', l1)

l2.extend('a')
print('l2.extend("a")', l2)

l2.append('b')
print('l2.append(''b'')', l2)

l3.insert(0, 'Beah')
print('l3.insert(0, "Beah")', l3)

l3.pop()
print('l3.pop()', l3)

del(l3[:1])
print('del', l3)

print('máximo', max(l1))
print('mínimo', min(l3))

############################################
l4 = list(range(0, 50, 4))
print('l4', l4)

soma = 0
for valor in l4:
    soma = soma + valor

print(soma)

############################################
l5 = [1, 2, 3, 'beah', True, 10.5, -9]
for elem in l5:
    print(f'O tipo de {elem} é {type(elem)}.')


#######################################################################################################
secreta = 'superensino'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra: ')
        continue

    digitadas.append(letra)

    if letra in secreta:
        print(f'Olha, temos a letra {letra} na palavra secreta!')
    else:
        print(f'Affs, a letra {letra} não existe na palavra secreta.')
        digitadas.pop()

    secreta_temp = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreta_temp += letra_secreta
        else:
            secreta_temp += '*'
    if secreta_temp == secreta:
        print(f'Parabéns!, você ganhou!!! A palavra secreta é {secreta}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreta_temp}')

    if letra not in secreta:
        chances -= 1
    print(f'Você ainda tem {chances} chance(s).')
    print()