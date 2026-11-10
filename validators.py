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
    tem_numero = any(char.isdigit() for char in telefone)
    nao_tem_letra = not any(char.isalpha() for char in telefone)
    return tem_numero and nao_tem_letra
