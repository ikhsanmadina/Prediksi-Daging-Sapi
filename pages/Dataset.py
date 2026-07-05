import streamlit as st

from utils.preprocessing import load_dataset

df = load_dataset()

# ==========================
# HEADER
# ==========================

st.title("📊 Dataset Harga Daging Sapi")

st.markdown("""
Halaman ini menampilkan dataset yang digunakan dalam proses
pelatihan model **Multiple Linear Regression**.
""")

st.divider()

# ==========================
# METRIC
# ==========================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Jumlah Data", len(df))

with c2:
    st.metric("Jumlah Kolom", df.shape[1])

with c3:
    st.metric("Missing Value", df.isnull().sum().sum())

st.divider()

# ==========================
# FILTER TAHUN
# ==========================

tahun = sorted(df["Tanggal"].dt.year.unique())

tahun_pilih = st.selectbox(
    "Pilih Tahun",
    ["Semua"] + list(tahun)
)

if tahun_pilih != "Semua":
    df = df[df["Tanggal"].dt.year == tahun_pilih]

# ==========================
# SEARCH
# ==========================

keyword = st.text_input(
    "Cari Harga..."
)

if keyword:
    df = df[df["Harga"].astype(str).str.contains(keyword)]

# ==========================
# DATAFRAME
# ==========================

st.dataframe(
    df,
    use_container_width=True,
    height=500
)

# ==========================
# DOWNLOAD
# ==========================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download CSV",
    csv,
    "dataset.csv",
    "text/csv"
)