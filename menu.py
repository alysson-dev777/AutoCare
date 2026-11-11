from datetime import date
from models.cliente import Cliente
from models.ordem_servico import OrdemServico
from models.servico import Servico
from repositories.cliente_database_repository import ClienteDatabaseRepository
from repositories.ordem_servico_database_repository import OrdemServicoDatabaseRepository
from repositories.servico_database_repository import ServicoDatabaseRepository
from repositories.relatorio_database_repository import RelatorioDatabaseRepository


from validators import (
    validar_cpf,
    validar_preco,
    validar_email,
    validar_nome,
    validar_telefone,
    validar_status,
    pode_alterar_ordem_servico
)

def ler_opcao():
    try:
        return int(input(">>> "))
    
    except ValueError:
        return -1

def exibir_menu():
    print("------------ AutoCare ------------")
    print("[1] - Gerenciar Clientes")
    print("[2] - Gerenciar Serviços")
    print("[3] - Gerenciar Ordens de Serviços")
    print("[4] - Gerenciar Relatórios")
    print("[0] - Sair")
    print("----------------------------------")

def cadastrar_cliente():
    print("\n---------- Cadastro de Cliente ----------")

    while True:
        nome = input("Nome: ").strip()
        if not nome:
            print("----------------------------------")
            print("O nome do cliente é obrigatório.")
            print("----------------------------------")
            continue
        if validar_nome(nome):
            break
        print("------------------------------------------------")
        print("Nome inválido! O nome não pode conter números.")
        print("------------------------------------------------")
    
    while True:
        cpf = input("CPF (apenas números): ").strip()
        if validar_cpf(cpf):
            break
        print("------------------------------------------------")
        print("CPF inválido! Digite exatamente 11 números.")
        print("------------------------------------------------")

    while True:
        telefone = input("Telefone: ").strip()
        if validar_telefone(telefone):
            break
        print("------------------------------------------------")
        print("Telefone inválido! Digite apenas números e símbolos permitidos (+, -, ()).")
        print("------------------------------------------------")
    
    
    while True:
        email = input("Email: ").strip()
        if validar_email(email):
            break
        print("------------------------------------------------")
        print("Email inválido! Formato esperado: nome@dominio.com")
        print("------------------------------------------------")

    cliente = Cliente(
        None,
        nome,
        cpf,
        telefone,
        email
    )

    repositorio = ClienteDatabaseRepository()
    resultado = repositorio.save(cliente)

    if resultado:
        print("\nCliente cadastrado com sucesso!")
        print(f"ID gerado: {cliente.id_cliente}")
    else:
        print("\nErro ao cadastrar cliente.")

def listar_cliente():
    repositorio = ClienteDatabaseRepository()
    clientes = repositorio.get_all()

    if clientes:
        print("\n----------- Lista de Clientes -----------")
        for cliente in clientes:
            print("----------------------------------")
            print(f"ID: {cliente.id_cliente}")
            print(f"Nome: {cliente.nome}")
            print(f"CPF: {cliente.cpf}")
            print(f"Telefone: {cliente.telefone}")
            print(f"Email: {cliente.email}")
        print("----------------------------------")

    else:
        print("\nNenhum cliente cadastrado.")

def buscar_cliente():
    repositorio = ClienteDatabaseRepository()

    try:
        id_cliente = int(input("Informe o ID do cliente que deseja buscar: "))

        if id_cliente <= 0:
            print("----------------------------------")
            print("O ID deve ser um número positivo.")
            print("----------------------------------")
            return

    except ValueError:
        print("--------------------------------------")
        print("ID Inválido! Digite um número inteiro.")
        print("--------------------------------------")
        return

    cliente = repositorio.find_by_id(id_cliente)

    if cliente is not None:
        print("\n----------- Cliente Encontrado -----------")
        print(f"ID: {cliente.id_cliente}")
        print(f"Nome: {cliente.nome}")
        print(f"CPF: {cliente.cpf}")
        print(f"Telefone: {cliente.telefone}")
        print(f"Email: {cliente.email}")
    else:
        print("----------------------------------")
        print("Cliente não encontrado.")
        print("----------------------------------")

