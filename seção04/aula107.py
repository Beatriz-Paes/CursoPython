# Criando exceções
class ExcecaoError(Exception):
    pass


def teste():
    raise ExcecaoError('Error!!!')


try:
    teste()
except ExcecaoError as error:
    print(f'Erro: {error}')
