while True:
    valor = input("Digite um número: ")

    if valor.isnumeric():
        break
    print("Digite apenas números: ")
valor_formatado = ''
n = len(valor)
for i in range(n-2,0,-3):
    if i == n-2:
        valor_formatado = valor_formatado + ',' + valor[n-2:n+1]

    if (i-3)>0:
        valor_formatado = '.' + valor[i-3:i] + valor_formatado

    else:
        valor_formatado = valor[0:i] + valor_formatado

print(valor_formatado)
