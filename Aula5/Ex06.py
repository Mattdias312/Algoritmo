x = int(input("Digite o valor de x:"))
y = int(input("Digite o valor de y:"))
z = int(input("Digite o valor de z:"))

if (x < y+z) and (y < z+x) and (z < y+x):
    if z == y == x:
        triangulo = "Equilátero"
    elif z == y or z == x or x == y:
        triangulo = "Isósceles"
    else:
        triangulo = "Escaleno"
else:
    triangulo = "Não é um triângulo"

print(triangulo)
