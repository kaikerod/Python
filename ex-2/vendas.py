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

  def total_vendas_periodo(self, data_inicio, data_fim):
    total = sum(venda.valor for venda in self.lista_vendas if data_inicio <= venda.data_venda <= data_fim)
    return total

  def produto_mais_vendido(self):
    if not self.lista_vendas:
      return None
    
    contagem_produtos = {}
    for venda in self.lista_vendas:
      nome_produto = venda.produto
      if nome_produto in contagem_produtos:
        contagem_produtos[nome_produto] += 1
      else:
        contagem_produtos[nome_produto] = 1
    
    produto_mais_vendido = max(contagem_produtos, key=contagem_produtos.get)
    return produto_mais_vendido

  def produto_mais_lucrativo(self):
    if not self.lista_vendas:
      return None
    
    lucro_produtos = {}
    for venda in self.lista_vendas:
      nome_produto = venda.produto
      if nome_produto in lucro_produtos:
        lucro_produtos[nome_produto] += venda.valor
      else:
        lucro_produtos[nome_produto] = venda.valor
    
    produto_mais_lucrativo = max(lucro_produtos, key=lucro_produtos.get)
    return produto_mais_lucrativo

  def media_vendas_por_dia(self):
    if not self.lista_vendas:
      return None
    
    vendas_por_dia = {}
    for venda in self.lista_vendas:
      data = venda.data_venda
      if data in vendas_por_dia:
        vendas_por_dia[data] += venda.valor
      else:
        vendas_por_dia[data] = venda.valor
    
    media_vendas_por_dia = sum(vendas_por_dia.values()) / len(vendas_por_dia)
    return media_vendas_por_dia

meu_sistema = AnaliseVendas()
v1 = Venda('Notebook', 2500.00, date.today())
v2 = Venda('Smartphone', 1500.00,   date(2025, 12, 25))
v3 = Venda('Tablet', 1000.00, date(2025, 1, 1))
v4 = Venda('Notebook', 2500.00, date.today())
meu_sistema.adicionar_venda(v1)
meu_sistema.adicionar_venda(v2)
meu_sistema.adicionar_venda(v3)
meu_sistema.adicionar_venda(v4)

print(f"Total de vendas no período: R$ {meu_sistema.total_vendas_periodo(date(2025, 1, 1), date(2025, 12, 31)):.2f}")

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

print(f"\nProduto mais vendido: {meu_sistema.produto_mais_vendido()}")