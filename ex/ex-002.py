idade = int(input('Digite sua idade e determinarei se você é criança, adolescente ou adulto: '))

if idade <= 12:
    print('Você é uma criança!')
elif idade < 18:
    print('Você é um adolescente!')
elif idade > 18:
    print('Você já é adulto!')