hist = vt.history(period="3y")
df = hist.reset_index()

import plotly.express as px
fig = px.line(df, x='Date', y='Close', title="VT ETF 종가 변화 (3년간)")
st.plotly_chart(fig, use_container_width=True)
