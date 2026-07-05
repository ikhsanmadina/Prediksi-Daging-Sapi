import streamlit as st
import pandas as pd
import plotly.express as px

from utils.train_model import train_model

st.set_page_config(
    page_title="Evaluasi Model",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Evaluasi Model")

st.write("""
Halaman ini menampilkan hasil evaluasi model Multiple Linear Regression.
""")

st.divider()

# ===========================================
# TRAIN MODEL
# ===========================================

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

# ===========================================
# METRIK
# ===========================================

c1, c2, c3, c4 = st.columns(4)

c1.metric("MAE", f"{mae:,.2f}")
c2.metric("RMSE", f"{rmse:,.2f}")
c3.metric("MAPE", f"{mape:.2%}")
c4.metric("R²", f"{r2:.4f}")

st.divider()

# ===========================================
# DATA HASIL
# ===========================================

hasil = pd.DataFrame({
    "Aktual": y_test.values,
    "Prediksi": y_pred
})

hasil["Residual"] = hasil["Aktual"] - hasil["Prediksi"]

# ===========================================
# GRAFIK AKTUAL VS PREDIKSI
# ===========================================

st.subheader("📈 Aktual vs Prediksi")

fig1 = px.line(
    hasil.reset_index(),
    x=hasil.reset_index().index,
    y=["Aktual", "Prediksi"],
    markers=True,
    template="plotly_white"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ===========================================
# RESIDUAL
# ===========================================

st.subheader("📉 Residual")

fig2 = px.scatter(
    hasil,
    x="Prediksi",
    y="Residual",
    template="plotly_white"
)

fig2.add_hline(
    y=0,
    line_dash="dash",
    line_color="red"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ===========================================
# TABEL
# ===========================================

st.subheader("📋 Hasil Prediksi")

st.dataframe(
    hasil,
    use_container_width=True
)

# ===========================================
# DOWNLOAD
# ===========================================

csv = hasil.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Hasil Prediksi",
    csv,
    "hasil_prediksi.csv",
    "text/csv"
)