def atualizar_cliente():
    repositorio = ClienteDatabaseRepository()

    try:
        id_cliente = int(input("Informe o ID do cliente que deseja editar: "))

    except ValueError:
        print("--------------------------------------")
        print("ID inválido! Digite um número inteiro.")
        print("--------------------------------------")
        return

    if id_cliente <= 0:
        print("----------------------------------------")
        print("ID inválido! Informe um número positivo.")
        print("----------------------------------------")
        return

    cliente = repositorio.find_by_id(id_cliente)

    if cliente is not None:

        while True:
            print("\n----------- Atualizar Cliente -----------")
            print(f"Cliente: {cliente.nome}")
            print("[1] - Nome")
            print("[2] - CPF")
            print("[3] - Telefone")
            print("[4] - Email")
            print("[0] - Voltar")

            opcao = ler_opcao()

            match opcao:

                case 1:
                    novo_valor = input("Informe o novo nome: ").strip()

                    if not novo_valor:
                        print("--------------------------------------")
                        print("O nome não pode ficar vazio.")
                        print("--------------------------------------")
                        continue
                        
                    if not validar_nome(novo_valor):
                        print("--------------------------------------")
                        print("Nome inválido! O nome não pode conter números.")
                        print("--------------------------------------")
                        continue

                    cliente.nome = novo_valor

                    resultado = repositorio.update(cliente)

                    if resultado:
                        print("--------------------------------------")
                        print("Nome atualizado com sucesso!")
                        print("--------------------------------------")
                    else:
                        print("--------------------------------------")
                        print("Erro ao atualizar nome.")
                        print("--------------------------------------")

                case 2:
                    novo_valor = input("Informe o novo CPF (apenas números): ").strip()

                    if not novo_valor:
                        print("--------------------------------------")
                        print("O CPF não pode ficar vazio.")
                        print("--------------------------------------")
                        continue
                    
                    if not validar_cpf(novo_valor):
                        print("--------------------------------------")
                        print("CPF inválido! Digite exatamente 11 números.")
                        print("--------------------------------------")
                        continue

                    cliente.cpf = novo_valor

                    resultado = repositorio.update(cliente)

                    if resultado:
                        print("--------------------------------------")
                        print("CPF atualizado com sucesso!")
                        print("--------------------------------------")
                    else:
                        print("--------------------------------------")
                        print("Erro ao atualizar CPF.")
                        print("--------------------------------------")

                case 3:
                    novo_valor = input("Informe o novo telefone: ").strip()

                    if not novo_valor:
                        print("--------------------------------------")
                        print("O telefone não pode ficar vazio.")
                        print("--------------------------------------")
                        continue
                        
                    if not validar_telefone(novo_valor):
                        print("--------------------------------------")
                        print("Telefone inválido! Não utilize letras.")
                        print("--------------------------------------")
                        continue

                    cliente.telefone = novo_valor

                    resultado = repositorio.update(cliente)

                    if resultado:
                        print("--------------------------------------")
                        print("Telefone atualizado com sucesso!")
                        print("--------------------------------------")
                    else:
                        print("--------------------------------------")
                        print("Erro ao atualizar telefone.")
                        print("--------------------------------------")

                case 4:
                    novo_valor = input("Informe o novo email: ").strip()

                    if not novo_valor:
                        print("--------------------------------------")
                        print("O email não pode ficar vazio.")
                        print("--------------------------------------")
                        continue
                    
                    if not validar_email(novo_valor):
                        print("--------------------------------------")
                        print("Email inválido! Formato esperado: nome@dominio.com")
                        print("--------------------------------------")
                        continue

                    cliente.email = novo_valor

                    resultado = repositorio.update(cliente)

                    if resultado:
                        print("--------------------------------------")
                        print("Email atualizado com sucesso!")
                        print("--------------------------------------")
                    else:
                        print("--------------------------------------")
                        print("Erro ao atualizar email.")
                        print("--------------------------------------")

                case -1:
                    print("--------------------------------------")
                    print("Opção inválida! Digite um número.")
                    print("--------------------------------------")
                    continue

                case 0:
                    break

                case _:
                    print("--------------------------------------")
                    print("Opção inválida! Tente novamente.")
                    print("--------------------------------------")
                    continue

    else:
        print("----------------------------------")
        print("Cliente não encontrado.")
        print("----------------------------------")

