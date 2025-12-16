despesas = {
    'aluguel': 1200.00,
    'luz': 180.50,
    'internet': 99.90,
    'mercado': 650.00,
    'transporte': 220.00,
    'lazer': 350.00
}

salario = 3500.00

def exibir_despesas():
    for despesa, valor in despesas.items():
        print(f'{despesa}: R$ {valor:.2f}')

def maior_gasto():
    for despesa, valor in despesas.items():
        if valor >= 1000:
            print(f'\nO maior gasto foi {despesa} que custa {valor}')

exibir_despesas()
maior_gasto()

sobra = salario - sum(despesas.values())
print(f'\nSeu saldo é de {sobra:.2f}')