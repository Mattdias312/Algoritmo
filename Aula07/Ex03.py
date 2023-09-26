n = int(input("Digite um número: "))
primo = 0
for i in range(1, n+1):
    if n % i == 0:
        primo += 1

if primo == 2:
    print(f"o número {n} é primo")
else:
    print(f"O número {n} não é primo")
