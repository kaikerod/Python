cedulas_disponiveis = [100, 50, 20, 10, 5, 2]

try:
    valor_saque = int(input("Digite o valor do saque: "))
    if valor_saque < 0:
        raise ValueError("O valor do saque não pode ser negativo!")

    for cedula in cedulas_disponiveis:
        quantidade = valor_saque // cedula
        valor_saque %= cedula
        print(f"Quantidade de {cedula} cedulas: {quantidade}")
except ValueError:
    print("Digite um valor válido!")