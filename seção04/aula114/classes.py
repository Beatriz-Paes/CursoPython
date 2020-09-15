from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta


class Conta(ABC):
    def __init__(self, agencia, num_conta, saldo):
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.ver_saldo()

    def ver_saldo(self):
        print(f'Agência: {self.agencia}\n'
              f'Conta: {self.num_conta}\n'
              f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente.')
            return
        self.saldo -= valor
        self.ver_saldo()


class ContaCorrente(Conta):
    def __init__(self, agencia, num_conta, saldo, limite=300):
        super().__init__(agencia, num_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente.')
            return
        self.saldo -= valor
        self.ver_saldo()


class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 5555]
        self.clientes = []
        self.contas = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agencia not in self.agencias:
            return False
        return True
