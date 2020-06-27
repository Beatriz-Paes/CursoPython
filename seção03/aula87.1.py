# Exercício - Undo e Redo - Minha solução
"""
Faça uma lista de tarefas com as seguintes opções:
    Adicionar tarefa
    listar tarefas
    Opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    Opção de refazer (a cada vez que chamarmos, refaz a última ação)

    ['tarefa 1', 'tarefa 2']
    ['tarefa 1] <- Desfazer
    ['tarefa 1', 'tarefa 2'] <- Refazer

"""

lista = []
recuperar = []


def adicionar():
    while True:
        tarefa = input('\nPara voltar ao menu inicial digite 0.'
                       '\n\tAdicione uma tarefa: ')
        if tarefa == '0':
            menu()
        lista.append(tarefa)


def listar():
    if lista:
        print('\nEssa é sua lista de tarefas:')
        for tarefa in lista:
            print(f'\t{tarefa}')
    else:
        print('\nSua lista de tarefas está vazia.')
    menu()


def desfazer():
    try:
        recuperar.append(lista[-1])
        del(lista[-1])
    except IndexError:
        print('\nSua lista de tarefas está vazia.')
    menu()


def refazer():
    try:
        lista.append(recuperar[-1])
        del(recuperar[-1])
    except IndexError:
        print('\nNão há nada para refazer.')
    menu()


def menu():
    opcao = input('\nO que deseja fazer?'
                  '\n\t1. Adicionar tarefa'
                  '\n\t2. Listar tarefas'
                  '\n\t3. Desfazer'
                  '\n\t4. Refazer'
                  '\n\t5. Sair'
                  '\n\n\tDigite um número de acordo com a opção desejada: ')

    if opcao.isdigit() and 1 <= int(opcao) <= 5:

        if opcao == '1':
            adicionar()

        elif opcao == '2':
            print(listar())

        elif opcao == '3':
            desfazer()

        elif opcao == '4':
            refazer()

        else:
            exit()

    else:
        print('\n\tVocê não digitou uma opção válida!')


menu()
