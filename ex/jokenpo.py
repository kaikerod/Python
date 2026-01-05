import random
escolha_do_usuario = input("Escolha entre pedra, papel ou tesoura: ")

if escolha_do_usuario == "pedra":
    escolha_do_computador = random.choice(["pedra", "papel", "tesoura"])
    if escolha_do_computador == "pedra":
        print("Empate!")
    elif escolha_do_computador == "papel":
        print("Você perdeu!")
    else:
        print("Você ganhou!")
elif escolha_do_usuario == "papel":
    escolha_do_computador = random.choice(["pedra", "papel", "tesoura"])
    if escolha_do_computador == "papel":
        print("Empate!")
    elif escolha_do_computador == "tesoura":
        print("Você perdeu!")