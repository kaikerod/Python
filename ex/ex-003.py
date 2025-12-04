name = 'Kaike'
password = ('kaike1234')

user_name = input('Digite seu usuário para efetuar o login: ')
user_password = input('Digite sua senha: ')

if user_name == name and user_password == password:
    print('Seja bem-vindo!')
else:
    print('Credenciais inválidas. Tente novamente.')