import streamlit as st

st.set_page_config(page_title="MBTI 선물 추천기 🎁", page_icon="🎁")

st.title("🎁 MBTI 선물 추천기")
st.write("당신의 성격에 어울리는 선물을 추천해드릴게요 😊")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("👇 당신의 MBTI를 선택해주세요!", [""] + mbti_types)

recommendations = {
    "ISTJ": {
        "gift": "🗂️ 고급 다이어리",
        "reason": "체계적이고 계획적인 ISTJ에게는 실용적인 다이어리가 제격이에요.",
        "personality": "현실적이고 신중하며 책임감이 강해요. 규칙을 잘 지키고 믿을 수 있는 타입이에요."
    },
    "ISFJ": {
        "gift": "🕯️ 향초 세트",
        "reason": "따뜻하고 배려심 깊은 ISFJ에겐 마음을 녹이는 향초가 어울려요.",
        "personality": "조용하고 온화하지만 헌신적이에요. 남을 돕는 걸 좋아하고 책임감이 강한 성격이에요."
    },
    "INFJ": {
        "gift": "📖 명상책 또는 저널",
        "reason": "깊은 내면의 세계를 가진 INFJ에겐 감성을 자극하는 책이 좋아요.",
        "personality": "통찰력 있고 조용하며 깊은 사고를 즐기는 이상주의자예요."
    },
    "INTJ": {
        "gift": "⌚ 스마트워치",
        "reason": "효율성과 기술을 중시하는 INTJ에겐 스마트워치가 딱이에요.",
        "personality": "분석적이고 독립적인 사고를 중시하며 목표 지향적인 전략가예요."
    },
    "ISTP": {
        "gift": "🛠️ 멀티툴 키트",
        "reason": "실용성과 손재주를 겸비한 ISTP에게 딱 좋은 선물이에요.",
        "personality": "실용적이고 조용한 관찰자예요. 논리적이고 유연해요."
    },
    "ISFP": {
        "gift": "🎨 수채화 도구 세트",
        "reason": "예술적인 감성을 지닌 ISFP에게 창의적인 도구가 잘 어울려요.",
        "personality": "따뜻하고 섬세하며 조용한 예술가 타입이에요."
    },
    "INFP": {
        "gift": "🧸 핸드메이드 인형",
        "reason": "감성적이고 따뜻한 마음을 가진 INFP에게는 감정을 담은 선물이 좋아요.",
        "personality": "창의적이고 이상을 중시하며 깊은 감정을 지닌 성격이에요."
    },
    "INTP": {
        "gift": "🔍 퍼즐 게임",
        "reason": "지적인 도전을 좋아하는 INTP에게는 머리를 쓰는 선물이 좋아요.",
        "personality": "논리적이고 분석적인 사색가예요. 지적 호기심이 풍부해요."
    },
    "ESTP": {
        "gift": "🎮 휴대용 게임기",
        "reason": "활동적이고 즉흥적인 ESTP는 즐거움을 주는 기기가 좋아요.",
        "personality": "활동적이고 대담한 리스크 테이커예요."
    },
    "ESFP": {
        "gift": "📸 인스탁스 카메라",
        "reason": "즐거운 순간을 사랑하는 ESFP에게 즉석 사진기는 최고의 선물!",
        "personality": "사교적이고 감각적인 타입이에요. 현재를 즐기는 걸 좋아해요."
    },
    "ENFP": {
        "gift": "✈️ 여행 상품권",
        "reason": "새로운 경험을 즐기는 ENFP에게는 자유로운 여행이 최고의 선물이죠!",
        "personality": "열정적이고 상상력이 풍부한 성격이에요."
    },
    "ENTP": {
        "gift": "🎤 무선 마이크",
        "reason": "아이디어가 넘치는 ENTP에겐 표현할 수 있는 선물이 어울려요.",
        "personality": "호기심 많고 말재주 있는 토론가예요. 도전을 즐겨요."
    },
    "ESTJ": {
        "gift": "🧳 정리정돈 수납함 세트",
        "reason": "체계적이고 리더십 강한 ESTJ는 깔끔한 정리를 좋아해요.",
        "personality": "현실적이고 체계적인 성격이에요."
    },
    "ESFJ": {
        "gift": "🍱 도시락 용기 세트",
        "reason": "주변 사람들을 챙기는 ESFJ에겐 따뜻함이 담긴 실용적인 선물이 좋아요.",
        "personality": "사교적이고 따뜻한 성격이에요. 조화를 중시해요."
    },
    "ENFJ": {
        "gift": "📅 맞춤형 플래너",
        "reason": "사람들을 이끄는 ENFJ에게는 리더십을 뒷받침하는 도구가 좋아요.",
        "personality": "타인을 이끄는 리더형이며, 타인의 성장을 돕는 걸 즐겨요."
    },
    "ENTJ": {
        "gift": "💼 고급 비즈니스 가방",
        "reason": "카리스마 넘치는 ENTJ에겐 성공을 상징하는 고급스러운 선물이 잘 어울려요.",
        "personality": "결단력 있고 지도력 있는 성격이에요. 효율성과 성공을 중시해요."
    }
}

if mbti:
    st.subheader(f"🎁 {mbti} 유형 추천 선물")
    st.markdown(f"**{recommendations[mbti]['gift']}**")
    st.info(recommendations[mbti]['reason'])

    st.subheader("🧠 성격 유형 설명")
    st.success(recommendations[mbti]['personality'])

