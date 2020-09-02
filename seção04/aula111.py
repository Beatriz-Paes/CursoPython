# Metaclasses

"""
Em python tudo é um objeto: incluindo classes.
Metaclasses  são as "classes" que criam classes.
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'b_fala' not in namespace:
            print(f'Crie o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, não atributo em {name}.')
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    teste = 'valor'

    def b_fala(self):
        print('OI')

    def sei_la(self):
        pass


b = B()

# Usando type para criar classes
A = type(
    'A',
    (),
    {'attr': 'Olá Mundo!'}
)

a = A()
print(a.attr)
print(type(A))
