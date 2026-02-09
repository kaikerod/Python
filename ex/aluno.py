class Aluno:
  def __init__(self, nome):
    self.nome = nome
    self.notas = []

  def adicionar_nota(self, nota):
    self.notas.append(nota)


  def calcular_media(self):
    media = sum(self.notas) / len(self.notas)
    if media <= 7:
      return 'Você não atingiu a média!'
    else:
      return 'Parabéns, você atingiu a média!'

  def listar_notas(self):
    for nota in self.notas:
      print(nota)


aluno1 = Aluno('Kaike')
aluno1.adicionar_nota(7)
aluno1.adicionar_nota(8)
print(aluno1.calcular_media())
print(aluno1.listar_notas())