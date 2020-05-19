# len - quantidade de caracteres

"""
usuario = input('Digite seu usuário: ')
qnt_caract = len(usuario)

#print(usuario, qnt_caract, type(qnt_caract))

#########################################################

if qnt_caract < 6:
    print('Você precisa digitar pelo menos 6 caracteres.')
else:
    print(f'Olá {usuario}, você foi cadastrado no sistema.')
"""

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foi: {len(string1 + string2)}.')
