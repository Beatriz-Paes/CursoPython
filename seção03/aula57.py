# Sistema de perguntas e respostas com dicionários

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 ao quadrado?',
        'respostas': {
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
        },
        'resposta_certa': 'd',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5 ao quadrado?',
        'respostas': {
            'a': '5',
            'b': '25',
            'c': '225',
            'd': '255',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 2 ao cubo?',
        'respostas': {
            'a': '2',
            'b': '4',
            'c': '6',
            'd': '8',
        },
        'resposta_certa': 'd',
    },
}
print()

respostas_certas = 0

for cp, vp in perguntas.items():
    print(f'{cp}: {vp["pergunta"]}')
    for cr, vr in vp['respostas'].items():
        print(f'[{cr}]: {vr}')
    resp_usuario = input('Escolha uma das opções acima (a/b/c/d): ')

    if resp_usuario == vp['resposta_certa']:
        print('Parabéns! você acertou :)')
        respostas_certas += 1
    else:
        print('Poxa, você errou!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} questões.')
print(f'Sua porcentagem de acertos foi de {porcentagem_acerto:.2f}%.')
