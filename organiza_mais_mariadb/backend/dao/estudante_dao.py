from backend.config.conexao import conectar
class EstudanteDAO:
    @staticmethod
    def listar():
        c=conectar(); q=c.cursor(dictionary=True)
        try:
            q.execute("SELECT id_estudante,nome FROM estudante ORDER BY nome")
            return q.fetchall()
        finally: q.close(); c.close()
    @staticmethod
    def inserir(nome):
        c=conectar(); q=c.cursor()
        try:
            q.execute("INSERT INTO estudante(nome) VALUES(%s)",(nome,)); c.commit()
            return q.lastrowid
        finally: q.close(); c.close()
