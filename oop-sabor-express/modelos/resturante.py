class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistro'
restaurante_praca.categoria = 'Italiana'

if restaurante_praca.ativo == False:
    print('Restaurante desativado!')
else:
    print('Restaurante ativado!')

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')