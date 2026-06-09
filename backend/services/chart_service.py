import matplotlib.pyplot as plt
import os

os.makedirs("reports", exist_ok=True)


def generate_product_chart(df):

    products = (
        df["product"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(8, 5))
    products.plot(kind="bar")

    plt.title("Top Products")
    plt.tight_layout()

    plt.savefig(
        "reports/product_distribution.png"
    )

    plt.close()


def generate_city_chart(df):

    cities = (
        df["city"]
        .value_counts()
    )

    plt.figure(figsize=(8, 5))
    cities.plot(kind="bar")

    plt.title("City Distribution")
    plt.tight_layout()

    plt.savefig(
        "reports/city_distribution.png"
    )

    plt.close()


def generate_missing_chart(df):

    missing = df.isnull().sum()

    plt.figure(figsize=(8, 5))
    missing.plot(kind="bar")

    plt.title("Missing Values")
    plt.tight_layout()

    plt.savefig(
        "reports/missing_values.png"
    )

    plt.close()