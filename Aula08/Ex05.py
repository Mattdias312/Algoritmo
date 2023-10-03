frase = input("Digite uma frase: ")
palavra = input("Digite a palavra: ")

qtd=frase.count(palavra)
total_palavra = frase.count(' ') + 1

print(f"A frase possui um total de {total_palavra} palavras")
print(f"A palavra {palavra} foi encontrada {qtd} vezes na frase")