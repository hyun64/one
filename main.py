# mbti_career_app.py
import streamlit as st

# 이모지와 함께 MBTI에 따른 직업 추천 딕셔너리
mbti_jobs = {
    "INTJ 🧠✨": ["데이터 과학자 📊", "AI 연구원 🤖", "전략 컨설턴트 📈"],
    "INFP 🌸🎨": ["작가 ✍️", "심리상담사 🧘", "예술가 🎭"],
    "ESFP 🎉🌟": ["이벤트 플래너 🎪", "마케터 📣", "배우 🎬"],
    "ENTP 💡🚀": ["스타트업 창업가 🧑‍💼", "광고 기획자 🎯", "기술 컨설턴트 💼"],
    "ISTJ 📏📚": ["회계사 💼", "공무원 🏛️", "엔지니어 🛠️"],
    "ENFP 🌈🔥": ["브랜드 디자이너 🎨", "강연가 🎤", "프로젝트 매니저 📋"],
    "ISFJ 🧸🌼": ["간호사 🏥", "교사 👩‍🏫", "사회복지사 🤝"],
    "ESTP 🎮🕶️": ["세일즈 매니저 💼", "응급 구조사 🚑", "파일럿 ✈️"],
    # 필요에 따라 다른 MBTI도 추가 가능
}

# 🎨 페이지 구성
st.set_page_config(page_title="MBTI 진로 추천 ✨", layout="centered")

# 🌟 타이틀
st.markdown("""
    <h1 style='text-align: center; color: #FF69B4;'>💫 MBTI 진로 추천기 💫</h1>
    <h3 style='text-align: center; color: #9370DB;'>당신의 성격 유형에 어울리는 직업을 찾아보세요! 🎯</h3>
    """, unsafe_allow_html=True)

# 🔍 MBTI 선택
mbti_selected = st.selectbox("당신의 MBTI 유형을 선택해주세요 💁‍♀️", list(mbti_jobs.keys()))

# 🎁 추천 결과
if mbti_selected:
    st.markdown("---")
    st.markdown(f"### 🧬 <span style='color:#20B2AA'>[{mbti_selected}]</span>에게 추천하는 직업은...!", unsafe_allow_html=True)
    for job in mbti_jobs[mbti_selected]:
        st.markdown(f"- {job}")

    st.markdown("🎓 **이 직업들은 당신의 성향과 잘 맞을 수 있어요!**")
    st.balloons()  # 🎈 풍선 애니메이션

# 🌟 푸터
st.markdown("---")
st.markdown("<p style='text-align: center;'>✨ Made with ❤️ by [YourName] ✨</p>", unsafe_allow_html=True)
