import csv

# Escrever arquivo csv
# newline='' evita que o arquivo fique com linhas em branco
with open("manipulando-dados/arquivo.csv", "w", newline='') as f:
  escritor = csv.writer(f)
  escritor.writerow(['nome', 'idade']) # escreve uma linha
  escritor.writerow(['Kaike', '20'])

# Ler arquivo csv
with open("manipulando-dados/arquivo.csv", "r", newline='') as f:
  leitor = csv.reader(f)
  for linha in leitor:
    print(linha)