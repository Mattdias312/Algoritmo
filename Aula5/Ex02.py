nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota_exame = 0

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Parabéns você foi aprovado, sua média foi {media:5.2f}")
elif media >= 3:
    nota_exame = 12 - media
    print(f"Você terá que fazer o exame, sua média foi {media:5.2f}")
else:
    print(f"Você foi reprovado, sua média foi {media:5.2f}")

if nota_exame != 0:
    print(f"Tem que tirar no minimo {nota_exame:5.2f}")
