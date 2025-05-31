# 시가총액 상위 10개 기업의 3년간 시가총액 추이 시각화

import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="시가총액 상위 10개 기업", layout="wide")
st.title("🏢 시가총액 상위 10개 기업의 3년간 시가총액 변화")

# 시가총액 탑 10 기업 (2024 기준)
top10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet (GOOGL)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Tesla": "TSLA",
    "Meta": "META",
    "Broadcom": "AVGO",
    "TSMC": "TSM"
}

@st.cache_data
def get_market_cap_data(tickers):
    all_data = []
    for name, symbol in tickers.items():
        try:
            stock = yf.Ticker(symbol)
            hist = stock.history(period="3y")
            shares = stock.info.get("sharesOutstanding", None)
            if shares is None or hist.empty:
                continue
            hist = hist.reset_index()
            hist["Market Cap"] = hist["Close"] * shares
            hist["Company"] = name
            all_data.append(hist[["Date", "Market Cap", "Company"]])
        except Exception as e:
            st.warning(f"{name} 데이터 오류: {e}")
    return pd.concat(all_data, ignore_index=True)

with st.spinner("데이터 불러오는 중..."):
    df = get_market_cap_data(top10_tickers)

# Plotly 시각화
fig = px.line(df,
              x="Date", y="Market Cap", color="Company",
              title="시가총액 상위 10개 기업의 시가총액 변화 (3년간)",
              labels={"Market Cap": "시가총액 (USD)", "Date": "날짜"},
              height=600)

st.plotly_chart(fig, use_container_width=True)
