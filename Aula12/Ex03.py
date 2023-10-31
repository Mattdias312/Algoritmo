lista1 = []
lista2 = []
for i in range(5):
    j = int(input("Digite os valores do 1 conjunto: "))
    lista1.append(j)
s = set(lista1)

for i in range(5):
    lista2.append(int(input("Digite os valores do 2 conjunto: ")))
r = set(lista2)

print(s.union(r))

