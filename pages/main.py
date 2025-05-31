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
        "reason": "체계적이고 신뢰할 수 있는 ISTJ에게는 언제나 실패 없는 삼겹살이 딱! 불판 위의 질서도 놓치지 않죠.",
        "personality": "현실적이고 신중하며 책임감이 강해요. 규칙을 잘 지키고 믿을 수 있는 타입이에요."
    },
    "ISFJ": {
        "food": "🥘 된장찌개",
        "reason": "배려심 깊고 따뜻한 ISFJ에게는 한국인의 소울푸드 된장찌개! 정 많은 그대에게 어울리는 진한 국물.",
        "personality": "조용하고 온화하지만 헌신적이에요. 남을 돕는 걸 좋아하고 책임감이 강한 성격이에요."
    },
    "INFJ": {
        "food": "🍵 비건 샐러드",
        "reason": "깊은 내면과 직관을 가진 INFJ는 의미 있는 선택을 좋아해요. 몸과 마음을 모두 채워주는 비건 샐러드 추천!",
        "personality": "통찰력 있고 조용하며 깊은 사고를 즐기는 이상주의자예요. 타인을 위한 비전을 품고 있어요."
    },
    "INTJ": {
        "food": "🍷 스테이크 & 와인",
        "reason": "전략가형 INTJ는 고급스럽고 효율적인 걸 좋아하죠. 완벽하게 구운 스테이크와 와인으로 멋진 식사를!",
        "personality": "분석적이고 독립적인 사고를 중시하며 목표 지향적인 전략가예요."
    },
    "ISTP": {
        "food": "🍜 일본식 라멘",
        "reason": "혼자만의 시간도 잘 즐기는 ISTP는 깊은 맛의 라멘처럼 조용하지만 강한 매력을 지녔어요.",
        "personality": "실용적이고 조용한 관찰자예요. 논리적이고 유연하며 즉각적인 행동을 좋아해요."
    },
    "ISFP": {
        "food": "🍦 젤라또",
        "reason": "감성적이고 예술적인 ISFP에겐 감각적인 젤라또가 어울려요. 부드럽고 달콤한 시간 💕",
        "personality": "따뜻하고 섬세하며 조용한 예술가 타입이에요. 자유로운 표현을 즐겨요."
    },
    "INFP": {
        "food": "🍫 수제 초콜릿",
        "reason": "이상주의자 INFP에게는 감정을 담은 수제 초콜릿! 달콤한 상상력이 피어납니다 🍫✨",
        "personality": "창의적이고 이상을 중시하며 깊은 감정을 지닌 성격이에요. 가치에 따라 행동해요."
    },
    "INTP": {
        "food": "☕ 아메리카노 & 크로와상",
        "reason": "사색가 INTP는 커피 한 잔과 철학적인 고찰이 찰떡. 크로와상과 함께라면 완벽!",
        "personality": "논리적이고 분석적인 사색가예요. 지적 호기심이 풍부하고 독창적인 아이디어를 좋아해요."
    },
    "ESTP": {
        "food": "🌮 타코",
        "reason": "모험을 즐기는 ESTP는 다양한 맛이 살아있는 타코가 잘 어울려요. 언제 어디서든 액션!",
        "personality": "활동적이고 대담한 리스크 테이커예요. 현실 감각이 뛰어나고 즉흥적이에요."
    },
    "ESFP": {
        "food": "🍓 딸기 케이크",
        "reason": "파티의 주인공 ESFP! 보기에도 예쁘고 맛도 좋은 딸기 케이크로 분위기 업!",
        "personality": "사교적이고 감각적인 타입이에요. 사람들과 어울리며 현재를 즐기는 걸 좋아해요."
    },
    "ENFP": {
        "food": "🍕 피자",
        "reason": "에너제틱하고 창의적인 ENFP는 다 함께 나눠 먹기 좋은 피자! 모두가 행복한 음식이에요 🍕",
        "personality": "열정적이고 상상력이 풍부한 성격이에요. 새로운 아이디어와 가능성을 추구해요."
    },
    "ENTP": {
        "food": "🌯 부리또",
        "reason": "끊임없이 아이디어를 내는 ENTP는 다양한 재료가 어우러진 부리또처럼 다채로운 매력의 소유자!",
        "personality": "호기심 많고 말재주 있는 토론가예요. 도전을 즐기고 혁신적인 아이디어를 선호해요."
    },
    "ESTJ": {
        "food": "🍛 카레라이스",
        "reason": "실용적이고 리더십 강한 ESTJ는 한 그릇으로 든든한 카레라이스가 딱! 빠르고 효율적인 식사 💪",
        "personality": "현실적이고 체계적인 성격이에요. 조직과 규율을 중요하게 생각해요."
    },
    "ESFJ": {
        "food": "🥗 샐러드볼",
        "reason": "타인을 잘 챙기는 ESFJ는 건강한 샐러드처럼 균형 잡힌 매력을 가지고 있어요 🥗💚",
        "personality": "사교적이고 따뜻한 성격이에요. 주변 사람을 챙기고 조화를 중시해요."
    },
    "ENFJ": {
        "food": "🍲 전골",
        "reason": "모두를 챙기는 따뜻한 리더 ENFJ! 함께 나눌 수 있는 전골이 어울리는 음식이에요 🍲",
        "personality": "카리스마 있고 타인을 잘 이끄는 리더형이에요. 타인의 성장을 돕는 걸 즐겨요."
    },
    "ENTJ": {
        "food": "🥩 프라임 립",
        "reason": "카리스마 넘치는 ENTJ는 고급지고 강렬한 프라임 립이 어울려요. 성공한 리더의 식사 스타일!",
        "personality": "결단력 있고 지도력 있는 성격이에요. 효율성과 성공을 중시해요."
    }
}

if mbti:
    st.subheader(f"🔍 {mbti} 유형 추천 음식")
    st.markdown(f"**{recommendations[mbti]['food']}**")
    st.info(recommendations[mbti]['reason'])

    st.subheader("🧠 성격 유형 설명")
    st.success(recommendations[mbti]['personality'])
