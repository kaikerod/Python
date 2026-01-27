class Musicas:
  lista_musicas = []

  def __init__(self, nome, artista, duracao):
    self.nome = nome
    self.artista = artista
    self.duracao = duracao
    Musicas.lista_musicas.append(self)

musica1 = Musicas()
musica1.nome = 'Always Then'
musica1.artista = 'KVB'
musica1.duracao = 320
