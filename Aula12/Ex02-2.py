d = {}
maior=0
sobrenomeVelho=''
for i in range(5):
    sobrenome = input("Digite o sobrenome: ")
    idade = int(input("Digite a idade: "))
    d[sobrenome] = idade

idades = list(d.values())
mediaIdades = sum(idades) / len(idades)
print(f"A média de idade é {mediaIdades}")

for chave, valor in d.items():
    if(valor > mediaIdades):
        print(f"As pessoas com idade acima da média são {chave}")
