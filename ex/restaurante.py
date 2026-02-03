class Restaurante:
  def __init__(self, nome, categoria, ativo):
    self.nome = nome
    self.categoria = categoria
    self.ativo = ativo

restautante1 = Restaurante('Trash', 'Hamburgueria', 'Ativo')
print(restautante1.categoria)