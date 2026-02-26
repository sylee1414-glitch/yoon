import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="칼로리 트래커", page_icon="🔥")
st.title("🔥 실시간 칼로리 추적기")
st.write("오늘 먹은 음식을 입력하면 그래프가 실시간으로 업데이트됩니다!")

# 1. 데이터 저장소 초기화 (페이지가 새로고침되어도 데이터가 날아가지 않게 함)
if 'calorie_data' not in st.session_state:
    st.session_state.calorie_data = pd.DataFrame(columns=['음식명', '칼로리'])

# 2. 사용자 입력 창 (사이드바 또는 메인 화면)
with st.form("calorie_form", clear_on_submit=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        food_name = st.text_input("🍎 어떤 음식을 드셨나요?", placeholder="예: 사과, 닭가슴살")
    with col2:
        calories = st.number_input("⚡ 칼로리(kcal)", min_value=0, step=10)
    
    submit_button = st.form_submit_button("기록 추가하기")

# 3. 데이터 추가 로직
if submit_button and food_name:
    new_data = pd.DataFrame({'음식명': [food_name], '칼로리': [calories]})
    # 기존 데이터에 새 데이터 합치기
    st.session_state.calorie_data = pd.concat([st.session_state.calorie_data, new_data], ignore_index=True)
    st.success(f"'{food_name}' 기록 완료!")

# 4. 그래프 그리기
if not st.session_state.calorie_data.empty:
    df = st.session_state.calorie_data
    
    # 막대 그래프 생성
    fig = px.bar(df, x='음식명', y='칼로리', 
                 color='음식명', 
                 text='칼로리', # 막대 위에 숫자 표시
                 title="😋 오늘 섭취한 칼로리 현황")
    
    st.plotly_chart(fig, use_container_width=True)

    # 총합 표시
    total_cal = df['칼로리'].sum()
    st.metric("오늘의 총 섭취량", f"{total_cal} kcal")

    # 데이터 초기화 버튼
    if st.button("전체 초기화"):
        st.session_state.calorie_data = pd.DataFrame(columns=['음식명', '칼로리'])
        st.rerun()
else:
    st.info("아직 입력된 데이터가 없어요. 위 양식을 작성해 보세요!")
