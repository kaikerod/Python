import random

num_secreto = random.randint(1, 100)
tentativas = 0

num_escolhido = int(input("Digite um número entre 1 e 100: "))

while num_escolhido != num_secreto:
    tentativas += 1
    if num_escolhido < num_secreto:
        print("Muito baixo! Tente novamente.")
    else:
        print("Muito alto! Tente novamente.")
    num_escolhido = int(input("Digite um número entre 1 e 100: "))

print(f"Você acertou o número em {tentativas} tentativas.")