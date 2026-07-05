import pandas as pd
import streamlit as st

@st.cache_data
def load_dataset():

    df = pd.read_excel(
        "dataset/dataset_daging_sapi_2021_2025.xlsx"
    )

    df["Tanggal"] = pd.to_datetime(df["Tanggal"])

    # Urutkan berdasarkan tanggal
    df = df.sort_values("Tanggal")

    # Hapus baris yang memiliki nilai kosong
    df = df.dropna()

    # Reset index
    df = df.reset_index(drop=True)

    return df