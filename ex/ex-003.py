name_set = 'Kaike'
password_set = ('kaike1234')

user_name = input('Digite seu usuário para efetuar o login: ')
user_password = input('Digite sua senha: ')

def login():
    if user_name == name_set and user_password == password_set:
        print('Seja bem-vindo!')
    else:
        print('Credenciais inválidas. Tente novamente.')


login()