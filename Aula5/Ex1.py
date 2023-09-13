num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f"O menor número é {num2}")
elif num1 == num2:
    print("Os números são iguais")
else:
    print(f"O menor número é {num1}")
