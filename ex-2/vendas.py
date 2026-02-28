from datetime import date

class Venda:
  def __init__(self, produto, valor, data_venda):
    self.produto = produto
    self.valor = valor
    self.data_venda = data_venda

  def __str__(self):
    return f"Produto: {self.produto:<15} | Valor: R$ {self.valor:<7.2f} | Data: {self.data_venda.strftime('%d/%m/%Y')}"

class AnaliseVendas:
  def __init__(self):
    self.lista_vendas = []