from model.client import Cliente

clientes=[]




def new_client():
    cpf=input("Digite o seu CPF (somente números): ")
    for cliente in clientes:
        if cpf==cliente["cpf"]:
            print("Usuário já possui cadastro")
            input("Pressione enter para continuar => ")
            break
    else:
        nome=input("Digite o seu nome completo: ")
        endereco=input("Digite o seu endereço no formato: Logradouro - Nro - Bairro - Cidade/sigla Estado ")
        data_nascimento=input("Digite a sua data de nascimento no formato (dd/mm/aaaa): ")
        cliente=Cliente(cpf, nome, endereco, data_nascimento)
        clientes.append(cliente.to_dict())
        print("Cliente cadastrado com sucesso")
        input("Pressione enter para continuar => ")



def update_client():
    cpf=input("Digite o seu CPF (somente números): ")

    # procurar cliente na lista
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("Cliente encontrado! Informe os novos dados:")
            nome=input("Digite o seu nome completo: ")
            endereco=input("Digite o seu endereco completo: ")
            data_nascimento=input("Digite a sua data de nascimento: ")
        # atualiza os campos
            cliente["nome"]=nome
            cliente["endereco"]=endereco
            cliente["data_nascimento"]=data_nascimento

            print("Cliente atualizado com sucesso")
            input("Pression enter para continuar => ")
            return
    # se não encontrar o cliente
    print("Cliente não encontrado.")
    input("Pressione Enter para continuar => ")

def delete_client():
    cpf=input("Digite o seu CPF do cliente que deseja excluir(somente números): => ")

    # procurar cliente na lista
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            op=input("Cliente encontrado! Digite [s] para excluir ou [n] para cancelar: => ")
            if op=="s":
                clientes.remove(cliente)
                print("Cliente excluído com sucesso.")
                input("Pressione Enter para continuar => ")
                return
            elif op=="n":
                print("opção cancelada.")
                input("Pressione Enter para continuar => ")              
                return
          
            
            else:
                print("opção inválida.")
                input("Pressione Enter para continuar => ")
                return



    # se não encontrar o cliente
    print("Cliente não encontrado.")
    input("Pressione Enter para continuar => ")

def list_all_clients():
    print("\n================ LISTA DE CLIENTES ================\n")

    for cliente in clientes:
        print(
            f"CPF: {cliente['cpf']}\n"
            f"Nome: {cliente['nome']}\n"
            f"Endereço: {cliente['endereco']}\n"
            f"Data de Nascimento: {cliente['data_nascimento']}\n"
        )
        print("==========================================\n")
    input("Pressione enter para continuar => ")



def menuCliente():
    while True:

        menu_cliente = """
================ MENU CLIENTES ================

    [n] Novo Cliente
    [l] Listar Clientes
    [a] Alterar dados Cliente
    [r] Remover Cliente
    [q] Sair

    => """

        opcao = input(menu_cliente).lower()

        if opcao == "n":
            new_client()

        elif opcao == "l":
            list_all_clients()

        elif opcao == "a":
            update_client()

        elif opcao == "r":
            delete_client()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
