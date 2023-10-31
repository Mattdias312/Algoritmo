lista1 = []
lista2 = []
for i in range(5):
    j = int(input("Digite os valores do 1 conjunto: "))
    lista1.append(j)
s = set(lista1)

for i in range(5):
    k = int(input("Digite os valores do 2 conjunto: "))
    lista2.append(k)
r = set(lista2)

print(s.union(r))

