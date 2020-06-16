# Exercício proposto - Minha solução

"""
Somar os valores dos produtos de um carrinho de compras em um e-commerce

carrinho = []

carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 20))
carrinho.append(('Produto3', 50))

usar list comprehension

"""


carrinho = []

carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 20))
carrinho.append(('Produto3', 50))
carrinho.append(('Produto4', 0.35))
carrinho.append(('Produto5', 38))
carrinho.append(('Produto6', 2))

total = [total[1] for total in carrinho]

print(sum(total))
