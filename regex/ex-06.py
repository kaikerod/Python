import re

texto = input('Digite o texto: ')

if re.search(r'\d{2}/\d{2}/\d{4}', texto):
    print('Data válida')
else:
    print('Data inválida')