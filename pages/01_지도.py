import streamlit as st
import folium
from streamlit.components.v1 import html

st.set_page_config(page_title="한국인이 사랑하는 여행지 Top 10", layout="wide")

st.title("🇰🇷 한국인이 사랑하는 여행지 Top 10")
st.markdown("사랑하는 사람과 함께 걷고 싶은 그 곳들... 💕\n\n가슴 속에 오래도록 남을 한국의 아름다운 여행지들을 소개합니다.")

# 여행지 목록 (위도, 경도 포함)
travel_spots = [
    {"name": "제주도", "lat": 33.4996, "lon": 126.5312, "desc": "자연이 숨 쉬는 섬, 제주 🍊 한라산과 푸른 바다, 그리고 따뜻한 정이 있는 곳."},
    {"name": "경주", "lat": 35.8562, "lon": 129.2247, "desc": "천년의 고도 경주 🌸 역사의 숨결을 따라 걷다 보면 마음도 함께 물들어요."},
    {"name": "부산 해운대", "lat": 35.1587, "lon": 129.1604, "desc": "푸른 바다와 낭만이 흐르는 해운대 🌊 설레는 여름 밤의 추억이 시작돼요."},
    {"name": "강릉", "lat": 37.7521, "lon": 128.8761, "desc": "커피향 가득한 동해의 낭만 강릉 ☕ 바다와 산이 어우러진 힐링의 도시."},
    {"name": "남해", "lat": 34.8371, "lon": 127.8924, "desc": "작은 유럽 같은 남해 🏞️ 다랭이 마을과 푸른 바다가 반겨줘요."},
    {"name": "속초", "lat": 38.2044, "lon": 128.5912, "desc": "설악산과 바다가 어우러진 속초 🌄 자연과 함께하는 평온한 시간."},
    {"name": "전주", "lat": 35.8242, "lon": 127.1480, "desc": "한옥과 비빔밥의 도시 전주 🏮 전통과 맛의 향연이 펼쳐져요."},
    {"name": "서울 북촌", "lat": 37.5826, "lon": 126.9831, "desc": "시간이 멈춘 듯한 골목, 북촌 한옥마을 🏘️ 도심 속 따스한 전통의 숨결."},
    {"name": "인천 차이나타운", "lat": 37.4736, "lon": 126.6169, "desc": "다문화의 향기가 느껴지는 차이나타운 🏮 색다른 매력이 있는 도시 여행."},
    {"name": "담양", "lat": 35.3211, "lon": 126.9876, "desc": "죽녹원 속 초록 쉼표, 담양 🎋 대나무 숲에서 느끼는 청량한 힐링."}
]

# 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

# 마커 추가
for spot in travel_spots:
    folium.Marker(
        [spot["lat"], spot["lon"]],
        popup=f"<b>{spot['name']}</b><br>{spot['desc']}",
        tooltip=spot["name"],
        icon=folium.Icon(color="pink", icon="heart")
    ).add_to(m)

# 지도 렌더링
folium_html = m._repr_html_()
st.markdown("### 📍 여행지 지도")
html(folium_html, height=600)

# 사랑스러운 소개 리스트
st.markdown("### 💖 여행지 소개")
for spot in travel_spots:
    with st.expander(f"✨ {spot['name']}"):
        st.markdown(f"🌸 {spot['desc']}")

