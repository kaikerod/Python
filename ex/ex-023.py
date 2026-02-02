import math

class Retangulo:
  def __init__(self, largura, altura):
    self.largura = largura
    self.altura = altura

  def calcular_perimetro(self):
    return 2 * (self.largura + self.altura)

  def calcular_area(self):
    return self.largura * self.altura

  def calcular_diagonal(self):
    return math.sqrt(self.largura ** 2 + self.altura ** 2)

retangulo1 = Retangulo(10, 20)
print(retangulo1.calcular_perimetro())
print(retangulo1.calcular_area())
print(retangulo1.calcular_diagonal())