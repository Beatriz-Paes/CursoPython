# Composição

from seção04.aula101.classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
cliente1.inserir_endereco('Manaus', 'AM')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Anne', 23)
cliente2.inserir_endereco('Manaus', 'AM')
cliente2.inserir_endereco('Salvador', 'BH')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('João', 19)
print(cliente3.nome)
cliente3.inserir_endereco('Rio de Janeiro', 'RJ')
cliente3.lista_enderecos()


print('#######################')