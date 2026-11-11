def validar_cpf(cpf: str) -> bool:
    return len(cpf) == 11 and cpf.isdigit()

def validar_preco(preco) -> bool:
    try:
        valor = float(preco)
        return valor >= 0
    except (ValueError, TypeError):
        return False

def validar_email(email: str) -> bool:
    if "@" in email:
        dominio = email.split("@")[-1]
        if "." in dominio and len(dominio.replace(".", "")) > 0:
            return True
    return False

def validar_nome(nome: str) -> bool:
    tem_letra = any(char.isalpha() for char in nome)
    nao_tem_numero = not any(char.isdigit() for char in nome)
    return tem_letra and nao_tem_numero

def validar_telefone(telefone: str) -> bool:
    caracteres_permitidos = "0123456789()+- "

    if not all(char in caracteres_permitidos for char in telefone):
        return False

    quantidade_digitos = sum(char.isdigit() for char in telefone)

    return 10 <= quantidade_digitos <= 13

def validar_status(status: str) -> bool:
    status_permitidos = ["Aberta", "Em Andamento", "Concluída"]
    return status in status_permitidos


def pode_alterar_ordem_servico(ordem_servico) -> bool:
    return ordem_servico.status != "Concluída"