# Datetime #2
from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays


setlocale(LC_ALL, '')   # Usa o idioma padrão configurado no sistema
setlocale(LC_ALL, 'pt_BR.utf-8')    # Especificando o idioma

# Domingo, 04 de Outubro de 2020

dt = datetime.now()

formatacao1 = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1)  # Date in English, sem usar o setlocale
print(formatacao2)

mes_atual = int(dt.strftime('%m'))

print(mes_atual, mdays[mes_atual])
