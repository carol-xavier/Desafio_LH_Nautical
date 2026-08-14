# %%
import pandas as pd
from database import get_connection
from sklearn.metrics.pairwise import cosine_similarity


TARGET_PRODUCT_ID = 180
TOP_N = 5
QUERY_PATH = "./queries/questao_7.sql" 

def execute_query(connection, query_path):

    with open(query_path, "r", encoding="utf-8") as file:
        query = file.read()

    with connection.cursor() as cursor:        
        cursor.execute(query)

        return cursor.fetchall()

def load_customer_product_interactions():
    """
    Extrai do banco as combinações únicas entre cliente e produto.

    Como a matriz usuário-item da questão é binária, múltiplas compras
    do mesmo produto pelo mesmo cliente são consideradas apenas uma vez.
    """

    with get_connection() as connection:
        result = execute_query(connection, QUERY_PATH)

    return pd.DataFrame(
        result,
        columns=[
            "customer_id",
            "product_id",
            "product_name"
        ]
    )


def build_user_item_matrix(interactions):
    """
    Constrói a matriz binária usuário x produto.

    Valor 1: cliente comprou o produto ao menos uma vez.
    Valor 0: cliente nunca comprou o produto.
    """
    user_item_matrix = pd.crosstab(
        interactions["customer_id"],
        interactions["product_id"]
    )

    return (user_item_matrix > 0).astype(int)


def calculate_product_similarity(user_item_matrix):
    """
    Calcula a similaridade de cosseno produto x produto.

    A matriz é transposta porque queremos comparar os vetores
    dos produtos com base nos clientes que compraram cada item.
    """
    similarity_matrix = cosine_similarity(
        user_item_matrix.T
    )

    return pd.DataFrame(
        similarity_matrix,
        index=user_item_matrix.columns,
        columns=user_item_matrix.columns
    )


def get_product_names(interactions):
    """
    Cria um mapeamento entre product_id e product_name.
    """
    return (
        interactions[
            ["product_id", "product_name"]
        ]
        .drop_duplicates()
        .set_index("product_id")["product_name"]
    )


def get_top_similar_products(
    product_similarity,
    product_names,
    target_product_id,
    top_n=5
):
    """
    Retorna os produtos mais similares ao produto de referência,
    excluindo o próprio produto do ranking.
    """
    similar_products = (
        product_similarity[target_product_id]
        .drop(target_product_id)
        .sort_values(ascending=False)
        .head(top_n)
    )

    return pd.DataFrame({
        "product_id": similar_products.index,
        "product_name": [
            product_names[product_id]
            for product_id in similar_products.index
        ],
        "cosine_similarity": similar_products.values
    }).reset_index(drop=True)


def main():
    interactions = load_customer_product_interactions()

    user_item_matrix = build_user_item_matrix(
        interactions
    )

    product_similarity = calculate_product_similarity(
        user_item_matrix
    )

    product_names = get_product_names(
        interactions
    )

    top_5 = get_top_similar_products(
        product_similarity=product_similarity,
        product_names=product_names,
        target_product_id=TARGET_PRODUCT_ID,
        top_n=TOP_N
    )

    print(top_5)


if __name__ == "__main__":
    main()