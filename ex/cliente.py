class Cliente:
  def __init__(self, nome, idade, cpf, endereco):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf
    self.endereco = endereco

  def __str__(self):
    return f'{self.nome} | {self.idade} | {self.cpf} | {self.endereco}'

cliente1 = Cliente('Kaike', 20, 1234, 'Rua Bruxelas')
print(cliente1)