def excluir_cliente():
    repositorio = ClienteDatabaseRepository()

    try:
        id_cliente = int(input("Informe o ID do cliente que deseja excluir: "))

        if id_cliente <= 0:
            print("----------------------------------")
            print("O ID deve ser um número positivo.")
            print("----------------------------------")
            return

    except ValueError:
        print("--------------------------------------")
        print("ID Inválido! Digite um número inteiro.")
        print("--------------------------------------")
        return

    cliente = repositorio.find_by_id(id_cliente)

    if cliente is not None:
        resultado = repositorio.delete(id_cliente)

        if resultado:
            print("----------------------------------")
            print("Cliente excluído com sucesso!")
            print("----------------------------------")
        else:
            print("----------------------------------")
            print("Erro ao excluir cliente.")
            print("----------------------------------")
    else:
        print("----------------------------------")
        print("Cliente não encontrado.")
        print("----------------------------------")

def cadastrar_servico():
    print("\n---------- Cadastro de Serviço ----------")

    while True:
        nome_servico = input("Nome do serviço: ").strip()

        if not nome_servico:
            print("----------------------------------")
            print("O nome do serviço é obrigatório.")
            print("----------------------------------")
            continue

        if validar_nome(nome_servico):
            break
        print("--------------------------------------------------")
        print("Nome inválido! Verifique o nome do serviço.")
        print("--------------------------------------------------")

    descricao = input("Descrição do serviço: ").strip()

    while True:
        preco_str = input("Preço padrão do serviço: R$").strip()
        if validar_preco(preco_str):
            preco_padrao = float(preco_str)
            break
        print("----------------------------------------------------")
        print("Preço Inválido! Digite um valor decimal não negativo.")
        print("----------------------------------------------------")

    servico = Servico(
        None,
        nome_servico,
        descricao,
        preco_padrao
    )

    repositorio = ServicoDatabaseRepository()
    resultado = repositorio.save(servico)

    if resultado:
        print("\nServiço cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar serviço.")

def listar_servico():
    repositorio = ServicoDatabaseRepository()
    servicos = repositorio.get_all()

    if servicos:
        print("\n----------- Lista de Serviços -----------")
        for servico in servicos:
            print("----------------------------------")
            print(f"ID: {servico.id_servico}")
            print(f"Nome: {servico.nome_servico}")
            print(f"Descrição: {servico.descricao}")
            print(f"Preço Padrão: R${servico.preco_padrao:.2f}")
        print("----------------------------------")

    else:
        print("\nNenhum serviço cadastrado.")

def buscar_servico():
    repositorio = ServicoDatabaseRepository()

    try:
        id_servico = int(input("Informe o ID do serviço que deseja buscar: "))
    
        if id_servico <= 0:
            print("----------------------------------")
            print("O ID deve ser um número positivo.")
            print("----------------------------------")
            return
    
    except ValueError:
            print("--------------------------------------")
            print("ID Inválido! Digite um número inteiro.")
            print("--------------------------------------")
            return


    servico = repositorio.find_by_id(id_servico)

    if servico is not None:
        print("\n----------- Serviço Encontrado -----------")
        print(f"ID: {servico.id_servico}")
        print(f"Nome: {servico.nome_servico}")
        print(f"Descrição: {servico.descricao}")
        print(f"Preço Padrão: R${servico.preco_padrao:.2f}")

    else:
        print("----------------------------------")
        print("Serviço não encontrado.")
        print("----------------------------------")

