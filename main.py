import streamlit as st

st.set_page_config(page_title="MBTI 음식 추천기 🍱", page_icon="🍜")

st.title("🍽️ MBTI 음식 추천기")
st.write("당신의 MBTI에 맞는 음식은 무엇일까요? 😋")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_types)

recommendations = {
    "ISTJ": "🍖 삼겹살 - 체계적인 당신에게 어울리는 한국인의 소울푸드!",
    "ISFJ": "🥘 된장찌개 - 따뜻하고 조용한 매력을 닮은 전통 음식!",
    "INFJ": "🍵 비건 샐러드 - 깊은 생각을 닮은 건강한 한 끼",
    "INTJ": "🍷 스테이크 & 와인 - 고급스럽고 전략적인 당신에게 딱!",
    "ISTP": "🍜 라멘 - 혼자만의 시간에 즐기기 좋은 따끈한 국물",
    "ISFP": "🍦 젤라또 - 감성을 자극하는 달콤한 휴식!",
    "INFP": "🍫 수제 초콜릿 - 상상력이 풍부한 당신의 달콤한 에너지",
    "INTP": "☕ 아메리카노 & 크로와상 - 조용히 사색하며 즐기기 좋은 조합",
    "ESTP": "🌮 타코 - 활동적인 당신에게 어울리는 다채로운 맛!",
    "ESFP": "🍓 딸기 케이크 - 인싸력 만렙! 눈과 입이 모두 즐거워요!",
    "ENFP": "🍕 피자 - 어디서든 분위기를 띄우는 당신에게 찰떡!",
    "ENTP": "🌯 부리또 - 자유롭고 창의적인 당신의 여행 식사",
    "ESTJ": "🍛 카레라이스 - 실용적이고 든든한 당신의 한 끼",
    "ESFJ": "🥗 샐러드볼 - 타인을 배려하는 당신의 건강한 선택",
    "ENFJ": "🍲 전골 - 모두를 챙기는 당신에게 잘 어울리는 푸짐한 음식",
    "ENTJ": "🥩 프라임 립 - 리더십 넘치는 당신의 당당한 선택"
}

if mbti:
    st.subheader(f"🔍 {mbti} 유형 추천 음식")
    st.success(recommendations[mbti])
