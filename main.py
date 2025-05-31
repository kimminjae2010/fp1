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
    # ... (생략 없이 그대로 넣으세요)
}

recommendations = {
    # ... (생략 없이 그대로 넣으세요)
}

emoji_effects = ["🎉", "✨", "💥", "🎊", "🔥", "🌟", "🎈", "💫", "🍀", "💖", "🧚", "😻"]

# 초기 타이틀, 선택란
st.title("🍽️ MBTI 음식 추천기")
st.write("당신의 성격에 어울리는 음식을 추천해드릴게요 😋")
mbti = st.selectbox("👇 당신의 MBTI를 선택해주세요!", [""] + mbti_types)

# 선택 이후만 결과 보여주기
if mbti:
    st.markdown(f"### 🧠 당신은 **{mbti}** 유형이에요!")
    st.write(f"📝 {mbti_descriptions[mbti]}")

    # 이모지 터뜨리기 효과
    burst = " ".join(random.choices(emoji_effects, k=20))
    st.markdown(f"<div style='font-size:28px'>{burst}</div>", unsafe_allow_html=True)

    # 추천 음식
    st.subheader("🍽️ 추천 음식")
    st.markdown(f"**{recommendations[mbti]['food']}**")
    st.info(recommen
