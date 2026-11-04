from database.connection import conectar
from models.ordem_servico import OrdemServico

class OrdemServicoDatabaseRepository:
    def save(self, ordem_servico):
        conexão = conectar()

        if conexão is None:
            return False

        try:
            cursor = conexão.cursor()

            sql = """
                Insert into ordem_servico (
                    id_cliente, 
                    id_servico, 
                    data_abertura, 
                    valor_cobrado, 
                    status
                )
                values (%s, %s, %s, %s, %s)
            """

            valores = (
                ordem_servico.id_cliente,
                ordem_servico.id_servico,
                ordem_servico.data_abertura,
                ordem_servico.valor_cobrado,
                ordem_servico.status
            )

            cursor.execute(sql, valores)
            conexão.commit()

            ordem_servico.id_os = cursor.lastrowid

            return True

        except Exception as erro:
            conexão.rollback()
            print(f"Erro ao cadastrar ordem de serviço: {erro}")
            return False

        finally:
            cursor.close()
            conexão.close()

    def get_all(self):
        conexão = conectar()

        if conexão is None:
            return []

        try:
            cursor = conexão.cursor()

            sql = "Select * from ordem_servico"

            cursor.execute(sql)

            registros = cursor.fetchall()

            ordens_servico = []

            for registro in registros:
                ordem_servico = OrdemServico(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3],
                    registro[4],
                    registro[5]
                )

                ordens_servico.append(ordem_servico)

            return ordens_servico

        except Exception as erro:
            print(f"Erro ao consultar ordens de serviço: {erro}")
            return []

        finally:
            cursor.close()
            conexão.close()

    def find_by_id(self, id_os):
        conexão = conectar()

        if conexão is None:
            return None

        try:
            cursor = conexão.cursor()

            sql = """
                Select * from ordem_servico
                where id_os = %s
            """
            cursor.execute(sql, (id_os,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            ordem_servico = OrdemServico(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4],
                registro[5]
            )
            return ordem_servico

        except Exception as erro:
            print(f"Erro ao buscar ordem de serviço: {erro}")
            return None

        finally:
            cursor.close()
            conexão.close()
    
    def update(self, ordem_servico):
        conexão = conectar()

        if conexão is None:
            return False

        try:
            cursor = conexão.cursor()

            sql = """
                Update ordem_servico
                set id_cliente = %s,
                    id_servico = %s, 
                    data_abertura = %s, 
                    valor_cobrado = %s, 
                    status = %s
                where id_os = %s
            """
            valores = (
                ordem_servico.id_cliente,
                ordem_servico.id_servico,
                ordem_servico.data_abertura,
                ordem_servico.valor_cobrado,
                ordem_servico.status,
                ordem_servico.id_os
            )
            cursor.execute(sql, valores)
            conexão.commit()

            return cursor.rowcount > 0
        except Exception as erro:
            conexão.rollback()
            print(f"Erro ao atualizar ordem de serviço: {erro}")
            return False

        finally:
            cursor.close()
            conexão.close()

    def delete(self, id_os):
        conexão = conectar()

        if conexão is None:
            return False

        try:
            cursor = conexão.cursor()

            sql = """
                Delete from ordem_servico
                where id_os = %s
            """

            cursor.execute(sql, (id_os,))
            conexão.commit()

            return cursor.rowcount > 0

        except Exception as erro:
            conexão.rollback()
            print(f"Erro ao excluir ordem de serviço: {erro}")
            return False

        finally:
            cursor.close()
            conexão.close()