def atualizar_servico():
    repositorio = ServicoDatabaseRepository()

    try:
        id_servico = int(input("Informe o ID do serviço que deseja editar: "))

    except ValueError:
        print("--------------------------------------")
        print("ID inválido! Digite um número inteiro.")
        print("--------------------------------------")
        return

    if id_servico <= 0:
        print("----------------------------------------")
        print("ID inválido! Informe um número positivo.")
        print("----------------------------------------")
        return

    servico = repositorio.find_by_id(id_servico)

    if servico is not None:

        while True:
            print("\n----------- Atualizar Serviço -----------")
            print(f"Serviço: {servico.nome_servico}")
            print("[1] - Nome")
            print("[2] - Descrição")
            print("[3] - Preço")
            print("[0] - Voltar")

            opcao = ler_opcao()

            match opcao:

                case 1:
                    novo_valor = input("Informe o novo nome: ").strip()

                    if not novo_valor:
                        print("--------------------------------------")
                        print("O nome não pode ficar vazio.")
                        print("--------------------------------------")
                        continue

                    if not validar_nome(novo_valor):
                        print("--------------------------------------")
                        print("Nome inválido! Verifique o nome do serviço.")
                        print("--------------------------------------")
                        continue

                    servico.nome_servico = novo_valor

                    resultado = repositorio.update(servico)

                    if resultado:
                        print("--------------------------------------")
                        print("Nome atualizado com sucesso!")
                        print("--------------------------------------")
                    else:
                        print("--------------------------------------")
                        print("Erro ao atualizar nome.")
                        print("--------------------------------------")

                case 2:
                    novo_valor = input("Informe a nova descrição: ").strip()

                    if not novo_valor:
                        print("--------------------------------------")
                        print("A descrição não pode ficar vazia.")
                        print("--------------------------------------")
                        continue

                    servico.descricao = novo_valor

                    resultado = repositorio.update(servico)

                    if resultado:
                        print("--------------------------------------")
                        print("Descrição atualizada com sucesso!")
                        print("--------------------------------------")
                    else:
                        print("--------------------------------------")
                        print("Erro ao atualizar descrição.")
                        print("--------------------------------------")

                case 3:
                    novo_valor = input("Informe o novo preço: R$").strip()
                    
                    if not validar_preco(novo_valor):
                        print("--------------------------------------")
                        print("Preço inválido! Digite um valor numérico não negativo.")
                        print("--------------------------------------")
                        continue

                    servico.preco_padrao = float(novo_valor)

                    resultado = repositorio.update(servico)

                    if resultado:
                        print("--------------------------------------")
                        print("Preço atualizado com sucesso!")
                        print("--------------------------------------")
                    else:
                        print("--------------------------------------")
                        print("Erro ao atualizar preço.")
                        print("--------------------------------------")

                case -1:
                    print("--------------------------------------")
                    print("Opção inválida! Digite um número.")
                    print("--------------------------------------")
                    continue

                case 0:
                    break

                case _:
                    print("--------------------------------------")
                    print("Opção inválida! Tente novamente.")
                    print("--------------------------------------")
                    continue

    else:
        print("----------------------------------")
        print("Serviço não encontrado.")
        print("----------------------------------")

def excluir_servico():
    repositorio = ServicoDatabaseRepository()

    try:
        id_servico = int(input("Informe o ID do serviço que deseja excluir: "))
    
        if id_servico <= 0:
                print("----------------------------------")
                print("O ID deve ser um número positivo.")
                print("----------------------------------")
                return
    
    except ValueError:
        print("--------------------------------------")
        print("ID Inválido! Digite um número inteiro.")
        print("--------------------------------------")
        return

    servico = repositorio.find_by_id(id_servico)

    if servico is not None:
        resultado = repositorio.delete(id_servico)

        if resultado:
            print("----------------------------------")
            print("Serviço excluído com sucesso!")
            print("----------------------------------")
        else:
            print("----------------------------------")
            print("Erro ao excluir serviço.")
            print("----------------------------------")
    else:
        print("----------------------------------")
        print("Serviço não encontrado.")
        print("----------------------------------")

def cadastrar_ordem_servico():
    print("\n------ Cadastro de Ordem de Serviço ------")

    try:
        id_cliente = int(input("ID do cliente: "))
        id_servico = int(input("ID do serviço: "))
        
        while True:
            preco_str = input("Valor cobrado: R$").strip()
            if validar_preco(preco_str):
                valor_cobrado = float(preco_str)
                break
            print("----------------------------------------------------")
            print("Valor Inválido! Digite um valor decimal não negativo.")
            print("----------------------------------------------------")

    except ValueError:
        print("-------------------------------------------------")
        print("Entrada Inválida! Verifique os valores informados")
        print("-------------------------------------------------")
        return

    if id_cliente <= 0:
        print("----------------------------------------")
        print("O ID do cliente deve ser maior que zero.")
        print("----------------------------------------")
        return
    
    if id_servico <= 0:
        print("----------------------------------------")
        print("O ID do serviço deve ser maior que zero.")
        print("----------------------------------------")
        return
    
    cliente_repositorio = ClienteDatabaseRepository()
    servico_repositorio = ServicoDatabaseRepository()

    if cliente_repositorio.find_by_id(id_cliente) is None:
        print("Cliente não encontrado!")
        return

    if servico_repositorio.find_by_id(id_servico) is None:
        print("Serviço não encontrado!")
        return

    ordem_servico = OrdemServico(
        None,
        id_cliente,
        id_servico,
        None,
        valor_cobrado,
        None
    )

    repositorio = OrdemServicoDatabaseRepository()
    resultado = repositorio.save(ordem_servico)

    if resultado:
        print("----------------------------------------")
        print("Ordem de serviço cadastrado com sucesso!")
        print("----------------------------------------")
    else:
        print("-----------------------------------")
        print("Erro ao cadastrar ordem de serviço.")
        print("-----------------------------------")


