from random import randint
lista = []

for i in range(0, 6000):
    lista.append(randint(1, 6))

lado1 = lista.count(1)
lado2 = lista.count(2)
lado3 = lista.count(3)
lado4 = lista.count(4)
lado5 = lista.count(5)
lado6 = lista.count(6)

print(f"Após 6000 jogadas sairam {lado1} o lado 1")
print(f"Após 6000 jogadas sairam {lado2} o lado 2")
print(f"Após 6000 jogadas sairam {lado3} o lado 3")
print(f"Após 6000 jogadas sairam {lado4} o lado 4")
print(f"Após 6000 jogadas sairam {lado5} o lado 5")
print(f"Após 6000 jogadas sairam {lado6} o lado 6")
