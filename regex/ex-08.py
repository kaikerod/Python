import re

cpf = input('Digite o CPF para validação: ')

if re.search(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$', cpf):
    print('O CPF está no formato correto')
else:
    print('O CPF está no formato incorreto')