def listar_ordem_servico():
    repositorio = OrdemServicoDatabaseRepository()

    ordens = repositorio.get_all()

    if ordens:
        print("------- Lista de Ordens de Serviço -------")

        for ordem in ordens:
            print("----------------------------------")
            print(f"ID da OS: {ordem.id_os}")
            print(f"ID do Cliente: {ordem.id_cliente}")
            print(f"ID do Serviço: {ordem.id_servico}")
            print(f"Data de Abertura: {ordem.data_abertura}")
            print(f"Valor Cobrado: R${ordem.valor_cobrado:.2f}")
            print(f"Status: {ordem.status}")

        print("----------------------------------")
    else:
        print("\nNenhuma Ordem de Serviço cadastrada.")


def buscar_ordem_servico():
    repositorio = OrdemServicoDatabaseRepository()

    try:
        id_os = int(input("Informe o ID da Ordem de Serviço que deseja buscar: "))

        if id_os <= 0:
            print("----------------------------------------")
            print("ID inválido! Informe um número positivo.")
            print("----------------------------------------")
            return

    except ValueError:
        print("--------------------------------------")
        print("ID inválido! Digite um número inteiro.")
        print("--------------------------------------")
        return

    ordem = repositorio.find_by_id(id_os)

    if ordem is not None:
        print("\n------- Ordem de Serviço Encontrada -------")
        print(f"ID da OS: {ordem.id_os}")
        print(f"ID do Cliente: {ordem.id_cliente}")
        print(f"ID do Serviço: {ordem.id_servico}")
        print(f"Data de Abertura: {ordem.data_abertura}")
        print(f"Valor Cobrado: R$ {ordem.valor_cobrado:.2f}")
        print(f"Status: {ordem.status}")

    else:
        print("-------------------------------------")
        print("Ordem de Serviço não encontrada.")
        print("-------------------------------------")


