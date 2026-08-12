"""
=============================================================================
Questão 2 - DB Schema
=============================================================================
"""
# %%
# Importando bibliotecas necessárias para gerar o schema do banco de dados
import os 
import csv
from datetime import datetime

# %%
# Listando todos os arquivos CSV na pasta "data"
files = [
    os.path.join("data", f)
    for f in os.listdir("data")
    if f.endswith(".csv")
]

# %%
# Função para inferir o tipo de dado de um valor 
def infer_type(value):
    value = value.strip()

    if value == "":
        return "empty"

    if value.lower() in ("true", "false"):
        return "BOOLEAN"

    try:
        int(value)
        return "INTEGER"
    except ValueError:
        pass

    try:
        float(value)
        return "FLOAT"
    except ValueError:
        pass

    try:
        datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        return "TIMESTAMP"
    except ValueError:
        pass

    try:
        datetime.strptime(value, "%Y-%m-%d")
        return "DATE"
    except ValueError:
        pass

    return "TEXT" 

# %%
# Função para inferir o tipo de dado de uma coluna com base em todos os valores presentes nela
def infer_column_type(values):
    values = [value for value in values if value.strip() != ""]

    types = [infer_type(value) for value in values]

    if all(t == "INTEGER" for t in types):
        return "INTEGER"

    if all(t == "boolean" for t in types):
            return "BOOLEAN"

    if all(t in ("integer", "float") for t in types):
        return "FLOAT"

    if all(t == "timestamp" for t in types):
        return "TIMESTAMP"

    if all(t == "date" for t in types):
            return "DATE"

    return "text"

# %%
# Função de validação para verificar as funções de inferência de tipos de dados e gerar o schema do banco de dados
def check_tables():
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            columns = reader.fieldnames
            data = list(reader)

        print(f"\nArquivo: {file}")
        print(f"Linhas: {len(data)}")
        print(f"Colunas: {len(columns)}")

        for column in columns:
            values = [row[column] for row in data]
            column_type = infer_column_type(values)

            print(f"{column}: {column_type}")
    
check_tables()

# %%
# Função para gerar o comando SQL CREATE_TABLE com base no nome da tabela, colunas e linhas
def generate_create_table(table_name, columns, rows):
    sql = f"CREATE TABLE {table_name} (\n"

    column_definitions = []

    for column in columns:
        values = [row[column] for row in rows]
        data_type = infer_column_type(values)

        column_definitions.append(
            f"    {column} {data_type}"
        )

    sql += ",\n".join(column_definitions)
    sql += "\n);\n"

    return sql

# %%
# Função para gerar o schema do banco de dados com base nos arquivos CSV presentes na pasta "data"
def generate_schema():
    schema = []

    for file in files:

        table_name = os.path.splitext(os.path.basename(file))[0]

        with open(file, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)

            columns = reader.fieldnames
            rows = list(reader)

        create_table = generate_create_table(
            table_name,
            columns,
            rows
        )

        schema.append(create_table)

    with open("schema.sql", "w", encoding="utf-8") as f:
        f.write("\n".join(schema))

generate_schema()
