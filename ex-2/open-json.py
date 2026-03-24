import json

# dados em formato de dicionário
dados = {'nome':'Ana', 'idade':20, 'enderecos':['a', 'b']}

# Escrever arquivo json
with open("ex-2/arquivo.json", "w") as f:
  json.dump(dados, f)

# Ler arquivo json
with open("ex-2/arquivo.json", "r") as f:
  dados_lidos = json.load(f)
  print(dados_lidos)