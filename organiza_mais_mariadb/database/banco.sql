CREATE DATABASE IF NOT EXISTS organiza_mais CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE organiza_mais;
CREATE TABLE IF NOT EXISTS estudante (
 id_estudante INT(11) NOT NULL AUTO_INCREMENT, nome VARCHAR(100) NOT NULL,
 PRIMARY KEY(id_estudante)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
CREATE TABLE IF NOT EXISTS materia (
 id_materia INT(11) NOT NULL AUTO_INCREMENT, nome_materia VARCHAR(100) NOT NULL,
 id_estudante INT(11) NOT NULL, PRIMARY KEY(id_materia), KEY id_estudante(id_estudante),
 CONSTRAINT materia_ibfk_1 FOREIGN KEY(id_estudante) REFERENCES estudante(id_estudante)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
CREATE TABLE IF NOT EXISTS atividade (
 id_atividade INT(11) NOT NULL AUTO_INCREMENT, titulo VARCHAR(100) NOT NULL,
 descricao TEXT NOT NULL, tipo VARCHAR(30) NOT NULL, data_entrega DATE NOT NULL,
 status VARCHAR(20) NOT NULL DEFAULT 'Pendente', id_materia INT(11) NOT NULL,
 PRIMARY KEY(id_atividade), KEY id_materia(id_materia),
 CONSTRAINT atividade_ibfk_1 FOREIGN KEY(id_materia) REFERENCES materia(id_materia)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
