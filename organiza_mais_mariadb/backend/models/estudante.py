class Estudante:
    def __init__(self, nome):
        self.nome = (nome or "").strip()
    def validar(self):
        if not self.nome or len(self.nome) > 100:
            raise ValueError("Informe um nome com até 100 caracteres.")
