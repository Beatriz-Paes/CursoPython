"""O que são dataclasses? O módulo Dataclasses fornece um decorador e funções para
criar automaticamente métodos como __init__(), __repr__(), __eq__() (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito em PEP 557.
Adicionado na versão 3.7 do python.
Doc: http://docs.python.org/pt-br/3/library/dataclasses.html
"""

from dataclasses import dataclass
from dataclasses import field, asdict, astuple


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(f'Invalid type {type(self.nome).__name__} != str em {self}')

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


# p0 = Pessoa(54684, '5')
p1 = Pessoa('A', '5')
p2 = Pessoa('C', '3')
p3 = Pessoa('D', '4')
p4 = Pessoa('B', '2')

pessoas = [p1, p2, p3, p4]
print(sorted(pessoas))
print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome))

print(p1)
# print(p1 == p2)

# print(p1)
# print(p1.nome)
# print(p1.sobrenome)
# print(p1.nome_completo)

print(asdict(p1))
print(astuple(p1))
