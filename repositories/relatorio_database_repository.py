from database.connection import conectar


class RelatorioDatabaseRepository:

    def quantidade_os_por_servico(self):
        conexao = conectar()

        if conexao is None:
            return []

        try:
            cursor = conexao.cursor(dictionary=True)

            sql = """
                SELECT
                    s.nome_servico,
                    COUNT(os.id_os) AS quantidade_os
                FROM ordem_servico os
                INNER JOIN servico s
                    ON os.id_servico = s.id_servico
                GROUP BY s.id_servico, s.nome_servico
                ORDER BY quantidade_os DESC
            """

            cursor.execute(sql)
            return cursor.fetchall()

        finally:
            cursor.close()
            conexao.close()

    def faturamento_por_servico(self):
        conexao = conectar()

        if conexao is None:
            return []

        try:
            cursor = conexao.cursor(dictionary=True)

            sql = """
                SELECT
                    s.nome_servico,
                    COUNT(os.id_os) AS quantidade_os,
                    SUM(os.valor_cobrado) AS faturamento_total,
                    AVG(os.valor_cobrado) AS valor_medio
                FROM ordem_servico os
                INNER JOIN servico s
                    ON os.id_servico = s.id_servico
                GROUP BY s.id_servico, s.nome_servico
                ORDER BY faturamento_total DESC
            """

            cursor.execute(sql)
            return cursor.fetchall()

        finally:
            cursor.close()
            conexao.close()
    def quantidade_os_e_media_por_cliente(self):
        conexao = conectar()

        if conexao is None:
            return []

        try:
            cursor = conexao.cursor(dictionary=True)

            sql = """
                SELECT
                    c.nome,
                    COUNT(os.id_os) AS quantidade_os,
                    AVG(os.valor_cobrado) AS media_valor_gasto
                FROM cliente c
                LEFT JOIN ordem_servico os
                    ON c.id_cliente = os.id_cliente
                GROUP BY c.id_cliente, c.nome
                ORDER BY quantidade_os DESC
            """

            cursor.execute(sql)
            return cursor.fetchall()

        finally:
            cursor.close()
            conexao.close()