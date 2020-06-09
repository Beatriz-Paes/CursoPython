# Sets
# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference (elementos apenas no set da esquerda)
# symmetric_difference ^ elementos que estão nos dois sets, mas não em ambos.

s1 = {1, 2, 3, 4, 5}    # conjunto 1
s2 = {6, 7, 8, 9}       # conjunto 2
s3 = set()              # conjunto vazio
s3.add(0)               # adiciona elementos no conjunto
s4 = s3.union(s1, s2)   # união de conjuntos
s5 = s1 | s2            # união de conjuntos
 

print(s1)
print(s4)
print(s5)

for v in s1:
    print(v)

print(s1.union(s2).union(s3))

lista = [1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 'beah', 'beah']  # lista
print(lista)
lista = set(lista)      # cast de lista para conjunto - elimina itens repetidos
print(lista)
lista = list(lista)     # cast de conjunto para lista
print(lista)

