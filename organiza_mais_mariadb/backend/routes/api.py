from flask import Blueprint,request,jsonify
from mysql.connector import Error
from backend.models.estudante import Estudante
from backend.models.materia import Materia
from backend.models.atividade import Atividade
from backend.dao.estudante_dao import EstudanteDAO
from backend.dao.materia_dao import MateriaDAO
from backend.dao.atividade_dao import AtividadeDAO
api=Blueprint("api",__name__)

@api.get("/api/estudantes")
def estudantes_listar():
    try: return jsonify(EstudanteDAO.listar())
    except Exception as e: return jsonify(erro=str(e)),500

@api.post("/api/estudantes")
def estudantes_criar():
    try:
        e=Estudante((request.get_json() or {}).get("nome")); e.validar()
        return jsonify(id_estudante=EstudanteDAO.inserir(e.nome)),201
    except ValueError as e: return jsonify(erro=str(e)),400
    except Exception as e: return jsonify(erro=str(e)),500

@api.get("/api/materias")
def materias_listar():
    try: return jsonify(MateriaDAO.listar())
    except Exception as e: return jsonify(erro=str(e)),500

@api.post("/api/materias")
def materias_criar():
    try:
        d=request.get_json() or {}; m=Materia(d.get("nome_materia"),d.get("id_estudante")); m.validar()
        return jsonify(id_materia=MateriaDAO.inserir(m.nome_materia,m.id_estudante)),201
    except ValueError as e: return jsonify(erro=str(e)),400
    except Exception as e: return jsonify(erro=str(e)),500

@api.delete("/api/materias/<int:id>")
def materias_excluir(id):
    try:
        if not MateriaDAO.excluir(id): return jsonify(erro="Matéria não encontrada."),404
        return jsonify(mensagem="Matéria excluída.")
    except Error: return jsonify(erro="Não exclua uma matéria que possua atividades vinculadas."),409

@api.get("/api/atividades")
def atividades_listar():
    try: return jsonify(AtividadeDAO.listar(request.args.get("status")))
    except Exception as e: return jsonify(erro=str(e)),500

@api.post("/api/atividades")
def atividades_criar():
    try:
        a=Atividade(request.get_json() or {}); a.validar()
        return jsonify(id_atividade=AtividadeDAO.inserir(a)),201
    except ValueError as e: return jsonify(erro=str(e)),400
    except Exception as e: return jsonify(erro=str(e)),500

@api.put("/api/atividades/<int:id>")
def atividades_editar(id):
    try:
        a=Atividade(request.get_json() or {}); a.validar()
        if not AtividadeDAO.atualizar(id,a): return jsonify(erro="Atividade não encontrada."),404
        return jsonify(mensagem="Atividade atualizada.")
    except ValueError as e: return jsonify(erro=str(e)),400
    except Exception as e: return jsonify(erro=str(e)),500

@api.patch("/api/atividades/<int:id>/status")
def atividades_status(id):
    status=(request.get_json() or {}).get("status")
    if status not in ("Pendente","Concluída"): return jsonify(erro="Status inválido."),400
    if not AtividadeDAO.status(id,status): return jsonify(erro="Atividade não encontrada."),404
    return jsonify(mensagem="Status atualizado.")

@api.delete("/api/atividades/<int:id>")
def atividades_excluir(id):
    if not AtividadeDAO.excluir(id): return jsonify(erro="Atividade não encontrada."),404
    return jsonify(mensagem="Atividade excluída.")
