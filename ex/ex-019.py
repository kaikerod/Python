def somar(a, b):
    return a + b

try:
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    resultado = somar(numero1, numero2)
    print(f'A soma de {numero1} e {numero2} é {resultado}')

except ValueError:
    print('Erro: Digite apenas números válidos!')