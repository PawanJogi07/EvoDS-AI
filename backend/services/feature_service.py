import pandas as pd

from sklearn.ensemble import RandomForestClassifier

def feature_importance():

    df = pd.read_csv("uploads/new.csv")

    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)

    df = df.dropna()

    target_column = "product"

    X = df.drop(columns=[target_column])
    X = pd.get_dummies(X)

    y = df[target_column]

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    importance = dict(
        zip(
            X.columns,
            model.feature_importances_
        )
    )

    importance = dict(
        sorted(
            importance.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]
    )

    return importance