CREATE TABLE ausencias (
    id_ausencia SERIAL PRIMARY KEY,
    id_colaborador INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    dias_afastamento INT NOT NULL,
    horas_perdidas NUMERIC(10,2) NOT NULL,
    tipo_ausencia VARCHAR(50),
    cid VARCHAR(20),

    CONSTRAINT fk_colaborador
        FOREIGN KEY (id_colaborador)
        REFERENCES colaboradores(id_colaborador)
);

SELECT
    COUNT(*) AS total_ausencias,
    COUNT(DISTINCT id_colaborador) AS colaboradores_com_ausencia
FROM ausencias;