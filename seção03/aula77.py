# Try / Except - Tratando exceções

print('#' * 50)
try:                    # Tente esse código
    print(a)
except NameError as erro:       # Se aparecer uma exceção do tipo NameError passe pro próximo código
    print('Erro do desenvolvedor.')

print('O código continua')

##########################################################################################################

print('#' * 50)
try:
    a = []
    print(a[1])
except NameError as erro:       # Se aparecer uma exceção do tipo NameError passe pro próximo código
    print('Erro do desenvolvedor.')

except Exception as erro:       # Se ocorrer qualquer outro erro o qual não previ
    print('Ocorreu um erro inesperado.')

print('O código continua')

##########################################################################################################

print('#' * 50)
try:
    a = {}
    print(a[1])
except NameError as erro:       # Se aparecer uma exceção do tipo NameError passe pro próximo código
    print('Erro do desenvolvedor.')

except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')

except Exception as erro:       # Se ocorrer qualquer outro erro o qual não previ
    print('Ocorreu um erro inesperado.')

print('O código continua')

##########################################################################################################

print('#' * 50)
try:
    a = {}
    print(a)
except NameError as erro:       # Se aparecer uma exceção do tipo NameError passe pro próximo código
    print('Erro do desenvolvedor.')

else:   # Vai ser executado se não houve except
    print('Seu código foi executado com sucesso.')

finally:    # Vai ser executado sempre
    print('Finalmente...')
##########################################################################################################

print('#' * 50)
try:
    a = 1 / 0

except (NameError, ZeroDivisionError) as erro:       # Se aparecer uma exceção do tipo NameError passe pro próximo código
    print('Erro do desenvolvedor.')

else:   # Vai ser executado se não houve except
    pass

finally:    # Vai ser executado sempre
    a = None

print(a)
