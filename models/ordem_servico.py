class OrdemServico:
    def __init__(self, id_os, id_cliente, id_servico, data_abertura, valor_cobrado, status):
        self.id_os = id_os
        self.id_cliente = id_cliente
        self.id_servico = id_servico
        self.data_abertura = data_abertura
        self.valor_cobrado = valor_cobrado
        self.status = status
    