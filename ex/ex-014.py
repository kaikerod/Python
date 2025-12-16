cardapio = {
    'X-Burguer': {'preco': 18.00, 'categoria': 'lanche', 'disponivel': True},
    'Pizza': {'preco': 45.00, 'categoria': 'principal', 'disponivel': True},
    'Refrigerante': {'preco': 6.00, 'categoria': 'bebida', 'disponivel': True},
}

cardapio['Poke'] = {'preco': 25.00, 'categoria': 'principal', 'disponivel': False}
cardapio['Refrigerante'] = {'preco': 6.00, 'categoria': 'bebida', 'disponivel': False}

print(cardapio)
