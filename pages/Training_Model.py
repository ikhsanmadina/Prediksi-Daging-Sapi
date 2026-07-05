import streamlit as st
import pandas as pd

from utils.preprocessing import load_dataset
from utils.train_model import train_model

# ============================================
# CONFIG
# ============================================

st.set_page_config(
    page_title="Training Model",
    page_icon="🤖",
    layout="wide"
)

# ============================================
# LOAD DATASET
# ============================================

df = load_dataset()

# ============================================
# HEADER
# ============================================

st.title("🤖 Training Multiple Linear Regression")

st.write(
    "Halaman ini digunakan untuk melatih model Multiple Linear Regression."
)

st.divider()

# ============================================
# CEK DATASET
# ============================================

st.subheader("📊 Informasi Dataset")

col1, col2 = st.columns(2)

with col1:
    st.metric("Jumlah Data", len(df))

with col2:
    st.metric("Jumlah Kolom", len(df.columns))

st.write("### Missing Value")

st.dataframe(
    df.isnull().sum().reset_index().rename(
        columns={
            "index": "Kolom",
            0: "Jumlah Missing"
        }
    ),
    use_container_width=True
)

st.divider()

# ============================================
# TRAIN MODEL
# ============================================

if st.button("🚀 Train Model"):

    (
        model,
        mae,
        rmse,
        mape,
        r2,
        X_test,
        y_test,
        y_pred
    ) = train_model()

    st.success("✅ Model berhasil dilatih!")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("MAE", f"{mae:,.2f}")
    c2.metric("RMSE", f"{rmse:,.2f}")
    c3.metric("MAPE", f"{mape:.2%}")
    c4.metric("R²", f"{r2:.4f}")

    st.divider()

    st.subheader("Koefisien")

    coef = pd.DataFrame({
        "Variabel": X_test.columns,
        "Koefisien": model.coef_
    })

    st.dataframe(
        coef,
        use_container_width=True
    )

    st.subheader("Intercept")

    st.code(model.intercept_)