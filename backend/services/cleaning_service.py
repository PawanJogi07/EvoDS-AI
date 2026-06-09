import pandas as pd

def clean_dataframe(df):

    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)

    if "city" in df.columns:
        df["city"] = (
            df["city"]
            .astype(str)
            .str.strip()
            .str.title()
        )

    return df