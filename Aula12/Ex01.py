d = {}
maior=0
sobrenomeVelho=''
for i in range(5):
    sobrenome = input("Digite o sobrenome: ")
    idade = int(input("Digite a idade: "))
    d[sobrenome] = idade
for chave, valor in d.items():
    if(valor > maior):
        maior = valor
        sobrenomeVelho = chave
print(f"A pessoa mais velha é {sobrenomeVelho}")
