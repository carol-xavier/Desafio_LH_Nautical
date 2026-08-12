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
