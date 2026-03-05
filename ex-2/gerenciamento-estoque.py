class Produto:
  def __init__(self, nome, codigo, quantidade, preco):
    self.nome = nome
    self.codigo = codigo
    self.quantidade = quantidade
    self.preco = preco

class Estoque:
  def __init__(self):
    self.produtos = []

  def adicionar_produto(self, produto):
    self.produtos.append(produto)

  def remover_produto(self, produto):
    self.produtos.remove(produto)

  def buscar_produto(self, codigo):
    for produto in self.produtos:
      if produto.codigo == codigo:
        return produto
    return None

  def listar_produtos(self):
    for produto in self.produtos:
      print(produto)