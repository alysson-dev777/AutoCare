from repositories.ordem_servico_database_repository import OrdemServicoDatabaseRepository
from repositories.cliente_database_repository import ClienteDatabaseRepository
from repositories.servico_database_repository import ServicoDatabaseRepository
from models.ordem_servico import OrdemServico
from validators import (
    validar_preco,
    validar_status,
    pode_alterar_ordem_servico
)

def testar_cadastro_ordem_servico():
    repositorio = OrdemServicoDatabaseRepository()

    clientes = ClienteDatabaseRepository().get_all()
    servicos = ServicoDatabaseRepository().get_all()

    assert clientes, "Não existem clientes cadastrados para o teste."
    assert servicos, "Não existem serviços cadastrados para o teste."

    id_cliente = clientes[0].id_cliente
    id_servico = servicos[0].id_servico

    quantidade_antes = len(repositorio.get_all())

    ordem = OrdemServico(
        None,
        id_cliente,
        id_servico,
        None,
        100.00,
        "Aberta"
    )

    try:
        resultado = repositorio.save(ordem)

        assert resultado is True, "O cadastro da OS falhou."
        assert ordem.id_os is not None, "A OS não recebeu um ID."
        
        quantidade_depois = len(repositorio.get_all())

        assert quantidade_depois == quantidade_antes + 1, (
            "A quantidade de ordens não aumentou corretamente."
        )

        print("Teste de caminho feliz: APROVADO!")

    finally:
        if ordem.id_os is not None:
            repositorio.delete(ordem.id_os)

def testar_integridade_referencial():
    repositorio = OrdemServicoDatabaseRepository()
    servicos = ServicoDatabaseRepository().get_all()

    assert servicos, "Não existem serviços cadastrados para o teste."

    id_servico = servicos[0].id_servico

    ordem = OrdemServico(
        None,
        999999,
        id_servico,
        None,
        100.00,
        "Aberta"
    )

    resultado = repositorio.save(ordem)

    assert resultado is False, (
        "O sistema permitiu cadastrar uma OS com cliente inexistente."
    )

    print("Teste de integridade referencial: APROVADO!")


def testar_valor_limite():
    assert validar_preco(-10.00) is False, (
        "O sistema aceitou um valor negativo."
    )

    assert validar_preco(0.00) is True, (
        "O sistema rejeitou o valor zero."
    )

    assert validar_preco(100.00) is True, (
        "O sistema rejeitou um valor positivo."
    )

    print("Teste de valor limite: APROVADO!")

def testar_regra_de_dominio():
    assert validar_status("Aberta") is True
    assert validar_status("Em Andamento") is True
    assert validar_status("Concluída") is True

    assert validar_status("Cancelada") is False

    ordem_concluida = OrdemServico(
        1, 1, 1, None, 100.00, "Concluída"
    )

    ordem_aberta = OrdemServico(
        2, 1, 1, None, 100.00, "Aberta"
    )

    assert pode_alterar_ordem_servico(ordem_concluida) is False
    assert pode_alterar_ordem_servico(ordem_aberta) is True

    print("Teste de regra de domínio: APROVADO!")

if __name__ == "__main__":
    testar_cadastro_ordem_servico()
    testar_integridade_referencial()
    testar_valor_limite()
    testar_regra_de_dominio()