#%%
import psycopg

from database import get_connection

QUERY_PATH = "./queries/questao_5.sql"

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