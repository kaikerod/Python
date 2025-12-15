nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

for i in nums:
    if i % 2 != 0:  # Verifica se é ímpar
        soma += i   # Adiciona à soma

print(f"A soma dos números ímpares é: {soma}")