def atualizar_ordem_servico():
    repositorio = OrdemServicoDatabaseRepository()

    try:
        id_os = int(input("Informe o ID da Ordem de Serviço que deseja editar: "))

    except ValueError:
        print("--------------------------------------")
        print("ID inválido! Digite um número inteiro.")
        print("--------------------------------------")
        return

    if id_os <= 0:
        print("----------------------------------------")
        print("ID inválido! Informe um número positivo.")
        print("----------------------------------------")
        return

    ordem = repositorio.find_by_id(id_os)

    if ordem is not None:

        if not pode_alterar_ordem_servico(ordem):
            print("--------------------------------------------------------")
            print("Ação bloqueada: Não é possível alterar uma OS Concluída.")
            print("--------------------------------------------------------")
            return

        while True:
            print("\n------ Atualizar Ordem de Serviço ------")
            print(f"Ordem de Serviço: {ordem.id_os}")
            print("[1] - ID do Cliente")
            print("[2] - ID do Serviço")
            print("[3] - Valor Cobrado")
            print("[4] - Status")
            print("[0] - Voltar")

            opcao = ler_opcao()

            match opcao:

                case 1:
                    try:
                        novo_valor = int(input("Informe o novo ID do cliente: "))
                    except ValueError:
                        print("--------------------------------------")
                        print("ID inválido! Digite um número inteiro.")
                        print("--------------------------------------")
                        continue

                    if novo_valor <= 0:
                        print("----------------------------------------")
                        print("O ID do cliente deve ser maior que zero.")
                        print("----------------------------------------")
                        continue

                    cliente_repositorio = ClienteDatabaseRepository()

                    if cliente_repositorio.find_by_id(novo_valor) is None:
                        print("--------------------------------------")
                        print("Cliente não encontrado.")
                        print("--------------------------------------")
                        continue

                    ordem.id_cliente = novo_valor

                    resultado = repositorio.update(ordem)

                    if resultado:
                        print("--------------------------------------")
                        print("ID do cliente atualizado com sucesso!")
                        print("--------------------------------------")
                    else:
                        print("--------------------------------------")
                        print("Erro ao atualizar ID do cliente.")
                        print("--------------------------------------")

                case 2:
                    try:
                        novo_valor = int(input("Informe o novo ID do serviço: "))
                    except ValueError:
                        print("--------------------------------------")
                        print("ID inválido! Digite um número inteiro.")
                        print("--------------------------------------")
                        continue

                    if novo_valor <= 0:
                        print("----------------------------------------")
                        print("O ID do serviço deve ser maior que zero.")
                        print("----------------------------------------")
                        continue

                    servico_repositorio = ServicoDatabaseRepository()

                    if servico_repositorio.find_by_id(novo_valor) is None:
                        print("--------------------------------------")
                        print("Serviço não encontrado.")
                        print("--------------------------------------")
                        continue

                    ordem.id_servico = novo_valor

                    resultado = repositorio.update(ordem)

                    if resultado:
                        print("--------------------------------------")
                        print("ID do serviço atualizado com sucesso!")
                        print("--------------------------------------")
                    else:
                        print("--------------------------------------")
                        print("Erro ao atualizar ID do serviço.")
                        print("--------------------------------------")

                case 3:
                    novo_valor = input("Informe o novo valor cobrado: R$").strip()
                    
                    if not validar_preco(novo_valor):
                        print("--------------------------------------")
                        print("Valor inválido! Digite um número decimal não negativo.")
                        print("--------------------------------------")
                        continue

                    ordem.valor_cobrado = float(novo_valor)

                    resultado = repositorio.update(ordem)

                    if resultado:
                        print("--------------------------------------")
                        print("Valor cobrado atualizado com sucesso!")
                        print("--------------------------------------")
                    else:
                        print("--------------------------------------")
                        print("Erro ao atualizar valor cobrado.")
                        print("--------------------------------------")

                case 4:
                    print("\nStatus disponíveis:")
                    print("[1] - Aberta")
                    print("[2] - Em Andamento")
                    print("[3] - Concluída")

                    opcao_status = ler_opcao()

                    match opcao_status:
                        case 1:
                            novo_status = "Aberta"
                        case 2:
                            novo_status = "Em Andamento"
                        case 3:
                            novo_status = "Concluída"
                        case -1:
                            print("--------------------------------------")
                            print("Opção inválida! Digite um número.")
                            print("--------------------------------------")
                            continue
                        case _:
                            print("--------------------------------------")
                            print("Opção de status inválida!")
                            print("--------------------------------------")
                            continue
                    
                    if not validar_status(novo_status):
                        print("Status inválido!")
                        continue

                    ordem.status = novo_status

                    resultado = repositorio.update(ordem)

                    if resultado:
                        print("--------------------------------------")
                        print("Status atualizado com sucesso!")
                        print("--------------------------------------")
                    else:
                        print("--------------------------------------")
                        print("Erro ao atualizar status.")
                        print("--------------------------------------")

                case -1:
                    print("--------------------------------------")
                    print("Opção inválida! Digite um número.")
                    print("--------------------------------------")
                    continue

                case 0:
                    break

                case _:
                    print("--------------------------------------")
                    print("Opção inválida! Tente novamente.")
                    print("--------------------------------------")
                    continue

    else:
        print("----------------------------------")
        print("Ordem de Serviço não encontrada.")
        print("----------------------------------")

def excluir_ordem_servico():
    repositorio = OrdemServicoDatabaseRepository()

    try:
        id_os = int(input("Informe o ID da Ordem de Serviço que deseja excluir: "))

        if id_os <= 0:
            print("----------------------------------------")
            print("ID inválido! Informe um número positivo.")
            print("----------------------------------------")
            return

    except ValueError:
        print("--------------------------------------")
        print("ID inválido! Digite um número inteiro.")
        print("--------------------------------------")
        return

    ordem = repositorio.find_by_id(id_os)

    if ordem is not None:
        resultado = repositorio.delete(id_os)

        if resultado:
            print("--------------------------------------")
            print("Ordem de Serviço excluída com sucesso!")
            print("--------------------------------------")
        else:
            print("---------------------------------")
            print("Erro ao excluir Ordem de Serviço.")
            print("---------------------------------")
    else:
        print("--------------------------------")
        print("Ordem de Serviço não encontrada.")
        print("--------------------------------")


