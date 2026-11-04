from database.connection import conectar
from models.cliente import Cliente

class ClienteDatabaseRepository:
    def save(self, cliente):
        conexão = conectar()

        if conexão is None:
           return False

        try:
            cursor = conexão.cursor()

            sql = """
                Insert into cliente (nome, cpf, telefone, email) values
                (%s, %s, %s, %s)
                """
            valores = (
                cliente.nome,
                cliente.cpf,
                cliente.telefone,
                cliente.email
            )

            cursor.execute(sql, valores)
            conexão.commit()

            cliente.id_cliente = cursor.lastrowid

            return True
        except Exception as erro:
            conexão.rollback()
            print(f"Erro ao cadastrar cliente: {erro}")
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

            sql = "Select * from cliente"

            cursor.execute(sql)

            registros = cursor.fetchall()

            clientes = []

            for registro in registros:
                cliente = Cliente(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3],
                    registro[4]
                )

                clientes.append(cliente)

            return clientes
        
        except Exception as erro:
            print(f"Erro ao consultar clientes: {erro}")
            return []
        
        finally:
            cursor.close()
            conexão.close()

    def find_by_id(self, id_cliente):
        conexão = conectar()

        if conexão is None:
            return None

        try:
            cursor = conexão.cursor()

            sql = """
                Select * from cliente
                where id_cliente = %s
            """
            cursor.execute(sql, (id_cliente,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            cliente = Cliente(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4]
            )
            return cliente

        except Exception as erro:
            print(f"Erro ao buscar cliente: {erro}")
            return None

        finally:
            cursor.close()
            conexão.close()

    def update(self, cliente):
        conexão = conectar()

        if conexão is None:
            return False

        try:
            cursor = conexão.cursor()

            sql = """
                Update cliente
                set nome = %s, cpf = %s, telefone = %s, email = %s
                where id_cliente = %s
            """
            valores = (
                cliente.nome,
                cliente.cpf,
                cliente.telefone,
                cliente. email,
                cliente.id_cliente
            )
            cursor.execute(sql, valores)
            conexão.commit()

            return cursor.rowcount > 0
        
        except Exception as erro:
            conexão.rollback()
            print(f"Erro ao atualizar cliente: {erro}")
            return False
        
        finally:
            cursor.close()
            conexão.close()

    def delete(self, id_cliente):
        conexão = conectar()

        if conexão is None:
            return False

        try:
            cursor = conexão.cursor()

            sql = """
                Delete from cliente
                where id_cliente = %s
            """

            cursor.execute (sql, (id_cliente,))
            conexão.commit()

            return cursor.rowcount > 0
        
        except Exception as erro:
            conexão.rollback()
            print(f"Erro ao deletar cliente: {erro}")
            return False

        finally:
            cursor.close()
            conexão.close()