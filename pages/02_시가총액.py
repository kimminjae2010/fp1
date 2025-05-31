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
top_companies_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA",
    "Amazon": "AMZN",
    "Alphabet (GOOGL)": "GOOGL",
    "Meta Platforms": "META",
    "Tesla": "TSLA",
    "Berkshire Hathaway": "BRK-A",
    "Eli Lilly": "LLY",
    "TSMC": "TSM",
    "Johnson & Johnson": "JNJ",
    "JPMorgan Chase": "JPM",
    "Visa": "V",
    "Walmart": "WMT",
    "ExxonMobil": "XOM",
    "UnitedHealth Group": "UNH",
    "Samsung Electronics": "005930.KS",
    "Procter & Gamble": "PG",
    "Chevron": "CVX",
    "Broadcom": "AVGO",
}

@st.cache_data
def get_market_cap_data(tickers, start, end):
    market_cap_data = {}
    successful_tickers = []
    failed_tickers = []

    for company_name, ticker in tickers.items():
        try:
            # yfinance.download에서 progress=False를 사용하여 출력 간소화
            data = yf.download(ticker, start=start, end=end, progress=False)
            
            # 데이터가 비어있지 않고 'Close' 컬럼이 있는지 확인
            if not data.empty and 'Close' in data.columns:
                market_cap_data[company_name] = data['Close']
                successful_tickers.append(company_name)
                # 데이터가 성공적으로 로드되면 디버깅용 메시지 출력
                # st.write(f"DEBUG: Successfully loaded data for {company_name} ({ticker}). Data points: {len(data['Close'])}")
            else:
                st.warning(f"Warning: No valid 'Close' data found for {company_name} ({ticker}) in the specified period. Data Empty: {data.empty}, Has 'Close' column: {'Close' in data.columns}")
                failed_tickers.append(company_name)
        except Exception as e:
            st.error(f"Error fetching data for {company_name} ({ticker}): {e}")
            failed_tickers.append(company_name)

    # 모든 티커에 대한 데이터 로딩이 실패했을 경우
    if not market_cap_data:
        st.error("모든 기업에 대한 데이터를 가져오는 데 실패했습니다. 티커 목록이나 인터넷 연결을 확인해 주세요.")
        return pd.DataFrame() # 빈 DataFrame 반환하여 오류 회피

    # Debugging: `market_cap_data`의 내용 확인
    # for name, series in market_cap_data.items():
    #     st.write(f"DEBUG: {name} series length: {len(series)}, is_empty: {series.empty}")
    #     if series.empty:
    #         st.write(f"DEBUG: {name} series is empty.")

    # DataFrame 생성 시, 인덱스 불일치로 인한 오류를 방지하기 위해 정렬 시도
    # (선택 사항이지만, 데이터를 합칠 때 발생할 수 있는 잠재적 문제를 줄여줌)
    combined_df = pd.DataFrame(market_cap_data)
    
    # 데이터프레임이 비어있는지 다시 확인
    if combined_df.empty:
        st.error("데이터프레임이 비어있어 그래프를 그릴 수 없습니다. 데이터 로딩 결과를 확인해 주세요.")
        return pd.DataFrame() # 확실히 빈 DataFrame 반환

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
        # 데이터가 비어있지 않은지 다시 확인
        if not df_market_cap[col].empty:
            fig.add_trace(go.Scatter(x=df_market_cap.index, y=df_market_cap[col], mode='lines', name=col))
        else:
            st.warning(f"Warning: '{col}'의 데이터가 비어있어 그래프에 포함되지 않습니다.")


    fig.update_layout(
        title="전 세계 시가총액 Top 20 기업의 5년간 종가 변화",
        xaxis_title="날짜",
        yaxis_title="종가 (USD)",
        hovermode="x unified",
        legend_title="기업",
        height=600,
        template="plotly_dark"
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
