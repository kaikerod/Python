class JogoForca:
  def __init__(self, palavra):
    self.palavra = palavra.upper()
    self.letras_tentadas = []
    self.tentativas = 6

  def mostrar_palavra(self):
    visual = []

    for letra in self.palavra:
      if letra in self.letras_tentadas:
        visual.append(letra)
      else:
        visual.append("_")
    return " ".join(visual)


meu_jogo = JogoForca("PYTHON")

meu_jogo.letras_tentadas.append("O")
meu_jogo.letras_tentadas.append("T")

print(f"Palavra atual: {meu_jogo.mostrar_palavra()}")