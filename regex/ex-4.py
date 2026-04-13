import re

url = input('Digite a url para validar: ')

if re.search(r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$', url):
    print('Url válida')
else:
    print('Url inválida')