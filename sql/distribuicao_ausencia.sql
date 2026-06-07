SELECT
    cid,
    COUNT(*) AS ocorrencias
FROM ausencias
GROUP BY cid
ORDER BY ocorrencias DESC;