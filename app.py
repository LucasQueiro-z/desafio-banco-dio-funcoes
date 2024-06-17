def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    extrato.append(f'Saldo Antes: R$ {saldo}')
    if valor > 0:
        if valor <= saldo:
            if valor <= limite:
                if numero_saques < limite_saques:
                    saldo -= valor
                    numero_saques += 1
                    extrato.append(f"Saque no valor de R$ {valor:.2f}, Saldo Atual: R$ {saldo:.2f}")
                    print(f"""
                        Saque no valor de R$ {valor:.2f} efetuado!
                        Extrato: {extrato}
                    """)
                else:
                    print("Limite de saques diários atingido!")
            else:
                print("Valor máximo por saque permitido é de R$ 500,00")
        else:
            print(f"Valor de saque (R$ {valor:.2f}) maior que o saldo atual (R$ {saldo:.2f})!")
    else:
        print("Saque inválido, valor deve ser acima de R$ 0,00")
    
    return saldo, extrato, numero_saques

def deposito(saldo, valor, extrato):
    extrato.append(f'Saldo Antes: R$ {saldo:.2f}')
    if valor > 0:
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} efetuado!")
        extrato.append(f'Valor do depósito: R$ {valor:.2f}')
        extrato.append(f"Saldo Atual: R$ {saldo:.2f}")
        print(f"Extrato: {extrato}")
    else:
        print("Valor do depósito deve ser maior que R$ 0,00")
    return saldo, extrato

def mostrar_extrato(saldo, *, extrato):
    if extrato:
        extrato.append(f'Saldo: R$ {saldo:.2f}')
        print("Extrato:")
        for linha in extrato:
            print(linha)
    else:
        print("Não há movimentações")
    return extrato

def cadastro_de_usuario(lista_users, nome, data_nascimento, cpf, endereco):
    if len(nome) > 0 and len(data_nascimento) > 0 and len(cpf) > 0 and len(endereco) > 0:
        if cpf.isdigit():
            lista_users.append(f"Nome: {nome} - Nascimento: {data_nascimento} - CPF: {cpf} - Endereço: {endereco}")
            print("Usuário cadastrado com sucesso!")
        else:
            print("CPF deve conter apenas números!")
    else:
        print("Todos os campos devem ser preenchidos!")

def criar_conta_corrente(lista_contas, nome_usuario):
    if len(nome_usuario.strip()) == 0:
        print("Digite um nome válido!")
    else:
        contar_contas = len(lista_contas) + 1
        lista_contas.append(f"Conta: {contar_contas} - Nome: {nome_usuario} - Agência: 0001")
        print(f"Conta corrente criada com sucesso! Número da conta: {contar_contas}")
    return lista_contas

def menu():
    saldo = 0.0
    extrato = []
    limite = 500.0
    numero_saques = 0
    limite_saques = 3
    lista_users = []
    lista_contas = []

    while True:
        print("\n----- Menu -----")
        print("1. Saque")
        print("2. Depósito")
        print("3. Mostrar Extrato")
        print("4. Cadastro de Usuário")
        print("5. Criar Conta Corrente")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)
        
        elif opcao == '2':
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == '3':
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            nome = input("Digite o nome: ")
            data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
            cpf = input("Digite o CPF: ")
            endereco = input("Digite o endereço: ")
            cadastro_de_usuario(lista_users, nome, data_nascimento, cpf, endereco)

        elif opcao == '5':
            nome_usuario = input("Digite o nome do usuário para a conta corrente: ")
            lista_contas = criar_conta_corrente(lista_contas, nome_usuario)

        elif opcao == '6':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()