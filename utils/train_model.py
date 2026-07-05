import pandas as pd
import joblib
import math
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error,
    r2_score
)

from utils.preprocessing import load_dataset


def train_model():

    # ==========================================
    # LOAD DATASET
    # ==========================================
    df = load_dataset()

    # ==========================================
    # AMBIL KOLOM YANG DIGUNAKAN
    # ==========================================
    df = df[
        [
            "Lag_1",
            "Lag_2",
            "Indikator_Lebaran",
            "Indeks_Pakan",
            "Harga"
        ]
    ].copy()

    # ==========================================
    # UBAH KE NUMERIK
    # ==========================================
    df["Lag_1"] = pd.to_numeric(df["Lag_1"], errors="coerce")
    df["Lag_2"] = pd.to_numeric(df["Lag_2"], errors="coerce")
    df["Indeks_Pakan"] = pd.to_numeric(df["Indeks_Pakan"], errors="coerce")
    df["Harga"] = pd.to_numeric(df["Harga"], errors="coerce")
    df["Indikator_Lebaran"] = pd.to_numeric(
        df["Indikator_Lebaran"],
        errors="coerce"
    )

    # ==========================================
    # HAPUS DATA YANG MASIH NaN
    # ==========================================
    df = df.dropna().reset_index(drop=True)

    # ==========================================
    # FITUR DAN TARGET
    # ==========================================
    X = df[
        [
            "Lag_1",
            "Lag_2",
            "Indikator_Lebaran",
            "Indeks_Pakan"
        ]
    ]

    y = df["Harga"]

    # ==========================================
    # SPLIT DATA
    # ==========================================
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # ==========================================
    # TRAIN MODEL
    # ==========================================
    model = LinearRegression()

    model.fit(
        X_train,
        y_train
    )

    # ==========================================
    # PREDIKSI
    # ==========================================
    y_pred = model.predict(X_test)

    # ==========================================
    # EVALUASI
    # ==========================================
    mae = mean_absolute_error(
        y_test,
        y_pred
    )

    rmse = math.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)

    mape = mean_absolute_percentage_error(
        y_test,
        y_pred
    )

    r2 = r2_score(
        y_test,
        y_pred
    )

    # ==========================================
    # SIMPAN MODEL
    # ==========================================
    joblib.dump(
        model,
        "model/model.pkl"
    )

    # ==========================================
    # RETURN
    # ==========================================
    return (
        model,
        mae,
        rmse,
        mape,
        r2,
        X_test,
        y_test,
        y_pred
    )