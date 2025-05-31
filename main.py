import streamlit as st
import random

st.set_page_config(page_title="MBTI 음식 추천기 🍽️", page_icon="🍜")

# MBTI 목록
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# MBTI 설명
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
    "ENTJ": "단호하고 효율적인 지도자"
}

# 음식 추천
recommendations = {
    "ISTJ": {"food": "🍖 삼겹살", "reason": "불판 위의 질서를 사랑하는 당신에게 삼겹살! 언제나 실패 없는 선택."},
    "ISFJ": {"food": "🥘 된장찌개", "reason": "정 많은 ISFJ에게는 따끈한 된장찌개가 딱!"},
    "INFJ": {"food": "🍵 비건 샐러드", "reason": "의미 있는 선택을 중시하는 INFJ에게는 몸과 마음이 정화되는 비건 샐러드."},
    "INTJ": {"food": "🍷 스테이크 & 와인", "reason": "고급진 식사와 전략적 사고가 찰떡인 INTJ!"},
    "ISTP": {"food": "🍜 일본식 라멘", "reason": "조용하고 깊은 맛의 라멘처럼 독립적인 당신에게."},
    "ISFP": {"food": "🍦 젤라또", "reason": "감성적이고 섬세한 ISFP에게는 부드럽고 달콤한 젤라또."},
    "INFP": {"food": "🍫 수제 초콜릿", "reason": "감정을 담은 초콜릿처럼 이상주의자 INFP에게 딱!"},
    "INTP": {"food": "☕ 아메리카노 & 크로와상", "reason": "사색과 분석에 잘 어울리는 깔끔한 조합!"},
    "ESTP": {"food": "🌮 타코", "reason": "모험을 좋아하는 ESTP에게 다양한 맛의 타코를!"},
    "ESFP": {"food": "🍓 딸기 케이크", "reason": "파티의 주인공 ESFP에게는 사랑스러운 비주얼의 케이크!"},
    "ENFP": {"food": "🍕 피자", "reason": "모두와 함께 먹는 피자는 ENFP의 활기찬 에너지와 찰떡!"},
    "ENTP": {"food": "🌯 부리또", "reason": "다양한 아이디어가 가득한 ENTP에게 부리또처럼 꽉 찬 구성!"},
    "ESTJ": {"food": "🍛 카레라이스", "reason": "빠르고 효율적인 식사엔 실속파 ESTJ에게 카레!"},
    "ESFJ": {"food": "🥗 샐러드볼", "reason": "균형감 있고 따뜻한 매력의 ESFJ에게 건강한 샐러드!"},
    "ENFJ": {"food": "🍲 전골", "reason": "다 함께 나눌 수 있는 전골은 따뜻한 리더 ENFJ에게!"},
    "ENTJ": {"food": "🥩 프라임 립", "reason": "강렬하고 고급진 선택, 리더 ENTJ에게 딱 어울려요!"}
}

# 이모지 폭죽 효과
emoji_effects = ["🎉", "✨", "💥", "🎊", "🔥", "🌟", "🎈", "💫", "🍀", "💖", "🧚", "😻"]

# UI
st.title("🍽️ MBTI 음식 추천기")
st.write("당신의 성격에 어울리는 음식을 추천해드릴게요 😋")

mbti = st.selectbox("👇 당신의 MBTI를 선택해주세요!", [""] + mbti_types)

# 결과 표시
if mbti:
    # 이모지 효과
    burst = " ".join(random.choices(emoji_effects, k=20))
    st.markdown(f"<div style='font-size:28px'>{burst}</div>", unsafe_allow_html=True)

    # MBTI 설명
    st.markdown(f"### 🧠 당신은 **{mbti}** 유형이에요!")
    st.write(f"📝 {mbti_descriptions[mbti]}")

    # 음식 추천
    st.subheader("🍱 추천 음식")
    st.markdown(f"**{recommendations[mbti]['food']}**")
    st.info(recommendations[mbti]['reason'])
