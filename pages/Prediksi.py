import streamlit as st

from utils.prediction import predict_harga

st.set_page_config(
    page_title="Prediksi Harga",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Prediksi Harga Daging Sapi")

st.write(
    "Masukkan data untuk memprediksi harga daging sapi."
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    lag1 = st.number_input(
        "Harga Hari Sebelumnya (Lag_1)",
        min_value=0.0,
        value=120000.0,
        step=100.0,
        format="%.2f"
    )

    lag2 = st.number_input(
        "Harga Dua Hari Sebelumnya (Lag_2)",
        min_value=0.0,
        value=119500.0,
        step=100.0,
        format="%.2f"
    )

with col2:

    indeks_pakan = st.number_input(
        "Indeks Pakan",
        min_value=0.0,
        value=1.00,
        step=0.01,
        format="%.2f"
    )

    indikator = st.selectbox(
        "Indikator Lebaran",
        ["Tidak", "Ya"]
    )
indikator = 1 if indikator == "Ya" else 0

st.divider()

if st.button("🔮 Prediksi Harga"):

    with st.spinner("⏳ Sedang melakukan prediksi..."):

        hasil = predict_harga(
            lag1,
            lag2,
            indikator,
            indeks_pakan
        )

    st.success("✅ Prediksi berhasil dilakukan.")

    st.metric(
        "💰 Estimasi Harga Daging",
        f"Rp {hasil:,.2f} / Kg"
    )

    selisih = hasil - lag1

    persen = (selisih / lag1) * 100

    st.divider()

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "📈 Selisih Harga",
            f"Rp {selisih:,.2f}"
        )

    with c2:
        st.metric(
            "📊 Persentase",
            f"{persen:.2f}%"
        )

    st.divider()

    if selisih > 0:
        st.success("📈 Harga diprediksi mengalami kenaikan.")
    elif selisih < 0:
        st.error("📉 Harga diprediksi mengalami penurunan.")
    else:
        st.info("➡️ Harga diprediksi tetap.")