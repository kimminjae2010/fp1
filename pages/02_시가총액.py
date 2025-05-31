# streamlit_app.py
import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

st.title("🌍 전 세계 시가총액 변화 (3년간)")

# VT ETF 데이터
vt = yf.Ticker("VT")
hist = vt.history(period="3y")

shares_outstanding = vt.info['sharesOutstanding']
hist['Market Cap'] = hist['Close'] * shares_outstanding

df = hist[['Market Cap']].reset_index()

# Plotly 시각화
fig = px.line(df, x='Date', y='Market Cap', title="Global Market Cap (VT ETF) Over 3 Years")

# Streamlit에 표시
st.plotly_chart(fig, use_container_width=True)
