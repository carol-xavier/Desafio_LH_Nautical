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
