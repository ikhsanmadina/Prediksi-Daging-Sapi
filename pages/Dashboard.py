import streamlit as st
import pandas as pd
import plotly.express as px

from utils.preprocessing import load_dataset

# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏠",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

df = load_dataset()

# ==========================================
# HEADER
# ==========================================

st.title("🏠 Dashboard")

st.markdown("""
Dashboard ini menampilkan ringkasan dataset harga daging sapi
yang digunakan dalam proses prediksi menggunakan algoritma
**Multiple Linear Regression**.
""")

st.divider()

# ==========================================
# METRIK
# ==========================================

jumlah_data = len(df)

tahun_awal = df["Tanggal"].dt.year.min()

tahun_akhir = df["Tanggal"].dt.year.max()

harga_rata = df["Harga"].mean()

harga_max = df["Harga"].max()

harga_min = df["Harga"].min()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "📦 Jumlah Data",
    f"{jumlah_data:,}"
)

col2.metric(
    "📅 Rentang Tahun",
    f"{tahun_awal}-{tahun_akhir}"
)

col3.metric(
    "💰 Rata-rata Harga",
    f"Rp {harga_rata:,.0f}"
)

col4.metric(
    "📈 Harga Maksimum",
    f"Rp {harga_max:,.0f}"
)

col5.metric(
    "📉 Harga Minimum",
    f"Rp {harga_min:,.0f}"
)

st.divider()

# ==========================================
# GRAFIK HARGA
# ==========================================

st.subheader("📈 Pergerakan Harga Daging Sapi")

fig = px.line(
    df,
    x="Tanggal",
    y="Harga",
    markers=False,
    template="plotly_white"
)

fig.update_layout(
    height=500,
    xaxis_title="Tanggal",
    yaxis_title="Harga (Rp)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================
# RATA-RATA PER TAHUN
# ==========================================

st.subheader("📊 Rata-rata Harga per Tahun")

rata_tahun = (
    df.groupby(df["Tanggal"].dt.year)["Harga"]
      .mean()
      .reset_index()
)

rata_tahun.columns = [
    "Tahun",
    "Rata-rata Harga"
]

fig2 = px.bar(
    rata_tahun,
    x="Tahun",
    y="Rata-rata Harga",
    text_auto=".0f",
    template="plotly_white"
)

fig2.update_layout(
    height=450
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# ==========================================
# DATA TERBARU
# ==========================================

st.subheader("📋 10 Data Terbaru")

st.dataframe(
    df.tail(10),
    use_container_width=True
)