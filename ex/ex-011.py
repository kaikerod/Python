usuarios = [{'nome':'Kaike', 'idade':'20', 'profissao':'Dev'},
            {'nome':'Rebeca', 'idade':'19', 'profissao':'Estudante'}
]

for dados in usuarios:
    nome = dados['nome']
    idade = dados['idade']
    profissao = dados['profissao']
    print(f'Seu nome é {nome}, sua idade é de {idade} anos e sua profissão é {profissao}')