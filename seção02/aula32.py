"""
Iterando strings com while
"""
############################################################
'''
minha_string = 'o rato roeu a roupa do rei de Roma.'
tamanho = len(minha_string)

c = 0

nova_string = ''

while c < tamanho:
    if minha_string[c] == 'r':
        nova_string = nova_string + minha_string[c].upper()
    else:
        nova_string += minha_string[c]

    c += 1

print(nova_string)
'''
while True:
    minha_string = input('Digite uma frase: ')
    tamanho = len(minha_string)

    c = 0
    contagem_atual = 0
    letra = ''
    while c < tamanho:
        qtd_vezes_letra = minha_string.count(minha_string[c])

        if contagem_atual < qtd_vezes_letra and minha_string[c].strip():
            letra = minha_string[c]
            contagem_atual = qtd_vezes_letra

    #    print(minha_string[c], conta)

        c += 1

    print(letra, contagem_atual)
