class Musicas:
  lista_musicas = []

  def __init__(self, nome, artista, duracao):
    self.nome = nome
    self.artista = artista
    self.duracao = duracao
    Musicas.lista_musicas.append(self)

  def __str__(self):
    return f'{self.nome} | {self.artista} | {self.duracao}'

  def listar_musicas():
    for musica in Musicas.lista_musicas:
      print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica1 = Musicas('Always Then', 'KVB', 320)
musica2 = Musicas('MONET', 'Crippling Alcoholism', 246)

Musicas.listar_musicas()