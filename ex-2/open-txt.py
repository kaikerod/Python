# escrever arquivo com a função open
# open(caminho_do_arquivo/nome_do_arquivo, modo)
# modos: 'w' (write), 'r' (read)
with open("ex-2/arquivo.txt", "w") as f:
  f.write("Hello World\n")

# ler arquivo com a função open
with open("ex-2/arquivo.txt", "r") as f:
  conteudo = f.read()
  print(conteudo)

# append em arquivo com a função open (adiciona na ultima linha)
with open("ex-2/arquivo.txt", "a") as f:
  f.write("Ola mundo!")