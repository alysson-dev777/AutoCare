from models.cliente import Cliente
from models.ordem_servico import OrdemServico
from models.servico import Servico
from repositories.cliente_database_repository import ClienteDatabaseRepository
from repositories.ordem_servico_database_repository import OrdemServicoDatabaseRepository
from repositories.servico_database_repository import ServicoDatabaseRepository

def exibir_menu():
    print("------------ AutoCare ------------")
    print("[1] - Gerenciar Clientes")
    print("[2] - Gerenciar Serviços")
    print("[3] - Gerenciar Ordens de Serviços")
    print("[0] - Sair")
    print("----------------------------------")

def cadastrar_cliente():
    print("\n---------- Cadastro de Cliente ----------")

    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

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
        print("\nCliente cadastrado com suceeso!")
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

    id_cliente = int(input("Informe o ID do cliente que deseja buscar: "))

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

    id_cliente = int(input("Informe o ID do cliente que deseja editar: "))

    cliente = repositorio.find_by_id(id_cliente)

    if cliente is not None:
        print("\nPressione ENTER para manter o valor atual.")

        nome = input(f"Nome ({cliente.nome}): ")
        cpf = input(f"CPF ({cliente.cpf}): ")
        telefone = input(f"Telefone ({cliente.telefone}): ")
        email = input(f"Email ({cliente.email}): ")

        if nome == "":
            nome = cliente.nome
        if cpf == "":
            cpf = cliente.cpf
        if telefone == "":
            telefone = cliente.telefone
        if email == "":
            email = cliente.email

        cliente_atualizado = Cliente(
            cliente.id_cliente,
            nome,
            cpf,
            telefone,
            email
        )

        resultado = repositorio.update(cliente_atualizado)

        if resultado:
            print("----------------------------------")
            print("Cliente atualizado com sucesso!")
            print("----------------------------------")
        else:
            print("----------------------------------")
            print("Erro ao atualizar cliente.")
            print("----------------------------------")
    else:
        print("----------------------------------")
        print("Cliente não encontrado.")
        print("----------------------------------")

def excluir_cliente():
    repositorio = ClienteDatabaseRepository()

    id_cliente = int(input("Informe o ID do cliente que deseja excluir: "))

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

    nome_servico = input("Nome do serviço: ")
    descricao = input("Descrição do serviço: ")
    preco_padrao = float(input("Preço padrão do serviço: R$"))

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

    id_servico = int(input("Informe o ID do serviço que deseja buscar: "))

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
    
    id_servico = int(input("Informe o ID do serviço que deseja editar: "))
    
    servico = repositorio.find_by_id(id_servico)
    
    if servico is not None:
        print("\nPressione ENTER para manter o valor atual.")
    
        nome_servico = input(f"Nome ({servico.nome_servico}): ")
        descricao = input(f"Descrição ({servico.descricao}): ")
        preco_padrao = input(f"Preço Padrão (R${servico.preco_padrao}): ")
    
        if nome_servico == "":
            nome_servico = servico.nome_servico
        if descricao == "":
            descricao = servico.descricao
        if preco_padrao == "":
            preco_padrao = servico.preco_padrao
        else:
            preco_padrao = float(preco_padrao)
    
        servico_atualizado = Servico(
            servico.id_servico,
            nome_servico,
            descricao,
            preco_padrao
            )
    
        resultado = repositorio.update(servico_atualizado)
    
        if resultado:
            print("----------------------------------")
            print("Serviço atualizado com sucesso!")
            print("----------------------------------")
        else:
            print("----------------------------------")
            print("Erro ao atualizar serviço.")
            print("----------------------------------")
    else:
        print("----------------------------------")
        print("Serviço não encontrado.")
        print("----------------------------------")

def excluir_servico():
    repositorio = ServicoDatabaseRepository()

    id_servico = int(input("Informe o ID do serviço que deseja excluir: "))

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

    id_cliente = int(input("ID do cliente: "))
    id_servico = int(input("ID do serviço: "))
    data_abertura = input("Data abertura (AAAA-MM-DD): ")
    valor_cobrado = float(input("Valor cobrado: R$"))
    status = input("Status da OS: ")

    ordem_servico = OrdemServico(
        None,
        id_cliente,
        id_servico,
        data_abertura,
        valor_cobrado,
        status
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

    id_os = int(input("Informe o ID da Ordem de Serviço que deseja buscar: "))

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

    id_os = int(input("Informe o ID da Ordem de Serviço que deseja editar: "))

    ordem = repositorio.find_by_id(id_os)

    if ordem is not None:
        print("\nPressione ENTER para manter o valor atual.")

        id_cliente = input(f"ID do Cliente ({ordem.id_cliente}): ")
        id_servico = input(f"ID do Serviço ({ordem.id_servico}): ")
        data_abertura = input(f"Data de Abertura ({ordem.data_abertura}): ")
        valor_cobrado = input(f"Valor Cobrado ({ordem.valor_cobrado}): ")
        status = input(f"Status ({ordem.status}): ")

        if id_cliente == "":
            id_cliente = ordem.id_cliente
        else:
            id_cliente = int(id_cliente)

        if id_servico == "":
            id_servico = ordem.id_servico
        else:
            id_servico = int(id_servico)

        if data_abertura == "":
            data_abertura = ordem.data_abertura

        if valor_cobrado == "":
            valor_cobrado = ordem.valor_cobrado
        else:
            valor_cobrado = float(valor_cobrado)

        if status == "":
            status = ordem.status

        ordem_atualizada = OrdemServico(
            ordem.id_os,
            id_cliente,
            id_servico,
            data_abertura,
            valor_cobrado,
            status
        )

        resultado = repositorio.update(ordem_atualizada)

        if resultado:
            print("----------------------------------------")
            print("Ordem de Serviço atualizada com sucesso!")
            print("----------------------------------------")
        else:
            print("-----------------------------------")
            print("Erro ao atualizar Ordem de Serviço.")
            print("-----------------------------------")
    else:
        print("----------------------------------")
        print("Ordem de Serviço não encontrada.")
        print("----------------------------------")


def excluir_ordem_servico():
    repositorio = OrdemServicoDatabaseRepository()

    id_os = int(input("Informe o ID da Ordem de Serviço que deseja excluir: "))

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

        opcao = int(input(">>> "))

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

        opcao = int(input(">>> "))

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
            case _:
                print("Opção Inválida! Tente novamente.")

def menu_ordem_servico():
    while True:

        print("\n------ Ordens de Serviços ------")
        print("[1] - Cadastrar Ordem de Serviço")
        print("[2] - Listar Ordens de Serviço")
        print("[3] - Buscar Ordem de Serviço por ID")
        print("[4] - Atualizar Ordem de Serviço")
        print("[5] - Excluir Ordem deServiço")
        print("[0] - Voltar")
        print("----------------------------------")

        opcao = int(input(">>> "))

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
            case _:
                print("Opção Inválida! Tente novamente.")