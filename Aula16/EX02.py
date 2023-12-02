lista_primo=[]
def primo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True

def qtd_primos(n):
    qtd = 0
    for i in range(1,n+1):
        if primo(i):
            lista_primo.append(i)
            qtd += 1
    return qtd

def soma_primo(qtd):
    total = 0
    for i in qtd[::]:
        total += i
    return total


print(primo(33))
print(qtd_primos(33))
print(lista_primo)
print(soma_primo(lista_primo))
