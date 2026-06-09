import joblib
import pandas as pd


def predict(data):

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