import streamlit as st
from data_loader import get_stock_data, get_crypto_data
from analyzer import evaluate_assets
import plotly.graph_objects as go

st.title("📈 Top 10 Investimentos - Ações BR & Criptomoedas")

br_tickers = st.text_input("Digite os tickers das ações brasileiras (ex: PETR4, VALE3):", "PETR4,VALE3")
crypto_tickers = st.text_input("Digite os tickers das criptomoedas (ex: BTC, ETH):", "BTC,ETH")

if st.button("Analisar"):
    tickers_br = [t.strip().upper() for t in br_tickers.split(",")]
    tickers_crypto = [c.strip().upper() for c in crypto_tickers.split(",")]

    stock_data = get_stock_data(tickers_br)
    crypto_data = get_crypto_data(tickers_crypto)

    st.subheader("🔎 Dados carregados (pré-merge)")
    if not stock_data.empty:
        st.write("📘 Ações carregadas:")
        st.dataframe(stock_data.tail())
    else:
        st.warning("⚠️ Nenhuma ação foi carregada.")

    if not crypto_data.empty:
        st.write("💰 Criptomoedas carregadas:")
        st.dataframe(crypto_data.tail())
    else:
        st.warning("⚠️ Nenhuma cripto foi carregada.")

    full_data = stock_data.join(crypto_data, how='outer')

    if full_data.empty:
        st.error("❌ Nenhum dado final disponível para análise.")

    else:
        st.line_chart(full_data)

        st.subheader("📊 Top 10 Investimentos (Simulação Monte Carlo)")
        ranking = evaluate_assets(full_data)
        st.dataframe(ranking)

        fig = go.Figure()
        for _, row in ranking.iterrows():
            fig.add_trace(go.Bar(name=row["Ticker"], x=["Expected Return"], y=[row["Expected Return"]]))
        st.plotly_chart(fig)
