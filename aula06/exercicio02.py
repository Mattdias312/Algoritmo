valor = int(input("Digite o valor:"))


if valor <= 1000:
        valor = valor * 0.1
elif valor <=5000:
    valor = valor * 0.2
else:
    valor = valor * 0.3

print(f"o desconto é de {valor}")