import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Gui20032007",
            database="autocare"
        )

        if conexao.is_connected():
            return conexao

    except Error as erro:
        print(f"Erro a conectar ao banco: {erro}")

    return None