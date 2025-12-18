def calcular_gorjeta(valor_da_conta, gorjeta):
    return valor_da_conta * (gorjeta / 100)

valor_da_conta = float(input("Digite o valor da conta: "))
gorjeta = float(input("Digite a porcentagem de gorjeta: "))
print(f'\nValor da conta: R$ {valor_da_conta:.2f}\nGorjeta: R$ {calcular_gorjeta(valor_da_conta, gorjeta):.2f}')