--Para este grupo específico de 10 clientes, identifique qual categoria de produto 
-- concentra a maior quantidade total de itens comprados (sum(quantity)).
WITH customer_metrics AS (
    SELECT
        customer_id,
        SUM(total) AS total_spent,
        COUNT(DISTINCT id) AS frequency,
        SUM(total) / COUNT(DISTINCT id) AS avg_ticket_customer
    FROM orders
    GROUP BY customer_id
),

customer_diversity AS (
    SELECT
        o.customer_id,
        COUNT(DISTINCT p.category_id) AS diversity_customer
    FROM orders o
        INNER JOIN order_items i
            ON i.order_id = o.id
        INNER JOIN product_variants v
            ON v.id = i.product_variant_id
        INNER JOIN products p
            ON p.id = v.product_id
    GROUP BY o.customer_id
),

top_customers AS (
    SELECT
        m.customer_id,
        m.avg_ticket_customer,
        d.diversity_customer
    FROM customer_metrics m
        INNER JOIN customer_diversity d
            ON d.customer_id = m.customer_id
    WHERE d.diversity_customer >= 13
    ORDER BY
        m.avg_ticket_customer DESC,
        m.customer_id ASC
    LIMIT 10
)

SELECT
    p.category_id,
    SUM(i.quantity) AS total_quantity
FROM top_customers t
    INNER JOIN orders o
        ON o.customer_id = t.customer_id
    INNER JOIN order_items i
        ON i.order_id = o.id
    INNER JOIN product_variants v
        ON v.id = i.product_variant_id
    INNER JOIN products p
        ON p.id = v.product_id
GROUP BY p.category_id
ORDER BY total_quantity DESC
LIMIT 1;