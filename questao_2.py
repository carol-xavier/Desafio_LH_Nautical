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