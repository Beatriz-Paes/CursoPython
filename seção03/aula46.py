# Funções - def

print('Hello!')  # Função
print('Hello!')  # Função

def saudacao(msg='Bom Dia,', nome='Posso ajudar?'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)

saudacao('Olá,', 'Super Aluno')
saudacao('Oi', 'Beah')
saudacao()
saudacao(nome='Boa Tarde,', msg='Posso ajudar?')
