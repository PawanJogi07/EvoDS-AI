import pandas as pd
import pickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model(target_column):

    with open(
        "uploads/current_file.txt",
        "r"
    ) as f:

        latest_file = f.read().strip()

    df = pd.read_csv(
        f"uploads/{latest_file}"
    )

    df = df.dropna()

    if target_column not in df.columns:
        return {
            "error": "Target column not found"
        }

    X = df.drop(
        columns=[target_column]
    )

    X = pd.get_dummies(X)

    y = df[target_column]

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )
    )

    model = RandomForestRegressor(
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    preds = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        preds
    )

    with open(
        "models/best_model.pkl",
        "wb"
    ) as f:

        pickle.dump(
            model,
            f
        )

    with open(
        "models/model_columns.pkl",
        "wb"
    ) as f:

        pickle.dump(
            X.columns.tolist(),
            f
        )

    return {
        "dataset": latest_file,
        "target": target_column,
        "accuracy": round(
            accuracy * 100,
            2
        )
    }