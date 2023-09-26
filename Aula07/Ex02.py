p_medio = 0
a_media = 0
imc_maior = 0
imc_menor = 0
for i in range(1, 6):
    a = float(input("Digite sua altura: "))
    p = float(input("Digite seu peso: "))
    imc = p/(a*a)
    if imc > imc_maior:
        imc_maior = imc
    if imc < imc_menor:
        imc_menor = imc
    if imc_menor == 0:
        imc_menor = imc
    a_media = a_media + a
    p_medio = p_medio + p

a_media = a_media/5
p_medio = p_medio/5
print(f"O peso médio é {p_medio:5.2f} a altura média é {a_media:5.2f}, o menor imc é {imc_menor:5.2f} e o maior imc é {imc_maior:5.2f}")
