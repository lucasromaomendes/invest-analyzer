import streamlit as st
import requests

st.subheader("🔌 Teste de conexão com a internet")

try:
    r = requests.get("https://finance.yahoo.com", timeout=5)
    if r.status_code == 200:
        st.success("✅ Conexão com Yahoo Finance OK.")
    else:
        st.warning(f"⚠️ Conexão feita, mas status: {r.status_code}")
except Exception as e:
    st.error(f"❌ Erro ao conectar: {e}")
