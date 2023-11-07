hifen1 = int(input("Digite quantos hifens serão colocados na 1° linha: "))
hifen2 = int(input("Digite quantos hifens serão colocados na 2° linha: "))


def desenha(qtd=10):
    for _ in range(0, qtd):
        print("-", end='')
    print()


desenha(hifen1)
print("** usando funções **")
desenha(hifen2)
