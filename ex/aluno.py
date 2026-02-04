class Aluno:
  def __init__(self, nome):
    self.nome = nome
    self.notas = []

  def adicionar_nota(self, nota):
    self.notas.append(nota)


  def calcular_media(self, nota):
    pass