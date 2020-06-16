# Exercício proposto - Solução do curso

carrinho = []

carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 20))
carrinho.append(('Produto3', 50))
carrinho.append(('Produto4', 0.35))
carrinho.append(('Produto5', 38))
carrinho.append(('Produto6', 2))

total = sum([y for x, y in carrinho])
print(total)
