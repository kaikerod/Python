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

  def adicionar_venda(self, venda):
    self.lista_vendas.append(venda)

  def vendas_acima_de(self, valor_minimo):
    vendas_filtradas = [venda for venda in self.lista_vendas if venda.valor > valor_minimo]
    return vendas_filtradas

meu_sistema = AnaliseVendas()
v1 = Venda('Notebook', 2500.00, date.today())
v2 = Venda('Smartphone', 1500.00, date(2025, 12, 25))
v3 = Venda('Tablet', 1000.00, date(2025, 1, 1))
meu_sistema.adicionar_venda(v1)
meu_sistema.adicionar_venda(v2)
meu_sistema.adicionar_venda(v3)

for i in meu_sistema.lista_vendas:
  print(i)

print("\n")

vendas_2k = meu_sistema.vendas_acima_de(2000)
if vendas_2k:
  print("Acima de 2000:")
  print("-" * 60)
  for i in vendas_2k:
    print(i)
else:
  print("Nenhuma venda acima de R$ 2000.00")