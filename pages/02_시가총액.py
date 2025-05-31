# streamlit_app.py
import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="세계 시가총액", layout="wide")
st.title("🌍 전 세계 시가총액 (VT ETF 기준) - 3년간 추이")

# VT ETF: Vanguard Total World Stock ETF
vt = yf.Ticker("VT")

# 가격 데이터 불러오기
hist = vt.history(period="3y")
hist = hist.reset_index()

# 시가총액 계산 시도
info = vt.info
shares_outstanding = info.get("sharesOutstanding")

if shares_outstanding:
    hist["Market Cap"] = hist["Close"] * shares_outstanding
    fig = px.line(hist, x="Date", y="Market Cap",
                  title="🌐 VT ETF를 통한 전 세계 시가총액 추정 (3년간)",
                  labels={"Market Cap": "시가총액 (USD)"})
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("⚠️ 'sharesOutstanding' 정보가 제공되지 않아 시가총액을 계산할 수 없습니다.\n대신 VT ETF의 종가 추이를 보여드립니다.")
    fig = px.line(hist, x="Date", y="Close",
                  title="📈 VT ETF 가격 추이 (3년간)",
                  labels={"Close": "종가 (USD)"})
    st.plotly_chart(fig, use_container_width=True)
