# escrever arquivo com a função open
with open("ex-2/arquivo.txt", "w") as f:
  f.write("Hello World")

# ler arquivo com a função open
with open("ex-2/arquivo.txt", "r") as f:
  conteudo = f.read()
  print(conteudo)
