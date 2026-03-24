nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# append em arquivo com a função open (adiciona na ultima linha)
# se estiver usando 'w' ele vai sobrescrever o arquivo
with open("manipulando-dados/arquivo.txt", "a") as f:
  f.write(f"Nome: {nome}\n")
  f.write(f"Idade: {idade}\n")
