# Classes abstratas
from seção04.aula105.classes import ContaPoupanca, ContaCorrente

# cp = ContaPoupanca(1111, 2222, 0)
# cp.depositar(10)
# cp.sacar(5)
# cp.sacar(5)
# cp.sacar(1)

print('############################')

cc = ContaCorrente(agencia=123456, conta=55555, saldo=0, limite=500)

cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)
