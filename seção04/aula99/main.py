# Associação

from seção04.aula99.classes import Escritor
from seção04.aula99.classes import Caneta
from seção04.aula99.classes import MaquinaDeEscrever


escritor = Escritor('Beatriz')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor


print(caneta.marca)
maquina.escrever()