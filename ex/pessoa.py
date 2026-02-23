class Pessoa:
  def __init__(self, nome, idade, profissao):
    self.nome = nome
    self.idade = idade
    self.profissao = profissao

  def __str__(self):
    return f'{self.nome} | {self.idade} | {self.profissao}'

  def aumentar_idade(self):
    self.idade += 1

pessoa1 = Pessoa('Kaike', 20, 'Dev')
print(pessoa1)
pessoa1.aumentar_idade()
print(pessoa1)