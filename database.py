import os

import psycopg
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

def get_connection():
    return psycopg.connect(**DB_CONFIG)

