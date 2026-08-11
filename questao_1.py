"""
=============================================================================
Questão 1 - EDA
=============================================================================
"""
# %%
# Importando bibliotecas necessárias para análise exploratória de dados
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# %%
"""
=============================================================================
1.1 Visão geral da base de dados
=============================================================================
"""

# %%
df_orders = pd.read_csv('data/orders.csv')

df_orders.head() # Ver as primeiras informações da base para verificar a criação do DF

# %%
df_orders.info() # Verificar informações do DF, como quantidade de linhas, colunas e tipos de dados

df_orders.describe().T # Verificar estatísticas descritivas da base de dados, como média, desvio padrão, valores mínimo e máximo

"""
Pela informação acima, podemos ver que a base de dados possui 48.998 linhas e 13 colunas. 
Em salesperson_id, 24131 valores nulos foram encontrados, e os tipos de dados das colunas são variados, incluindo inteiros, floats e objetos.
Além disso, a média está bem acima da mediana (25.917,84), o que sugere uma distribuição assimétrica à direita.
"""
# %%
"""
=============================================================================
1.2 Avaliação da coluna "total"
=============================================================================
"""
# %%
total_duplicates = df_orders.duplicated().sum() # Verificar duplicidade de registros completos.
print(f"Total duplicate rows: {total_duplicates}")

# %%
fisrt_date = df_orders['created_at'].min() # Verificar a primeira data de criação de pedidos    
last_date = df_orders['created_at'].max() # Verificar a última data de criação de pedidos
print(f"O intervalo de tempo da base de dados é de {fisrt_date} até {last_date}.") # Imprimir o intervalo de tempo da base de dados

# %%
max_value = df_orders['total'].max() # Verificar o valor máximo de pedidos
min_value = df_orders['total'].min() # Verificar o valor mínimo de pedidos
avg_ticket = df_orders['total'].mean() # Verificar o valor médio de pedidos 
print(f"O valor máximo de pedidos é de R$ {max_value:.2f}, o valor mínimo de pedidos é de R$ {min_value:.2f} e o valor médio é R$ {avg_ticket:.2f}.") # Imprimir os valores máximo e mínimo de pedidos

