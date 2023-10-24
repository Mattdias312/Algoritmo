lista = []
tupla = ()
i = 0
while i < 10:
    x = int(input("Digite um número: "))
    lista.append(x)
    i += 1

tupla = tuple(lista)

print(tupla[::-1])
