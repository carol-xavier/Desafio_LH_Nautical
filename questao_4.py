# %%
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

# %%
# Importando as variáveis de ambiente do arquivo .env
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
def execute_query(connection, query_path):

    with open(query_path, "r", encoding="utf-8") as file:
        query = file.read()

    with connection.cursor() as cursor:        
        cursor.execute(query)

        return cursor.fetchall()
    

# %%
def main():
    try:
        with psycopg.connect(**DB_CONFIG) as connection:
            result = execute_query(connection, file_path)

            for row in result:
                print(row)

    except psycopg.Error as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    main()