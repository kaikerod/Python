class Pessoa:
  def __init__(self, nome, idade, peso, altura):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura

pessoa1 = Pessoa('Kaike', '20', '80.2', '1,83')
print(pessoa1.nome)