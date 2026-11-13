import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost", port=3306, user="root",
        password="", database="organiza_mais"
    )
