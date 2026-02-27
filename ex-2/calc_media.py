class Turma:
  def __init__(self):
    self.lista_notas = []

  def adicionar_nota(self, nota):
    self.lista_notas.append(nota)

  def calc_media(self):
    if not self.lista_notas:
      return 0
    soma_total = sum(self.lista_notas)
    quantidade_de_notas = len(self.lista_notas)

    media = soma_total / quantidade_de_notas
    return media

  def verificar_notas(self):
    if not self.lista_notas:
      return None, None
    return max(self.lista_notas), min(self.lista_notas)

  def contar_notas_acima_da_media(self):
    media = self.calc_media()
    notas_acima = [nota for nota in self.lista_notas if nota > media]
    return len(notas_acima)

turma_python = Turma()
turma_python.adicionar_nota(4)
turma_python.adicionar_nota(4.6)
turma_python.adicionar_nota(9)
turma_python.adicionar_nota(8)
maior, menor = turma_python.verificar_notas()
print(f"A maior nota é: {maior}")
print(f"A menor nota é: {menor}")
print(f"A média da turma é: {turma_python.calc_media()}")
print(f"Quantidade de notas acima da média: {turma_python.contar_notas_acima_da_media()}")