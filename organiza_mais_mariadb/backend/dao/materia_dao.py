from backend.config.conexao import conectar
class MateriaDAO:
    @staticmethod
    def listar():
        c=conectar(); q=c.cursor(dictionary=True)
        try:
            q.execute("""SELECT m.id_materia,m.nome_materia,m.id_estudante,e.nome AS nome_estudante
                         FROM materia m JOIN estudante e ON e.id_estudante=m.id_estudante
                         ORDER BY m.nome_materia""")
            return q.fetchall()
        finally: q.close(); c.close()
    @staticmethod
    def inserir(nome,id_estudante):
        c=conectar(); q=c.cursor()
        try:
            q.execute("INSERT INTO materia(nome_materia,id_estudante) VALUES(%s,%s)",(nome,id_estudante))
            c.commit(); return q.lastrowid
        finally: q.close(); c.close()
    @staticmethod
    def excluir(id):
        c=conectar(); q=c.cursor()
        try: q.execute("DELETE FROM materia WHERE id_materia=%s",(id,)); c.commit(); return q.rowcount
        finally: q.close(); c.close()
