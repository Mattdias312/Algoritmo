dia = int(input("Entre com o número do dia: "))

match dia:
    case 1:
        nome = "Domeingo"
    case 2:
        nome = "Segunda-Feira"
    case 3:
        nome = "Terça-Feira"
    case 4:
        nome = "Quarta-Feira"
    case 5:
        nome = "Quinta-Feira"
    case 6:
        nome = "Sexta-Feira"
    case 7:
        nome = "Sábado"
    case _:
        nome = f"O valor {dia} é inválido"

print(nome)