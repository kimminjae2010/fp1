import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(layout="wide")

st.title("전 세계 시가총액 Top 20 기업의 5년간 변화")
st.write("yfinance를 사용하여 지난 5년간의 시가총액 데이터를 기반으로 Plotly로 인터랙티브한 그래프를 그립니다.")

# 현재 날짜 기준 5년 전 날짜 계산
end_date = datetime.now()
start_date = end_date - timedelta(days=5 * 365) # 대략적인 5년 전

# 시가총액 상위 기업 (예시, 실제 데이터와 다를 수 있음)
# 시가총액 상위 기업 리스트는 수동으로 업데이트하거나, 외부 API를 통해 가져와야 합니다.
# 여기서는 대표적인 글로벌 기업들을 예시로 사용합니다.
top_companies_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA",
    "Amazon": "AMZN",
    "Alphabet (GOOGL)": "GOOGL",
    "Meta Platforms": "META",
    "Tesla": "TSLA",
    "Berkshire Hathaway": "BRK-A", # BRK-B도 가능
    "Eli Lilly": "LLY",
    "TSMC": "TSM",
    "Johnson & Johnson": "JNJ",
    "JPMorgan Chase": "JPM",
    "Visa": "V",
    "Walmart": "WMT",
    "ExxonMobil": "XOM",
    "UnitedHealth Group": "UNH",
    "Samsung Electronics": "005930.KS", # 한국 기업은 `.KS` 접미사
    "Procter & Gamble": "PG",
    "Chevron": "CVX",
    "Broadcom": "AVGO",
}

@st.cache_data
def get_market_cap_data(tickers, start, end):
    """
    주어진 티커 리스트에 대해 지정된 기간 동안의 시가총액 데이터를 가져옵니다.
    """
    market_cap_data = {}
    successful_tickers = []
    failed_tickers = []

    for company_name, ticker in tickers.items():
        try:
            # yfinance는 'Adj Close'를 기준으로 시가총액을 계산하기 어려움.
            # 대신 'Volume'과 'Close' 가격을 사용하여 시가총액을 추정하거나,
            # 아니면 Yahoo Finance에서 제공하는 'Market Cap' 데이터를 직접적으로 가져와야 함.
            # yfinance는 과거 시가총액 자체를 직접적으로 제공하지 않으므로,
            # 여기서는 'Close' 가격에 'Outstanding Shares'를 곱하는 방식으로 추정해야 합니다.
            # 하지만 'Outstanding Shares'가 일별로 제공되지 않으므로,
            # 여기서는 'Close' 가격 변화를 시가총액 변화로 간주하고 그래프를 그립니다.
            # 정확한 시가총액 데이터를 위해서는 다른 API를 고려해야 합니다.

            # 임시 방편으로 종가 데이터를 가져와 시가총액 변화 추이로 활용
            data = yf.download(ticker, start=start, end=end, progress=False) # progress=False 추가하여 터미널 출력 줄임
            if not data.empty and 'Close' in data.columns:
                market_cap_data[company_name] = data['Close']
                successful_tickers.append(company_name)
            else:
                st.warning(f"Warning: No valid 'Close' data found for {company_name} ({ticker}) in the specified period.")
                failed_tickers.append(company_name)
        except Exception as e:
            st.error(f"Error fetching data for {company_name} ({ticker}): {e}")
            failed_tickers.append(company_name)

    if not market_cap_data:
        st.error("모든 기업에 대한 데이터를 가져오는 데 실패했습니다. 티커 목록이나 인터넷 연결을 확인해 주세요.")
        return pd.DataFrame() # 빈 DataFrame 반환

    # 데이터를 하나의 DataFrame으로 합치기 (동일한 인덱스를 갖도록)
    # pd.concat을 사용하면 여러 Series를 합치면서 인덱스 정렬을 해줍니다.
    combined_df = pd.DataFrame(market_cap_data)

    # 모든 Series가 동일한 길이를 가지지 않을 수 있으므로, reindex 또는 fillna를 고려해야 합니다.
    # 여기서는 DataFrame으로 변환된 후 결측치는 NaN으로 처리됩니다.

    if failed_tickers:
        st.warning(f"다음 기업들의 데이터를 가져오는 데 실패했거나 유효한 데이터가 부족합니다: {', '.join(failed_tickers)}")
    
    return combined_df

# 데이터 로딩
with st.spinner("데이터를 로딩 중입니다... 잠시만 기다려주세요."):
    df_market_cap = get_market_cap_data(top_companies_tickers, start_date, end_date)

if not df_market_cap.empty:
    st.subheader("지난 5년간 Top 20 기업의 종가 변화 (시가총액 추이 대체)")
    st.write("⚠️ **주의**: yfinance는 과거 시가총액 데이터를 직접 제공하지 않으므로, 이 그래프는 각 기업의 종가 변화를 시가총액 변화의 대리 지표로 사용합니다. 정확한 시가총액 데이터를 위해서는 다른 API를 사용해야 합니다.")

    # Plotly 그래프 생성
    fig = go.Figure()

    for col in df_market_cap.columns:
        fig.add_trace(go.Scatter(x=df_market_cap.index, y=df_market_cap[col], mode='lines', name=col))

    fig.update_layout(
        title="전 세계 시가총액 Top 20 기업의 5년간 종가 변화",
        xaxis_title="날짜",
        yaxis_title="종가 (USD)",
        hovermode="x unified",
        legend_title="기업",
        height=600,
        template="plotly_dark" # 또는 "plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("원시 데이터")
    st.dataframe(df_market_cap)

else:
    st.error("데이터를 불러오는 데 실패했거나 데이터가 없어 그래프를 그릴 수 없습니다. 티커 목록이나 인터넷 연결을 확인해 주세요.")

st.markdown("""
---
**참고 사항**:
* `yfinance`는 과거 시가총액 데이터를 직접 제공하지 않습니다. 위 그래프는 종가(Close Price)를 시가총액 변화의 대리 지표로 사용했습니다. 정확한 시가총액 변화를 보기 위해서는 기업의 발행 주식수 데이터를 함께 사용하여 계산하거나, 시가총액 데이터를 직접 제공하는 다른 금융 API (예: FMP, Alpha Vantage 등)를 활용해야 합니다.
* "전 세계 시가총액 Top 20 기업" 리스트는 수동으로 업데이트해야 합니다. 시가총액 순위는 수시로 변동합니다.
* 한국 기업의 경우 티커 뒤에 `.KS` (예: `005930.KS` for Samsung Electronics)를 붙여야 합니다.
""")
