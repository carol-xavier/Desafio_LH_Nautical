"""
=============================================================================
Questão 3 - Load Data: Criar e carregar tabelas no PostgreSQL a partir de arquivos CSV
=============================================================================
"""

#Importando as bibliotecas necessárias
import csv
import os
import psycopg
from psycopg import sql
from dotenv import load_dotenv

load_dotenv()


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

# Variável global para definir o diretório onde os arquivos CSV estão localizados
CSV_DIR = "data"

# Função para obter os nomes das colunas de um arquivo CSV
def get_csv_columns(file_path):
    with open(file_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        return next(reader)

## Previamente, um banco de dados postgreSQL foi criado pelo terminal, utilizando os comandos:
### CREATE USER username WITH PASSWORD 'password';
### CREATE DATABASE nome_do_banco;
## O schema.sql de questao_2.py foi executado no banco de dados para criar as tabelas necessárias, comando:
### psql -h db_host -U db_user -d db_name -f schema.sql

# Funções para carregar os dados de um arquivo CSV em uma tabela do PostgreSQL
def load_csv(connection, file_path, table_name):
    columns = get_csv_columns(file_path)

    copy_query = sql.SQL(
        "COPY {} ({}) FROM STDIN WITH (FORMAT CSV, HEADER TRUE)"
    ).format(
        sql.Identifier(table_name),
        sql.SQL(", ").join(map(sql.Identifier, columns)),
    )

    with open(file_path, "r", encoding="utf-8", newline="") as file:
        with connection.cursor() as cur:
            with cur.copy(copy_query) as copy:
                while data := file.read(8192):
                    copy.write(data)


def main():
    csv_files = sorted(
        file_name
        for file_name in os.listdir(CSV_DIR)
        if file_name.lower().endswith(".csv")
    )

    with psycopg.connect(**DB_CONFIG) as connection:
        for file_name in csv_files:
            table_name = os.path.splitext(file_name)[0]
            file_path = os.path.join(CSV_DIR, file_name)

            load_csv(connection, file_path, table_name)

            print(f"{file_name} carregado em {table_name}")

    print("Carregamento concluído.")


if __name__ == "__main__":
    main()

# Run the comand below to execute the script (in the terminal, in the same directory as the script):
# python questao_3.py