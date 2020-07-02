# Encapsulamento

"""
public, protected, private

Convenções:
    _ Private/Protect - Recomenda-se que não seja acessado
    __ Private - Recomenda-se fortemente que não acessado

"""


class BaseDeDados:
    def __init__(self):
        # self.dados = {} -> O Atributo principal da classe é público (pode ser acessado dentro e fora da classe)
        # self._dados = {}  # Utilizando um _ antes do atributo, recomenda-se que esse atributo não seja acessado.
        self.__dados = {}  # Utilizando dois _, recomenda-se fortemente que esse atributo não seja acessado.

    @property  # Utilizando decorador para obter um dado
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Beah')
bd.inserir_cliente(3, 'Ana')
# bd.lista_clientes()
# bd.dados = 'Uma outra coisa'  # Posso acessar o atributo de fora da classe, pois é público.
# Nesse caso, quebra tudo que foi construído.


bd.__dados = 'Uma outra coisa'
# print(bd._dados)  # Ainda com _, eu consigo acessar.
# print(bd.__dados)  # Renomeia utilizando o nome da classe

print(bd._BaseDeDados__dados)  # Valor real do atributo

print(bd.__dados)

# bd.dados = 'Outro valor' -> Exception - Não posso configurar esse atributo
