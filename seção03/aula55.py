# Tuplas

t1 = (1, 2, 3, 'Beah', 10.1) * 3
t2 = 4, 5, 6, 'Paes'
t3 = t1 + t2
t1 = list(t1)


n1, n2, n3, n4, *_ = t3

for valor in t1:
    print(valor)

    print(t1)
    print(t3)
    print(n4)