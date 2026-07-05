import streamlit as st
# ==========================
# Konfigurasi Halaman
# ==========================
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.set_page_config(
    page_title="Prediksi Harga Daging Sapi",
    page_icon="🥩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# Header
# ==========================

st.sidebar.title("🐄 Prediksi Harga Daging")

st.subheader("Multiple Linear Regression")

st.markdown("---")
st.caption(
    "Prediksi Harga Daging Sapi • Multiple Linear Regression • © 2026"
)
st.markdown("""
## 👋 Selamat Datang

Aplikasi ini digunakan untuk melakukan **Prediksi Harga Daging Sapi**
menggunakan algoritma **Multiple Linear Regression**.

### 📌 Menu Aplikasi

- 🏠 Dashboard
- 📊 Dataset
- 📈 Visualisasi Data
- 🤖 Training Model
- 💰 Prediksi Harga
- 📉 Evaluasi Model
- ℹ️ Tentang

Silakan pilih menu pada **sidebar sebelah kiri**.
""")

st.info("👈 Klik menu pada sidebar untuk mulai menggunakan aplikasi.")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Algoritma", "MLR")

with col2:
    st.metric("Framework", "Streamlit")

with col3:
    st.metric("Bahasa", "Python")

st.markdown("---")

st.caption("© 2026 | Prediksi Harga Daging Sapi | Multiple Linear Regression")