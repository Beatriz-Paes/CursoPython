# Dictionary comprehension

l1 = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x: y.upper() for x, y in l1}
d2 = {f'chave_{x}': x**2 for x in range(5)}
print(d1)
print(d2)