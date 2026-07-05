import streamlit as st

st.set_page_config(
    page_title="Tentang",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ Tentang Aplikasi")

st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/1046/1046784.png",
        width=180
    )

with col2:

    st.subheader("Prediksi Harga Daging Sapi")

    st.write("""
Aplikasi ini dikembangkan untuk melakukan prediksi harga daging sapi
menggunakan algoritma **Multiple Linear Regression**.

Model dibangun menggunakan data historis harga daging sapi
periode **2021–2025** serta beberapa variabel pendukung.
""")

st.markdown("---")

st.subheader("👨‍🎓 Profil Peneliti")

st.write("""
**Nama :** Anyi Suryani

**Program Studi :** Teknik Informatika

**Universitas :** Universitas Muhammadiyah Sukabumi (UMMI)

**Judul Penelitian :**

Prediksi Harga Daging Sapi Menggunakan Algoritma Multiple Linear Regression
""")

st.markdown("---")

st.subheader("📚 Teknologi")

c1, c2, c3 = st.columns(3)

c1.success("Python")
c2.success("Streamlit")
c3.success("Scikit-Learn")

c4, c5, c6 = st.columns(3)

c4.info("Pandas")
c5.info("Plotly")
c6.info("Joblib")

st.markdown("---")

st.caption("© 2026 | Prediksi Harga Daging Sapi")