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

# %%
"""
=============================================================================
1.3 Avaliação de outliers
=============================================================================
"""
q1 = np.percentile(df_orders['total'], 25)
q3 = np.percentile(df_orders['total'], 75)
iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outliers = df_orders[(df_orders['total'] < lower_limit) | (df_orders['total'] > upper_limit)]
print(f"Total outliers detected: {len(outliers)}\nValores acima de R$ {upper_limit:.2f} foram detectados como outliers.")

# %%
# Visualização dos quartis e outliers
plt.figure(figsize=(8, 5))

sns.boxplot(data=df_orders, y='total')

plt.title('Distribution of Order Total')
plt.ylabel('Order Total (R$)')

plt.show()

# %%
"""
=============================================================================
1.4 Diagnóstico
=============================================================================
"""
conclusion = "A análise exploratória inicial indica que a tabela 'orders' requer validações adicionais antes de \nser utilizada em análises definitivas. A coluna `salesperson_id` apresenta 24.131 valores nulos, \naproximadamente 49,25% dos registros, o que pode impactar análises relacionadas ao desempenho \ndos vendedores. A coluna `total` não apresenta valores negativos ou nulos, porém foram identificados \n452 possíveis outliers pelo critério do IQR. Esses registros não devem ser considerados erros \nautomaticamente, pois podem representar pedidos de alto valor e precisam ser investigados. Além disso, \n`created_at` está armazenada em formato textual e deverá ser convertida para um tipo de data/hora \nem uma etapa posterior de tratamento. Portanto, a tabela é adequada para uma análise exploratória inicial, \nmas não está pronta para análises definitivas sem tratamento prévio, principalmente em relação aos valores \nausentes, ao formato das datas e aos possíveis outliers."

print(conclusion)