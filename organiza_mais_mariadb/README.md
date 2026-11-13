# Organiza+ — Sistema de Organização Escolar

## 1. Sobre o projeto

O **Organiza+** é um sistema web desenvolvido com o objetivo de ajudar estudantes a organizar suas atividades escolares, trabalhos, provas e prazos de entrega.

A proposta surgiu da necessidade de facilitar a rotina dos estudantes, evitando esquecimentos e permitindo um melhor acompanhamento das tarefas.

## 2. Integrantes

- Ana Clara
- Heloisa Esther

**Turma:** 2TID

## 3. Objetivo

Desenvolver uma plataforma simples e intuitiva que permita cadastrar, organizar, editar e acompanhar atividades escolares, contribuindo para uma rotina de estudos mais organizada.

## 4. Público-alvo

Estudantes do Ensino Fundamental, Ensino Médio e Ensino Técnico que desejam melhorar sua organização escolar.

## 5. Funcionalidades

- Cadastro de estudantes.
- Cadastro de matérias.
- Cadastro de atividades escolares.
- Edição de atividades.
- Exclusão de atividades.
- Organização das atividades por matéria.
- Visualização das datas de entrega.
- Identificação de atividades pendentes e concluídas.
- Atualização do status das atividades.

## 6. Tecnologias utilizadas

### Front-end
- HTML5
- CSS3
- JavaScript

### Back-end
- Python
- Flask
- Programação Orientada a Objetos (POO)

### Banco de dados
- MariaDB / MySQL
- XAMPP
- phpMyAdmin

### Ferramentas
- Visual Studio Code
- Git
- GitHub

## 7. Estrutura do projeto

```text
organiza_mais/
│
├── backend/
│   ├── config/
│   ├── dao/
│   ├── models/
│   ├── routes/
│   └── app.py
│
├── frontend/
│   ├── css/
│   │   └── estilo.css
│   ├── js/
│   │   └── main.js
│   └── index.html
│
├── database/
│   └── banco.sql
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 8. Banco de dados

O sistema utiliza o banco de dados `organiza_mais`, composto por três tabelas principais:

- **estudante:** armazena os dados dos estudantes.
- **materia:** armazena as matérias relacionadas aos estudantes.
- **atividade:** armazena os títulos, descrições, tipos, datas de entrega e status das atividades.

As tabelas possuem relacionamentos por meio de chaves estrangeiras.

## 9. Como executar o projeto

### Pré-requisitos

- Python instalado.
- XAMPP instalado.
- Visual Studio Code.
- Navegador de internet.

### Passo 1 — Banco de dados

1. Abra o XAMPP.
2. Inicie o Apache e o MySQL.
3. Acesse o phpMyAdmin.
4. Crie ou selecione o banco `organiza_mais`.
5. Importe o arquivo `database/banco.sql`, caso as tabelas ainda não existam.

### Passo 2 — Instalar dependências

No terminal, dentro da pasta principal do projeto, execute:

```powershell
pip install -r requirements.txt
```

### Passo 3 — Iniciar o back-end

Execute:

```powershell
python -m backend.app
```

O servidor ficará disponível em:

```text
http://127.0.0.1:5000
```

### Passo 4 — Abrir o front-end

Abra o arquivo `frontend/index.html` utilizando o Live Server do Visual Studio Code.

## 10. Resultados esperados

Espera-se que o Organiza+ facilite a organização das atividades escolares, ajude os estudantes a acompanhar seus prazos e proporcione uma maneira prática de visualizar suas responsabilidades.

## 11. Considerações finais

O desenvolvimento do Organiza+ proporciona a aplicação prática dos conhecimentos de desenvolvimento web, banco de dados, Python, Flask e Programação Orientada a Objetos.

O projeto busca oferecer uma solução tecnológica para uma dificuldade comum na vida dos estudantes: a organização da rotina escolar.

