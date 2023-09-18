escolha = str(input("Digite um tipo lata, galão ou litro: "))
if escolha == "lata" or escolha == "galão" or escolha == "litro":
    largura = float(input("Digite a largura da parede: "))
    comprimento = float(input("Digite o comprimento da parede: "))


    area = (2*(largura * 2.80)) - (0.80 * 2.10)
    area = (area + (2*(comprimento * 2.80)))
    qtnd = area / 3

    if escolha == "lata":
        qtnd_lata = qtnd / 18
        print(f"Você vai precisar de {qtnd_lata:5.1f} latas")
    elif escolha == "galão":
        qtnd_galao = qtnd / 3.6
        print(f"Você vai precisar de {qtnd_galao:5.1f} galões")
    elif escolha == "litro":
        print(f"Você vai precisar de {qtnd:5.1f} litros")
else:
    print("Tipo escolhido errado. Tem que ser lata, galão ou litro")
