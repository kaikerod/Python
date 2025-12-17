dados_pessoais = {
    'nome': 'Kaike',
    'idade': 20,
    'cidade': 'São Paulo',
    'estado': 'SP',
    'pais': 'Brasil'
}

dados_pessoais['email'] = 'kaike@gmail.com'
estado = dados_pessoais.pop('estado')

for chave, valor in dados_pessoais.items():
    print(f'{chave}: {valor}')

for chave in dados_pessoais.keys():
    if chave == 'email':
        print(f'{chave}: {dados_pessoais[chave]}')