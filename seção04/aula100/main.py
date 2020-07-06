# Agregação

from seção04.aula100.classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('Bermuda', 30)
p3 = Produto('Casaco', 99)
p4 = Produto('Caneca', 35.99)
p5 = Produto('Boné', 25.60)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p4)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p5)

carrinho.lista_produtos()
print(round(carrinho.soma_total()))