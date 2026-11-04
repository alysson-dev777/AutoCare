from database.connection import conectar
from models.servico import Servico

class ServicoDatabaseRepository:
    def save(self, servico):
        conexão = conectar()
    
        if conexão is None:
            return False
    
        try:
            cursor = conexão.cursor()
    
            sql = """
                Insert into servico (nome_servico, descricao, preco_padrao) values
                (%s, %s, %s)
            """
            valores = (
                servico.nome_servico,
                servico.descricao,
                servico.preco_padrao
            )
    
            cursor.execute(sql, valores)
            conexão.commit()
    
            servico.id_servico = cursor.lastrowid
    
            return True
        except Exception as erro:
            conexão.rollback()
            print(f"Erro ao cadastrar serviço: {erro}")
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

            sql = "Select * from servico"

            cursor.execute(sql)

            registros = cursor.fetchall()

            servicos = []

            for registro in registros:
                servico = Servico(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3]
                )

                servicos.append(servico)

            return servicos
        except Exception as erro:
            print(f"Erro ao consultar serviço: {erro}")
            return []

        finally:
            cursor.close()
            conexão.close()

    def find_by_id(self, id_servico):
        conexão = conectar()

        if conexão is None:
            return None

        try:
            cursor = conexão.cursor()

            sql = """
                Select * from servico
                where id_servico = %s
            """
            cursor.execute(sql, (id_servico,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            servico = Servico(
                registro[0],
                registro[1],
                registro[2],
                registro[3]
            )
            return servico

        except Exception as erro:
            print(f"Erro ao buscar serviço: {erro}")
            return None

        finally:
            cursor.close()
            conexão.close()

    def update(self, servico):
        conexão = conectar()

        if conexão is None:
            return False

        try:
            cursor = conexão.cursor()

            sql = """
                Update servico
                set nome_servico = %s, descricao = %s, preco_padrao = %s
                where id_servico = %s
            """
            valores = (
                servico.nome_servico,
                servico.descricao,
                servico.preco_padrao,
                servico.id_servico
            )
            cursor.execute(sql, valores)
            conexão.commit()

            return cursor.rowcount > 0

        except Exception as erro:
            conexão.rollback()
            print(f"Erro ao atualizar serviço: {erro}")
            return False

        finally:
            cursor.close()
            conexão.close()

    def delete(self, id_servico):
        conexão = conectar()

        if conexão is None:
            return False

        try:
            cursor = conexão.cursor()

            sql = """
                Delete from servico
                where id_servico = %s
            """
            cursor.execute(sql)
            conexão.commit()

            return cursor.rowcount > 0

        except Exception as erro:
            conexão.rollback()
            print(f"Erro ao deletar serviço: {erro}")
            return False

        finally:
            cursor.close()
            conexão.close()

            