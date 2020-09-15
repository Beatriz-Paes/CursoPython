# Desafio POO

"""
Exercicio com abstração, herança, encapsulamento e polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco. A ideia é que o cliente tenha uma
conta (poupança ou corrente) e que possa sacar/depositar nessa conta. Contas correntes tem um limite extra.
Banco tem clientes e contas.

Dicas:

Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)

Criar classes ContaPoupanca e ContaCorrente que herda de conta
    ContaCorrente deve ter um limite extra
    Contas tem agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e polimorfismo - As subclasses
    que implementam o método sacar)

Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)

Banco será responsável por autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco

Só será possível sacar se passar na autenticação do banco (descrita acima)
"""

from seção04.aula114.classes import Banco, Cliente, ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Beah', 25)
cliente2 = Cliente('Anne', 30)
cliente3 = Cliente('Marcella', 40)

conta1 = ContaPoupanca(1111, 123456, 0)
conta2 = ContaCorrente(5555, 123456, 0)
conta3 = ContaPoupanca(1234, 123457, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(50)
    cliente1.conta.sacar(20)
else:
    print(f'Cliente: {cliente1.nome} - não autenticado.')

print('#####################################')

if banco.autenticar(cliente2):
    # cliente2.conta.depositar(50)
    cliente2.conta.sacar(150)
else:
    print(f'Cliente: {cliente2.nome} - não autenticado.')
