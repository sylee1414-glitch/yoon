import streamlit as st
st.set_page_config(page_title="홈페이지", page_icon="🏠")
st.title('나의 첫 웹 서비스 만들기!')
name = st.text_input('이름을 입력해주세요: ')
menu = st.selectbox('좋아하는 음식을 선택해주세요: ', ['슈팅스타', '아몬드봉봉'])
if st.button('인사말 생성') :
  st.write(name+'님! 당신이 좋아하는 음식은 '+menu+'이군요?! 저도 좋아요!!')
