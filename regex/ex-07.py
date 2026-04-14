import re

nome = input('Digite o nome do cliente para validação: ')

if re.search(r'^[A-Z][a-z]+$', nome):
    print('Nome válido')
else:
    print('Nome inválido')