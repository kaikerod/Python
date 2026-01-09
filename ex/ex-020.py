class Musica:
    nome = ''
    artista = ''
    duracao = 0

musica1 = Musica()
musica1.nome = 'Always Then'
musica1.artista = 'The KVB'
musica1.duracao = 5

musica2 = Musica()
musica2.nome = 'Monet'
musica2.artista = 'Crippling Alcoholism'
musica2.duracao = 4

musica3 = Musica()
musica3.nome = 'The Felling Overcomes'
musica3.artista = 'Lovers Guilt'
musica3.duracao = 3

print(f'A musica {musica1.nome} do artista {musica1.artista} tem {musica1.duracao} minutos de duracao')
print(f'A musica {musica2.nome} do artista {musica2.artista} tem {musica2.duracao} minutos de duracao')
print(f'A musica {musica3.nome} do artista {musica3.artista} tem {musica3.duracao} minutos de duracao')

