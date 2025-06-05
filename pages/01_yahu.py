import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 제목
st.title("글로벌 시가총액 TOP10 기업 - 최근 1년간 주가 변화")

# 기업 티커 리스트
top10_tickers = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "BRK-B", "TSM", "LLY", "AVGO"]

# 데이터 수집 기간
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 데이터 다운로드
@st.cache_data
def load_data(tickers):
    data = yf.download(tickers, start=start_date, end=end_date)["Adj Close"]
    return data

data = load_data(top10_tickers)

# Plotly 시각화
fig = go.Figure()

for ticker in top10_tickers:
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data[ticker],
        mode='lines',
        name=ticker
    ))

fig.update_layout(
    title="최근 1년간 글로벌 시가총액 TOP10 기업 주가 변화 (Adjusted Close)",
    xaxis_title="날짜",
    yaxis_title="주가 (USD)",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
