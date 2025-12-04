from clienteTela import menuCliente
from contaTela import menuConta


def menu():

    executando=True

    while executando:
        menu = """  
        SEJA BEM-VINDO(A)!
        
        Escolha uma opção:

        [c] Cliente
        [b] Conta Bancária
        [q] Sair

        => """


        opcao = input(menu).lower()

        if opcao == "c":
            menuCliente()


        elif opcao == "b":
            menuConta()


        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

#executar a função principal, construtor
if __name__ == "__main__":
    menu()