# Organiza+ — MariaDB/XAMPP

Projeto com Python POO, Flask, HTML, CSS, JavaScript e MariaDB/MySQL.

## Banco
O código usa exatamente as tabelas `estudante`, `materia` e `atividade`, e os campos do SQL enviado. Se o banco `organiza_mais` já existe no phpMyAdmin, não importe o SQL novamente; `database/banco.sql` é apenas uma referência para recriar o banco.

## Conexão XAMPP
Em `backend/config/conexao.py`, o padrão é host `localhost`, porta `3306`, usuário `root`, senha vazia e banco `organiza_mais`. Altere se seu XAMPP usar outra configuração.

## Executar no Windows
1. Inicie Apache e MySQL no XAMPP.
2. Abra a pasta raiz no VS Code.
3. No terminal:
   `py -m venv .venv`
   `.\.venv\Scripts\Activate.ps1`
   `pip install -r requirements.txt`
   `python backend/app.py`
4. Abra `frontend/index.html` com Live Server.
5. Teste `http://127.0.0.1:5000/api/health`.

Cadastre na ordem: estudante → matéria → atividade.

## Rotas
- GET/POST `/api/estudantes`
- GET/POST/DELETE `/api/materias`
- GET/POST/PUT/DELETE `/api/atividades`
- PATCH `/api/atividades/<id>/status`

A chave estrangeira impede excluir uma matéria que ainda tenha atividades vinculadas.
