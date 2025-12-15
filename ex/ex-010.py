# 1. Solicita a temperatura e a escala desejada
try:
    temp_original = float(input('Digite um valor para medir a temperatura: '))
except ValueError:
    print("Entrada inválida. Por favor, digite um número para a temperatura.")
    exit()

escala_original = input('Em qual escala a temperatura está (C/c para Celsius, F/f para Fahrenheit)? ').upper()

# 2. Executa a conversão
if escala_original == 'C':
    # Conversão de Celsius para Fahrenheit
    fahrenheit = (temp_original * 1.8) + 32
    print(f'{temp_original}°C é igual a {fahrenheit:.2f}°F')

elif escala_original == 'F':
    # Conversão de Fahrenheit para Celsius
    celsius = (temp_original - 32) / 1.8
    print(f'{temp_original}°F é igual a {celsius:.2f}°C')

else:
    # Caso a escala digitada não seja reconhecida
    print('Escala não reconhecida. Por favor, digite "C" ou "F".')