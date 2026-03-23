class AluguelCarro:
  def __init__(self, nome_cliente, dias_alugados, modelo_carro):
    self.nome_cliente = nome_cliente
    self.dias_alugados = dias_alugados
    self.valor_diaria = 50
    self.modelo_carro = modelo_carro
    self.placas = []

  def alugar_carro(self, placa, carro, dias_alugados):
    self.placas.append(placa)
    print(f"O carro {carro} com a placa {placa} foi alugado por {self.nome_cliente} por {dias_alugados} dias")

  def devolver_carro(self, placa):
    self.placas.remove(placa)
    print(f"O carro com a placa {placa} foi devolvido")

  def calcular_valor_total(self, dias_alugados):
    return f"O valor total do aluguel é de R$ {dias_alugados * self.valor_diaria}"

  def listar_placas(self):
    for placa in self.placas:
      print(placa)

aluguel = AluguelCarro("Kaike", 3, "Gol")
aluguel.alugar_carro("ABC-1234", "Gol", 3)
print(aluguel.calcular_valor_total(3))