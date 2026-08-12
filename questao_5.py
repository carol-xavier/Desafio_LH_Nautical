#%%
import os
import psycopg
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

# %%

connection = psycopg.connect(**DB_CONFIG)

query = """
WITH calendar AS (
    SELECT
        generate_series(
            (SELECT MIN(created_at::date) FROM orders),
            CURRENT_DATE,
            INTERVAL '1 day'
        )::date AS calendar_date
),

daily_sales AS (
    SELECT
        created_at::date AS sale_date,
        SUM(total) AS total_daily_sales
    FROM orders
    WHERE channel = 'pos'
    GROUP BY created_at::date
),

calendar_sales AS (
    SELECT
        c.calendar_date,
        CASE EXTRACT(DOW FROM c.calendar_date)
            WHEN 0 THEN 'Domingo'
            WHEN 1 THEN 'Segunda-feira'
            WHEN 2 THEN 'Terça-feira'
            WHEN 3 THEN 'Quarta-feira'
            WHEN 4 THEN 'Quinta-feira'
            WHEN 5 THEN 'Sexta-feira'
            WHEN 6 THEN 'Sábado'
        END AS weekday_name,
        COALESCE(d.total_daily_sales, 0) AS total_daily_sales
    FROM calendar c
    LEFT JOIN daily_sales d
        ON d.sale_date = c.calendar_date
)

SELECT
    weekday_name,
    AVG(total_daily_sales) AS avg_daily_sales
FROM calendar_sales
GROUP BY
    weekday_name,
    EXTRACT(DOW FROM calendar_date)
ORDER BY avg_daily_sales ASC;
"""

cursor = connection.cursor()

cursor.execute(query)

result = cursor.fetchall()

for row in result:
    print(row)