def primo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True

def qtd_primos(n):
    qtd = 0
    for i in range(1,n+1):
        if primo(i):
            qtd += 1
    return qtd


valor = int(input("Digite um número: "))
print(qtd_primos(valor))
