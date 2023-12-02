def soma(n):
    total_soma = 0
    qtd = len(n)
    for i in range(0, qtd):
        total_soma += int(n[i])
    return total_soma

def multiplica(n):
    total_multi = 1
    qtd = len(n)
    for i in range(0, qtd):
        total_multi *= int(n[i])
    return total_multi

n = '3011392323014'
print(multiplica(n))
print(soma(n))
