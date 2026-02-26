import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🍦 아이스크림 선호도 조사 결과")

# 1. 가상의 데이터 만들기 (나중에 엑셀이나 DB 연결 가능)
data = pd.DataFrame({
    '메뉴': ['슈팅스타', '아몬드봉봉', '민트초코', '엄마는외계인'],
    '득표수': [15, 30, 10, 25]
})

# 2. Plotly를 이용한 막대 그래프 생성
fig = px.bar(data, x='메뉴', y='득표수', 
             title='가장 인기 있는 맛은?',
             color='메뉴', # 메뉴별로 색상 다르게
             template='plotly_white') # 깔끔한 배경 테마

# 3. Streamlit 화면에 그래프 표시
st.plotly_chart(fig)

# 4. 추가 팁: 파이 차트도 그려볼까요?
st.subheader("비중 확인하기")
fig2 = px.pie(data, values='득표수', names='메뉴', hole=0.3)
st.plotly_chart(fig2)
