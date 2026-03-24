nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

with open("manipulando-dados/arquivo.txt", "w") as f:
  f.write(f"Nome: {nome}\n")
  f.write(f"Idade: {idade}\n")
