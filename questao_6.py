# %%
import os
import psycopg
from datetime import date
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# Configuração do banco de dados para conexão
DB_CONFIG = {
    "dbname": DB_NAME,
    "user": DB_USER,
    "password": DB_PASSWORD,
    "host": DB_HOST,
    "port": DB_PORT,
}

connection = psycopg.connect(**DB_CONFIG)

query = """
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
ORDER BY m.month;
"""

cursor = connection.cursor()

cursor.execute(query)

result = cursor.fetchall()

connection.close()

monthly_sales = {
    month: units
    for month, units in result
}


"""
=============================================================================
Separar dados de treino e de teste conforme delimitado pelo tech lead
=============================================================================
"""
train = {
    month: units
    for month, units in monthly_sales.items()
    if month <= date(2025, 12, 1)
}

test = {
    month: units
    for month, units in monthly_sales.items()
    if date(2026, 1, 1) <= month <= date(2026, 3, 1)
}


"""
=============================================================================
Modelo Walk-forward
=============================================================================
"""
# Abordagem considerando que as compras com os fornecedores acontece mês a mês.
# Portanto, utilizamos dados reais do mês anterior para o cálculo da média móvel. 
history = dict(train)
walk_forward_forecasts = {}

for month in sorted(test):
    previous_months = sorted(history)[-3:]

    forecast = sum(
        history[m] for m in previous_months
    ) / 3

    walk_forward_forecasts[month] = forecast

    # Após prever o mês, seu valor real passa a fazer parte do histórico
    history[month] = test[month]


# Cálculo do Mean Absolute Error para avaliação do modelo
def mae(actual, predicted):
    errors = [
        abs(actual[month] - predicted[month])
        for month in actual
    ]
    
    return sum(errors) / len(errors)

mae_walk_forward = mae(test, walk_forward_forecasts)
print(mae_walk_forward)