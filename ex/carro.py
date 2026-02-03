class Carro:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.caracteristicas = [marca, modelo, ano]
  
  # def exibir_carro(self):
  #   return f"{self.marca} {self.modelo} - Ano: {self.ano}"
  
  def exibir_carro(self):
    for i in self.caracteristicas:
      print(i)


carro1 = Carro('Audi', 'R8', 2010)
carro1.exibir_carro()