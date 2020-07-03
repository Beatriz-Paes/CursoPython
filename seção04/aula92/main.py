# POO - Classes

from seção04.aula92.pessoas import Pessoa

# p1.comer('maçã')
# p1.falar('POO')
# p1.parar_comer()
# p1.falar('POO')
# p1.comer('Uva')
# p1.parar_falar()
# p1.falar('Python')

p1 = Pessoa('Luiz', 20)
p2 = Pessoa('Anne', 32)

p1.falar('POO')
p2.falar('Filmes')  # Objetos independentes
p1.comer('Legumes')

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
