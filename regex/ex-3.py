import re

palavra = input('Digite a palavra chave: ')

primeiras_letras = str(palavra[:3])
ultimas_letras = str(palavra[-3:])

print(f'As primeiras letras são: {primeiras_letras}')
print(f'As ultimas letras são: {ultimas_letras}')