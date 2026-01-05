import random
import string

numeros = string.digits
minusculas = string.ascii_lowercase
maiusculas = string.ascii_uppercase
simbolos = string.punctuation

senha = []

for i in range(3):
    senha.append(random.choice(numeros))
    senha.append(random.choice(minusculas))
    senha.append(random.choice(maiusculas))
    senha.append(random.choice(simbolos))

random.shuffle(senha) # Embaralha a senha

print(f'Sua senha segura é: {''.join(senha)}')