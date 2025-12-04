from clienteTela import clientes
from model.conta import Conta

contas=[]


def identifica():
    cpf=input("Digite o seu CPF (somente números): => ")
    for cliente in clientes:
        if cpf==cliente["cpf"]:
            return cpf
            
 
    print("Cliente não encontrado.")
    input("Pressione Enter para continuar => ")
    return None
    


def new_account(cpf):
    if cpf is None:
        return

#verifica se cliente possui cadastro
    
    op=input("Cliente encontrado! Digite [s] para  criar uma nova conta ou [n] para cancelar: ")
    if op=="s":
        conta=Conta(cpf)
        contas.append(conta.to_dict())
        print("Conta criada com sucesso.")
        input("Pressione Enter para continuar => ")
        return
    elif op=="n":
        print("opção cancelada.")
        input("Pressione Enter para continuar => ")              
        return
    else:
        print("Opção inválida.")
        input("Pressione Enter para continuar => ")
        return
            


def list_all_accounts():
    print("\n================ LISTA DE CONTAS ================\n")

    for conta in contas:
        print(
            f"CPF: {conta['cpf']}\n"
            f"Agência: {conta['agencia']}\n"
            f"Número C/C: {conta['numero']}\n"
        )
        print("==========================================\n")
    input("Pressione enter para continuar => ")
      

def deposito(saldo,valor,extrato,/):

    #verifica se cliente possui cadastro

    if valor > 0:
        saldo+= valor
        extrato+= f"Depósito: R$ {valor:.2f}\n"


    else:
        print("Operação falhou! O valor informado é inválido.")
        input("Pressione enter para continuar => ")


    return saldo,extrato


def saque(*,saldo,valor,extrato,limite,numero_saques,LIMITE_SAQUES):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        input("Pressione enter para continuar => ")
        

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        input("Pressione enter para continuar => ")
        

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        input("Pressione enter para continuar => ")
        
        

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")
        input("Digite enter para continuar. => ")
        

    else:
        print("Operação falhou! O valor informado é inválido.")
        input("Digite enter para continuar. => ")
        
    return saldo,extrato,numero_saques


def exibir_extrato(saldo,/,*,extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    input("Pressione enter para continuar => ")
        
    return


def menuConta():
    while True:
        menu_conta = """
================ MENU CONTA BANCÁRIA ================

    [c] Criar Conta Bancária
    [l] Listar Contas 
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """


        opcao = input(menu_conta).lower()

        if opcao == "c":
            cpf=identifica()
            if cpf: 
                new_account(cpf)
                
                


        if opcao == "l":
            list_all_accounts()

        if opcao == "d":
            cpf=identifica()
            if cpf is None:
                continue
            for conta in contas:
                if conta["cpf"] == cpf:

                    valor=float(input("Informe o valor do depósito: "))
                    conta["saldo"], conta["extrato"] = deposito(conta["saldo"], valor,conta["extrato"])
                    print("Depósito realizado com sucesso.")
                    input("Pressione enter para continuar => ")
        
                    break
            else:
                print("Conta não encontrada.")
                input("Digite enter para continuar. => ")



        elif opcao == "s":
            cpf=identifica()
            if cpf is None:
                continue
            for conta in contas:
                if conta["cpf"] == cpf:
       
                    valor=float(input("Informe o valor do saque: "))
                    conta["saldo"],conta["extrato"],conta["numero_saques"] = saque(saldo=conta["saldo"], valor=valor,extrato=conta["extrato"],limite=500,numero_saques=conta["numero_saques"], LIMITE_SAQUES=3)
                    break
            else:
                print("Conta não encontrada.")
                input("Digite enter para continuar. => ")

        elif opcao == "e":
            cpf=identifica()
            if cpf is None:
                continue
            for conta in contas:
                if conta["cpf"] == cpf:
                    exibir_extrato(
                        conta["saldo"],      
                        extrato=conta["extrato"]  
                    )
                    break
            else:
                print("Conta não encontrada.")
                input("Digite enter para continuar.  => ")


        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")