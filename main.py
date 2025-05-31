import streamlit as st
import random

st.set_page_config(page_title="MBTI 음식 추천기 🍽️", page_icon="🍜")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti_descriptions = {
    "ISTJ": "신중하고 책임감이 강한 현실주의자",
    "ISFJ": "따뜻하고 헌신적인 조력자",
    "INFJ": "통찰력 있고 이상을 추구하는 조용한 리더",
    "INTJ": "전략적이고 독립적인 계획자",
    "ISTP": "냉철하고 유연한 문제 해결사",
    "ISFP": "감성적이고 자유로운 예술가",
    "INFP": "이상과 감성이 풍부한 중재자",
    "INTP": "논리적이고 창의적인 사색가",
    "ESTP": "에너지 넘치고 즉흥적인 활동가",
    "ESFP": "사교적이고 즐거움을 추구하는 연예인",
    "ENFP": "열정적이고 창의적인 활동가",
    "ENTP": "아이디어가 넘치는 토론가",
    "ESTJ": "체계적이고 실용적인 관리자",
    "ESFJ": "친절하고 따뜻한 사교가",
    "ENFJ": "타인을 이끄는 따뜻한 리더",
