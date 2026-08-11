-- Questão 1.1: Agregações básicas na tabela "orders"

SELECT
    COUNT(*) AS total_rows,
    MIN(created_at) AS min_created_at,
    MAX(created_at) AS max_created_at,
    MIN(total) AS min_total,
    MAX(total) AS max_total,
    AVG(total) AS avg_total
FROM orders;