class JogoForca:
  def __init__(self, palavra):
    self.palavra = palavra.upper()
    self.letras_tentadas = []
    self.tentativas = 6


meu_jogo = JogoForca("PYTHON")
print(f"Palavra: {meu_jogo.palavra}")
print(f"Tentativas: {meu_jogo.tentativas}")
print(f"Letras já chutadas: {meu_jogo.letras_tentadas}")