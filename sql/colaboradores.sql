CREATE TABLE colaboradores (
    id_colaborador SERIAL PRIMARY KEY,
    matricula VARCHAR(20) UNIQUE,
    nome VARCHAR(100) NOT NULL,
    sexo VARCHAR(20),
    data_nascimento DATE,
    area VARCHAR(50),
    cargo VARCHAR(50),
    gestor VARCHAR(100),
    data_admissao DATE,
    status VARCHAR(20)
);

SELECT COUNT(*)
FROM colaboradores;