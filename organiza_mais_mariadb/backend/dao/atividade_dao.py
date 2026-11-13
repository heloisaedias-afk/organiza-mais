from backend.config.conexao import conectar
class AtividadeDAO:
    @staticmethod
    def listar(status=None):
        c=conectar(); q=c.cursor(dictionary=True)
        try:
            sql="""SELECT a.id_atividade,a.titulo,a.descricao,a.tipo,
                   DATE_FORMAT(a.data_entrega,'%Y-%m-%d') AS data_entrega,
                   a.status,a.id_materia,m.nome_materia
                   FROM atividade a JOIN materia m ON m.id_materia=a.id_materia"""
            if status in ("Pendente","Concluída"):
                q.execute(sql+" WHERE a.status=%s ORDER BY a.data_entrega",(status,))
            else: q.execute(sql+" ORDER BY a.data_entrega")
            return q.fetchall()
        finally: q.close(); c.close()
    @staticmethod
    def inserir(a):
        c=conectar(); q=c.cursor()
        try:
            q.execute("""INSERT INTO atividade(titulo,descricao,tipo,data_entrega,status,id_materia)
                         VALUES(%s,%s,%s,%s,%s,%s)""",
                      (a.titulo,a.descricao,a.tipo,a.data_entrega,a.status,a.id_materia))
            c.commit(); return q.lastrowid
        finally: q.close(); c.close()
    @staticmethod
    def atualizar(id,a):
        c=conectar(); q=c.cursor()
        try:
            q.execute("""UPDATE atividade SET titulo=%s,descricao=%s,tipo=%s,data_entrega=%s,
                         status=%s,id_materia=%s WHERE id_atividade=%s""",
                      (a.titulo,a.descricao,a.tipo,a.data_entrega,a.status,a.id_materia,id))
            c.commit(); return q.rowcount
        finally: q.close(); c.close()
    @staticmethod
    def status(id,status):
        c=conectar(); q=c.cursor()
        try: q.execute("UPDATE atividade SET status=%s WHERE id_atividade=%s",(status,id)); c.commit(); return q.rowcount
        finally: q.close(); c.close()
    @staticmethod
    def excluir(id):
        c=conectar(); q=c.cursor()
        try: q.execute("DELETE FROM atividade WHERE id_atividade=%s",(id,)); c.commit(); return q.rowcount
        finally: q.close(); c.close()
