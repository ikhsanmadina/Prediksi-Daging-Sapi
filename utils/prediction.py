import joblib
import numpy as np


def predict_harga(
    lag1,
    lag2,
    indikator_lebaran,
    indeks_pakan
):

    model = joblib.load("model/model.pkl")

    data = np.array([
        [
            lag1,
            lag2,
            indikator_lebaran,
            indeks_pakan
        ]
    ])

    hasil = model.predict(data)

    return hasil[0]