d = {}
maiorMedia = {}
sobrenomeVelho=''
idadeTotal=0
media = 0
for i in range(5):
    sobrenome = input("Digite o sobrenome: ")
    idade = int(input("Digite a idade: "))
    d[sobrenome] = idade
    idadeTotal += idade
media = idadeTotal / 5
for chave, valor in d.items():
    if(valor > media):
        maiorMedia[chave] = valor

print(f"As pessoas com idade acima da média são {maiorMedia.keys()}")
