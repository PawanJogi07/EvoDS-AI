import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_models(target_column):

    with open(
        "uploads/current_file.txt",
        "r"
    ) as f:

        latest_file = f.read().strip()

    df = pd.read_csv(
        f"uploads/{latest_file}"
    )

    if "Unnamed: 0" in df.columns:
        df.drop(
            columns=["Unnamed: 0"],
            inplace=True
        )

    df = df.dropna()

    if target_column not in df.columns:

        return {
            "error":
            f"{target_column} not found"
        }

    X = df.drop(
        columns=[target_column]
    )

    # ORIGINAL FEATURES SAVE
    original_features = X.columns.tolist()

    X = pd.get_dummies(X)

    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Dynamic k for KNN based on training set size
    optimal_k = max(1, min(5, len(X_train) - 1))

    models = {
        "RandomForest":
        RandomForestClassifier(random_state=42),

        "DecisionTree":
        DecisionTreeClassifier(random_state=42),

        "KNN":
        KNeighborsClassifier(n_neighbors=optimal_k)
    }

    leaderboard = {}

    best_model = None
    best_model_name = None
    best_accuracy = 0

    for name, model in models.items():

        model.fit(
            X_train,
            y_train
        )

        preds = model.predict(
            X_test
        )

        acc = accuracy_score(
            y_test,
            preds
        )

        leaderboard[name] = round(
            acc * 100,
            2
        )

        if acc > best_accuracy:

            best_accuracy = acc
            best_model_name = name
            best_model = model

    os.makedirs(
        "models",
        exist_ok=True
    )

    joblib.dump(
        best_model,
        "models/best_model.pkl"
    )

    joblib.dump(
        X.columns.tolist(),
        "models/model_columns.pkl"
    )

    # NEW
    joblib.dump(
        original_features,
        "models/original_features.pkl"
    )

    joblib.dump(
        target_column,
        "models/target_column.pkl"
    )

    return {
        "dataset": latest_file,
        "target": target_column,
        "best_model": best_model_name,
        "accuracy": round(
            best_accuracy * 100,
            2
        ),
        "leaderboard": leaderboard
    }