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
