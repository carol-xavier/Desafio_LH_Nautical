SELECT DISTINCT
    o.customer_id,
    p.id AS product_id,
    p.name AS product_name
FROM orders o
JOIN order_items oi
    ON o.id = oi.order_id
JOIN product_variants pv
    ON oi.product_variant_id = pv.id
JOIN products p
    ON pv.product_id = p.id
WHERE o.customer_id IS NOT NULL;