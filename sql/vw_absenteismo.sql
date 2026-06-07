CREATE VIEW vw_absenteismo AS
SELECT
    c.id_colaborador,
    c.matricula,
    c.nome,
    c.sexo,

    EXTRACT(
        YEAR FROM AGE(CURRENT_DATE, c.data_nascimento)
    ) AS idade,

    CASE
        WHEN EXTRACT(YEAR FROM AGE(CURRENT_DATE, c.data_nascimento))
            BETWEEN 18 AND 24 THEN '18-24'
        WHEN EXTRACT(YEAR FROM AGE(CURRENT_DATE, c.data_nascimento))
            BETWEEN 25 AND 34 THEN '25-34'
        WHEN EXTRACT(YEAR FROM AGE(CURRENT_DATE, c.data_nascimento))
            BETWEEN 35 AND 44 THEN '35-44'
        WHEN EXTRACT(YEAR FROM AGE(CURRENT_DATE, c.data_nascimento))
            BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55+'
    END AS faixa_etaria,

    c.area,
    c.cargo,
    c.gestor,
    c.data_admissao,
    c.status,

    a.id_ausencia,
    a.data_inicio,
    a.data_fim,
    a.dias_afastamento,
    a.horas_perdidas,
    a.tipo_ausencia,
    a.cid

FROM colaboradores c
INNER JOIN ausencias a
    ON c.id_colaborador = a.id_colaborador;

SELECT COUNT(*)
FROM vw_absenteismo;

SELECT *
FROM vw_absenteismo
LIMIT 5;
