def contador(frase):
    palavras = frase.split()
    print(palavras)
    return len(palavras)

frase = input("Digite uma frase: ")
print(contador(frase))