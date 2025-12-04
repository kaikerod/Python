import os

print('Sabor express \n')

print('1. Cadastrar Restaurante')
print('2. Listar Restaurantes')
print('3. Ativar Restaurante')
print('4. Sair \n')

opcao_escolhida = int(input('Escolha uma opção: '))

def cadastro():
    dados_cadastro = []
    dados_cadastro = input('Preencha com o nome e endereço: \n')
    

def finalizar_app():
    os.system('cls')
    print('Saindo...')

if opcao_escolhida == 1:
    cadastro()
else:
    finalizar_app()