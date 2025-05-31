import streamlit as st

st.set_page_config(page_title="MBTI 음식 추천기 🍽️", page_icon="🍜")

st.title("🍽️ MBTI 음식 추천기")
st.write("당신의 성격에 어울리는 음식을 추천해드릴게요 😋")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("👇 당신의 MBTI를 선택해주세요!", [""] + mbti_types)

recommendations = {
    "ISTJ": {
        "food": "🍖 삼겹살",
        "reason": "체계적이고 신뢰할 수 있는 ISTJ에게는 언제나 실패 없는 삼겹살이 딱! 불판 위의 질서도 놓치지 않죠."
    },
    "ISFJ": {
        "food": "🥘 된장찌개",
        "reason": "배려심 깊고 따뜻한 ISFJ에게는 한국인의 소울푸드 된장찌개! 정 많은 그대에게 어울리는 진한 국물."
    },
    "INFJ": {
        "food": "🍵 비건 샐러드",
        "reason": "깊은 내면과 직관을 가진 INFJ는 의미 있는 선택을 좋아해요. 몸과 마음을 모두 채워주는 비건 샐러드 추천!"
    },
    "INTJ": {
        "food": "🍷 스테이크 & 와인",
        "reason": "전략가형 INTJ는 고급스럽고 효율적인 걸 좋아하죠. 완벽하게 구운 스테이크와 와인으로 멋진 식사를!"
    },
    "ISTP": {
        "food": "🍜 일본식 라멘",
        "reason": "혼자만의 시간도 잘 즐기는 ISTP는 깊은 맛의 라멘처럼 조용하지만 강한 매력을 지녔어요."
    },
    "ISFP": {
        "food": "🍦 젤라또",
        "reason": "감성적이고 예술적인 ISFP에겐 감각적인 젤라또가 어울려요. 부드럽고 달콤한 시간 💕"
    },
    "INFP": {
        "food": "🍫 수제 초콜릿",
        "reason": "이상주의자 INFP에게는 감정을 담은 수제 초콜릿! 달콤한 상상력이 피어납니다 🍫✨"
    },
    "INTP": {
        "food": "☕ 아메리카노 & 크로와상",
        "reason": "사색가 INTP는 커피 한 잔과 철학적인 고찰이 찰떡. 크로와상과 함께라면 완벽!"
    },
    "ESTP": {
        "food": "🌮 타코",
        "reason": "모험을 즐기는 ESTP는 다양한 맛이 살아있는 타코가 잘 어울려요. 언제 어디서든 액션!"
    },
    "ESFP": {
        "food": "🍓 딸기 케이크",
        "reason": "파티의 주인공 ESFP! 보기에도 예쁘고 맛도 좋은 딸기 케이크로 분위기 업!"
    },
    "ENFP": {
        "food": "🍕 피자",
        "reason": "에너제틱하고 창의적인 ENFP는 다 함께 나눠 먹기 좋은 피자! 모두가 행복한 음식이에요 🍕"
    },
    "ENTP": {
        "food": "🌯 부리또",
        "reason": "끊임없이 아이디어를 내는 ENTP는 다양한 재료가 어우러진 부리또처럼 다채로운 매력의 소유자!"
    },
    "ESTJ": {
        "food": "🍛 카레라이스",
        "reason": "실용적이고 리더십 강한 ESTJ는 한 그릇으로 든든한 카레라이스가 딱! 빠르고 효율적인 식사 💪"
    },
    "ESFJ": {
        "food": "🥗 샐러드볼",
        "reason": "타인을 잘 챙기는 ESFJ는 건강한 샐러드처럼 균형 잡힌 매력을 가지고 있어요 🥗💚"
    },
    "ENFJ": {
        "food": "🍲 전골",
        "reason": "모두를 챙기는 따뜻한 리더 ENFJ! 함께 나눌 수 있는 전골이 어울리는 음식이에요 🍲"
    },
    "ENTJ": {
        "food": "🥩 프라임 립",
        "reason": "카리스마 넘치는 ENTJ는 고급지고 강렬한 프라임 립이 어울려요. 성공한 리더의 식사 스타일!"
    }
}

if mbti:
    st.subheader(f"🔍 {mbti} 유형 추천 음식")
    st.markdown(f"**{recommendations[mbti]['food']}**")
    st.info(recommendations[mbti]['reason'])
