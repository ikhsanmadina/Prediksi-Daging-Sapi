import streamlit as st
import plotly.express as px

from utils.preprocessing import load_dataset

# ============================================
# CONFIG
# ============================================

st.set_page_config(
    page_title="Visualisasi",
    page_icon="📈",
    layout="wide"
)

# ============================================
# LOAD DATA
# ============================================

df = load_dataset()

# ============================================
# HEADER
# ============================================

st.title("📈 Visualisasi Data")

st.markdown("""
Halaman ini menampilkan berbagai visualisasi dari dataset harga
daging sapi yang digunakan pada proses pemodelan Multiple Linear Regression.
""")

st.divider()

# ============================================
# FILTER TAHUN
# ============================================

tahun = sorted(df["Tanggal"].dt.year.unique())

pilih_tahun = st.selectbox(
    "Pilih Tahun",
    ["Semua"] + list(tahun)
)

if pilih_tahun != "Semua":
    df = df[df["Tanggal"].dt.year == pilih_tahun]

# ============================================
# LINE CHART
# ============================================

st.subheader("📈 Grafik Harga Daging")

fig_line = px.line(
    df,
    x="Tanggal",
    y="Harga",
    markers=True,
    template="plotly_white"
)

fig_line.update_layout(
    height=500
)

st.plotly_chart(
    fig_line,
    use_container_width=True
)

# ============================================
# HISTOGRAM
# ============================================

st.subheader("📊 Histogram Harga")

fig_hist = px.histogram(
    df,
    x="Harga",
    nbins=25,
    template="plotly_white"
)

st.plotly_chart(
    fig_hist,
    use_container_width=True
)

# ============================================
# BOXPLOT
# ============================================

st.subheader("📦 Boxplot Harga")

fig_box = px.box(
    df,
    y="Harga",
    template="plotly_white"
)

st.plotly_chart(
    fig_box,
    use_container_width=True
)

# ============================================
# SCATTER
# ============================================

st.subheader("📉 Scatter Plot")

fig_scatter = px.scatter(
    df,
    x="Lag_1",
    y="Harga",
    color="Indikator_Lebaran",
    template="plotly_white"
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

# ============================================
# KORELASI
# ============================================

st.subheader("🔥 Korelasi Antar Variabel")

corr = df[
    [
        "Harga",
        "Lag_1",
        "Lag_2",
        "Indeks_Pakan",
        "Indikator_Lebaran"
    ]
].corr()

st.dataframe(
    corr.style.background_gradient(cmap="Greens"),
    use_container_width=True
)

st.divider()

st.caption("Visualisasi Dataset Harga Daging Sapi")