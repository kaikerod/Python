class Produto:
  def __init__(self, nome, codigo, quantidade, preco):
    self.nome = nome
    self.codigo = codigo
    self.quantidade = quantidade
    self.preco = preco

class Estoque:
  def __init__(self):
    self.produtos = []