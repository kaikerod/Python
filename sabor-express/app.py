import os

restaurantes_cadastrados = ['Trash and Fresh', 'Hot in Tender']

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes \n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes_cadastrados.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso! \n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    os.system('cls')
    print('Listando restaurantes: \n')

    for restaurante in restaurantes_cadastrados:
        print(f'-{restaurante}')

    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()