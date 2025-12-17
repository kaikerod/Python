playlist = {
    'Bohemian Rhapsody': {'artista': 'Queen', 'duracao': 354, 'ano': 1975, 'plays': 1250},
    'Imagine': {'artista': 'John Lennon', 'duracao': 183, 'ano': 1971, 'plays': 890},
}

playlist['Hotel California'] = {'artista': 'Eagles', 'duracao': 252, 'ano': 1977, 'plays': 1500}
playlist['Crippling Alcoholism'] = {'artista': 'Anathema', 'duracao': 245, 'ano': 2000, 'plays': 1000}

total_duracao = 0
mais_plays = 0

for duracao in playlist.values():
    total_duracao += duracao['duracao']

print(f'Esta é a duracao total: {total_duracao}')

for mais_tocada in playlist.values():
    mais_plays += mais_tocada['plays']

print(f'Esta é a musica mais tocada: {mais_plays}')