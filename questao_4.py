# %%
import psycopg

from database import get_connection


"""
Escolha qual query você deseja executar, descomentando a linha correspondente abaixo e comentando as demais.
"""
#QUERY_PATH = "./queries/all_customers.sql"  # Calcula ticket médio e diversidade para todos os clientes
#QUERY_PATH = "./queries/top_10_customers.sql"  # Calcula e seleciona os clientes fiéis, os 10 clientes com maior ticket médio e diversida
QUERY_PATH = "./queries/top_category.sql"  # Calcula e seleciona a categoria mais comprada, com maior ticket médio e diversidade


def execute_query(connection, query_path):

    with open(query_path, "r", encoding="utf-8") as file:
        query = file.read()

    with connection.cursor() as cursor:        
        cursor.execute(query)

        return cursor.fetchall()
    

def main():
    try:
        with get_connection() as connection:
            result = execute_query(connection, QUERY_PATH)

            for row in result:
                print(row)

            connection.close()

    except psycopg.Error as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    main()