def menu_cliente():
    while True:

        print("\n------------ Clientes ------------")
        print("[1] - Cadastrar Cliente")
        print("[2] - Listar Clientes")
        print("[3] - Buscar Cliente por ID")
        print("[4] - Atualizar Cliente")
        print("[5] - Excluir Cliente")
        print("[0] - Voltar")
        print("----------------------------------")

        opcao = ler_opcao()

        match opcao:
            case 1:
                cadastrar_cliente()
            case 2:
                listar_cliente()
            case 3:
                buscar_cliente()
            case 4:
                atualizar_cliente()
            case 5:
                excluir_cliente()
            case 0:
                break
            case -1:
                print("Opção Inválida. Digite um número.")
            case _:
                print("Opção Inválida! Tente novamente.")

def menu_servico():
    while True:

        print("\n------------ Serviços ------------")
        print("[1] - Cadastrar Serviço")
        print("[2] - Listar Serviços")
        print("[3] - Buscar Serviço por ID")
        print("[4] - Atualizar Serviço")
        print("[5] - Excluir Serviço")
        print("[0] - Voltar")
        print("----------------------------------")

        opcao = ler_opcao()

        match opcao:
            case 1:
                cadastrar_servico()
            case 2:
                listar_servico()
            case 3:
                buscar_servico()
            case 4:
                atualizar_servico()
            case 5:
                excluir_servico()
            case 0:
                break
            case -1:
                print("Opção Inválida. Digite um número.")
            case _:
                print("Opção Inválida! Tente novamente.")

def menu_ordem_servico():
    while True:

        print("\n------ Ordens de Serviços ------")
        print("[1] - Cadastrar Ordem de Serviço")
        print("[2] - Listar Ordens de Serviço")
        print("[3] - Buscar Ordem de Serviço por ID")
        print("[4] - Atualizar Ordem de Serviço")
        print("[5] - Excluir Ordem de Serviço")
        print("[0] - Voltar")
        print("----------------------------------")

        opcao = ler_opcao()

        match opcao:
            case 1:
                cadastrar_ordem_servico()
            case 2:
                listar_ordem_servico()
            case 3:
                buscar_ordem_servico()
            case 4:
                atualizar_ordem_servico()
            case 5:
                excluir_ordem_servico()
            case 0:
                break
            case -1:
                print("Opção Inválida. Digite um número.")
            case _:
                print("Opção Inválida! Tente novamente.")

def menu_relatorios():
    repositorio = RelatorioDatabaseRepository()

    while True:
        print("\n-------------- Relatórios --------------")
        print("[1] - Quantidade de OS por serviço")
        print("[2] - Faturamento por serviço")
        print("[3] - Quantidade de OS e média por cliente")
        print("[0] - Voltar")
        print("------------------------------------")

        opcao = ler_opcao()

        match opcao:
            case 1:
                resultados = repositorio.quantidade_os_por_servico()

                print("\n--- Quantidade de OS por Serviço ---")

                if not resultados:
                    print("Nenhum registro encontrado.")
                else:
                    for item in resultados:
                        print(
                            f"{item['nome_servico']}: "
                            f"{item['quantidade_os']} OS"
                        )

            case 2:
                resultados = repositorio.faturamento_por_servico()

                print("\n--- Faturamento por Serviço ---")

                if not resultados:
                    print("Nenhum registro encontrado.")
                else:
                    for item in resultados:
                        print(f"\nServiço: {item['nome_servico']}")
                        print(f"Quantidade de OS: {item['quantidade_os']}")
                        print(f"Faturamento: R$ {item['faturamento_total']:.2f}")
                        print(f"Valor médio: R$ {item['valor_medio']:.2f}")

            case 3:
                resultados = repositorio.quantidade_os_e_media_por_cliente()

                print("\n--- Quantidade de OS e Média por Cliente ---")

                if not resultados:
                    print("Nenhum registro encontrado.")
                else:
                    for item in resultados:
                        print(f"\nCliente: {item['nome']}")
                        print(f"Quantidade de OS: {item['quantidade_os']}")

                        if item['media_valor_gasto'] is not None:
                            print(f"Média de valor gasto: R$ {item['media_valor_gasto']:.2f}")
                        else:
                            print("Média de valor gasto: Sem ordens de serviço.")

            case 0:
                break
            case -1:
                print("Opção Inválida. Digite um número.")

            case _:
                print("Opção inválida! Tente novamente.")
