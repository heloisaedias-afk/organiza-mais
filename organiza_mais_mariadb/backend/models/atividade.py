class Atividade:
    def __init__(self, dados):
        self.titulo = (dados.get("titulo") or "").strip()
        self.descricao = (dados.get("descricao") or "").strip()
        self.tipo = dados.get("tipo")
        self.data_entrega = dados.get("data_entrega")
        self.status = dados.get("status") or "Pendente"
        self.id_materia = dados.get("id_materia")
    def validar(self):
        if not self.titulo or len(self.titulo) > 100: raise ValueError("Título obrigatório (até 100 caracteres).")
        if not self.descricao: raise ValueError("Descrição obrigatória.")
        if self.tipo not in ("Tarefa", "Trabalho", "Prova"): raise ValueError("Tipo inválido.")
        if not self.data_entrega: raise ValueError("Informe a data de entrega.")
        if not self.id_materia: raise ValueError("Selecione uma matéria.")
        if self.status not in ("Pendente", "Concluída"): raise ValueError("Status inválido.")
