def primo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True


n = int(input("Digite um numero primo: "))
print(primo(n))
