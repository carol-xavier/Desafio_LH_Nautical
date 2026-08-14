-- Não há formação de zeros artificiais com MIN(created_at) em generate_series, 
--pois a primeira venda de bussola foi em janeiro de 2020
WITH monthly_calendar AS (
    SELECT
    generate_series(
        DATE_TRUNC('month', MIN(created_at)),
        DATE '2026-03-01',
        INTERVAL '1 month'
    )::date AS month
FROM orders
),

bussola_sales AS (
    SELECT
        DATE_TRUNC('month', o.created_at)::date AS month,
        SUM(oi.quantity) AS units_sold
    FROM orders o
    JOIN order_items oi
        ON o.id = oi.order_id
    JOIN product_variants pv
        ON oi.product_variant_id = pv.id
    JOIN products p
        ON pv.product_id = p.id
    WHERE p.name = 'Bússola de Bordo 702'
    GROUP BY 1
)

SELECT 
    m.month,
    COALESCE(b.units_sold, 0) AS units_sold
FROM monthly_calendar m
    LEFT JOIN bussola_sales b
    ON m.month = b.month
ORDER BY m.month DESC;