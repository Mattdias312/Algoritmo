nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"{nome} tem {idade} anos!")

if idade >= 60:
    print("Você já pode pagar meia no cinema")
else:
    print("Você não tem direito a meia idoso")

print("Acabou o programa!")