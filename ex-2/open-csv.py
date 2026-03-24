import csv

# Escrever arquivo csv
# newline='' evita que o arquivo fique com linhas em branco
with open("ex-2/arquivo.csv", "w", newline='') as f:
  escritor = csv.writer(f)
  escritor.writerow(['nome', 'idade']) # escreve uma linha
  escritor.writerow(['Kaike', '20'])

# Ler arquivo csv
with open("ex-2/arquivo.csv", "r", newline='') as f:
  leitor = csv.reader(f)
  for linha in leitor:
    print(linha)