import os
import joblib
import pandas as pd


def predict(data):

    # Model exists?
    if not os.path.exists(
        "models/best_model.pkl"
    ):
        return {
            "error":
            "No trained model found. Please train a model first."
        }

    if not os.path.exists(
        "models/model_columns.pkl"
    ):
        return {
            "error":
            "Model columns not found. Please train a model first."
        }

    model = joblib.load(
        "models/best_model.pkl"
    )

    columns = joblib.load(
        "models/model_columns.pkl"
    )

    sample = pd.DataFrame(
        [data]
    )

    sample = pd.get_dummies(
        sample
    )

    sample = sample.reindex(
        columns=columns,
        fill_value=0
    )

    prediction = model.predict(
        sample
    )

    return {
        "prediction":
        str(prediction[0])
    }