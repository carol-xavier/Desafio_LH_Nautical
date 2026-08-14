# %%
import psycopg

from datetime import date

from database import get_connection


QUERY_PATH = "./queries/questao_6.sql"


def execute_query(connection, query_path):
    with open(query_path, "r", encoding="utf-8") as file:
        query = file.read()

    with connection.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def get_data():
    with get_connection() as connection:
        return execute_query(connection, QUERY_PATH)


def calculate_mae(actual, predicted):
    errors = [
        abs(actual[month] - predicted[month])
        for month in actual
    ]

    return sum(errors) / len(errors)


def main():
    try:
        result = get_data()

        monthly_sales = {
            month: units
            for month, units in result
        }

        """
        =========================================================================
        Separar dados de treino e de teste conforme delimitado pelo Tech Lead
        =========================================================================
        """
        train = {
            month: units
            for month, units in monthly_sales.items()
            if month <= date(2025, 12, 1)
        }

        test = {
            month: units
            for month, units in monthly_sales.items()
            if date(2026, 1, 1) <= month <= date(2026, 3, 1)
        }

        """
        =========================================================================
        Modelo Walk-forward
        =========================================================================
        """
        history = dict(train)
        walk_forward_forecasts = {}

        for month in sorted(test):
            previous_months = sorted(history)[-3:]

            forecast = sum(
                history[m] for m in previous_months
            ) / len(previous_months)

            walk_forward_forecasts[month] = forecast

            # Após prever o mês, o valor real passa a fazer parte do histórico.
            history[month] = test[month]

        mae_walk_forward = calculate_mae(
            test,
            walk_forward_forecasts,
        )

        print("Previsões:")
        for month, forecast in walk_forward_forecasts.items():
            print(month, forecast)

        print(f"MAE: {mae_walk_forward}")

    except psycopg.Error as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    main()
# %%
