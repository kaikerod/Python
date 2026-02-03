class Restaurante:
  def __init__(self, nome, categoria, ativo):
    self.nome = nome
    self.categoria = categoria
    self.ativo = False

  def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'

restautante1 = Restaurante('Trash', 'Hamburgueria', True)
print(restautante1)