soma = 0
qtd = int(input("Quantas idades você quer digitar? "))
for i in range(1, qtd+1):
    n = int(input(f"Entre com o {i}° idade: "))
    soma = soma + n
media = soma / qtd

print(f"A média é {media:5.2f}")
