usuarios = [
    {'nome': 'Kaike', 'idade': '20', 'profissao': 'Dev'},
    {'nome': 'Rebeca', 'idade': '19', 'profissao': 'Estudante'}
]

# 1. Iterando sobre a lista para coletar e-mails e exibir dados
for dados in usuarios:
    # Pedindo o e-mail dinamicamente para cada usuário na lista
    email = input(f"Digite o e-mail de {dados['nome']}: ")
    
    # Adicionando a nova chave 'email' ao dicionário atual
    dados['email'] = email
    
    # Exibindo a frase com todos os dados atualizados
    print(f"Nome: {dados['nome']} | Idade: {dados['idade']} | Profissão: {dados['profissao']} | E-mail: {dados['email']}")
    print("-" * 30)

# 2. Mostrando como a lista ficou ao final
print("\nLista final de usuários:")
print(usuarios)