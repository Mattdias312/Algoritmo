e = 0
n = int(input("Digite o valor de n: "))
for i in range(1, n+1):
    e = e + (2 ** i)

print(f"A soma é {e}")
