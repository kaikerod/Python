def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

a = int(input("Digite o primeiro número: "))
operacao = input("Digite a operação: (+, -, *, /): ")
b = int(input("Digite o segundo número: "))

try:
    if operacao == "+":
        print(somar(a, b))
    elif operacao == "-":
        print(subtrair(a, b))
    elif operacao == "*":
        print(multiplicar(a, b))
    elif operacao == "/":
        print(dividir(a, b))
    else:
        print("Operação inválida!")
except ValueError:
    print("Erro: Digite apenas números válidos!")