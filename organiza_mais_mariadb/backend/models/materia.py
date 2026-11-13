class Materia:
    def __init__(self, nome_materia, id_estudante):
        self.nome_materia = (nome_materia or "").strip()
        self.id_estudante = id_estudante
    def validar(self):
        if not self.nome_materia or len(self.nome_materia) > 100:
            raise ValueError("Informe o nome da matéria (até 100 caracteres).")
        if not self.id_estudante:
            raise ValueError("Selecione um estudante.")
