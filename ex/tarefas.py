import os


lista_de_tarefas = []


def exibir_opcoes():
    print("\nBem-vindo ao sistema de gerenciamento de tarefas!")
    print("--------------------------------")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair\n")


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()


def escolher_opcao():
    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            adicionar_tarefa()
        elif escolha == 2:
            listar_tarefas()
        elif escolha == 3:
            remover_tarefa()
        elif escolha == 4:
            sair()
        else:
            print("Opção inválida!")
    except ValueError:
        print("Opção inválida!")
        escolher_opcao()


def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    lista_de_tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    voltar_ao_menu_principal()


def listar_tarefas():
    if not lista_de_tarefas:
        print("Nenhuma tarefa encontrada!")
        voltar_ao_menu_principal()
    else:
        print("Lista de tarefas:")
        for i, tarefa in enumerate(lista_de_tarefas, 1):
            print(f"{i}. {tarefa}")
        voltar_ao_menu_principal()


def remover_tarefa():
    if not lista_de_tarefas:
        print("Nenhuma tarefa encontrada!")
        voltar_ao_menu_principal()
    else:
        print("Lista de tarefas:")
        for i, tarefa in enumerate(lista_de_tarefas, 1):
            print(f"{i}. {tarefa}")
        tarefa_remover = int(input("Digite o número da tarefa que deseja remover: "))
        try:
            lista_de_tarefas.pop(tarefa_remover - 1)
            print(f"Tarefa '{tarefa_remover}' removida com sucesso!")
            voltar_ao_menu_principal()
        except IndexError:
            print("Tarefa não encontrada!")
            voltar_ao_menu_principal()


def sair():
    print("Saindo do programa...")
    exit()


def main():
    os.system("cls")
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()