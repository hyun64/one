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
# mbti_career_app.py
import streamlit as st

# MBTI에 따른 직업 및 설명 사전
mbti_jobs = {
    "INTJ 🧠✨": {
        "데이터 과학자 📊": "복잡한 데이터를 분석하여 전략을 수립하는 전문가예요. 논리적인 사고를 좋아하는 INTJ에게 딱이에요!",
        "AI 연구원 🤖": "인공지능의 미래를 여는 연구자. 끊임없이 새로운 지식을 탐구하는 성향과 잘 맞아요!",
        "전략 컨설턴트 📈": "기업의 문제를 해결해주는 전략가. 분석력과 계획력을 가진 INTJ에게 적합해요."
    },
    "INFP 🌸🎨": {
        "작가 ✍️": "감성을 글로 풀어내는 직업. 자기 표현을 중요시하는 INFP에게 잘 어울려요.",
        "심리상담사 🧘": "사람의 마음을 이해하고 돕는 역할. 공감 능력이 뛰어난 INFP에게 추천해요.",
        "예술가 🎭": "자신의 감정을 예술로 표현해요. 창의성과 감수성이 풍부한 INFP에게 제격이에요."
    },
    "ESFP 🎉🌟": {
        "이벤트 플래너 🎪": "사람들과 함께 즐길 수 있는 이벤트를 기획해요. 활기찬 성격의 ESFP에게 잘 맞아요!",
        "마케터 📣": "트렌디한 감각으로 사람들의 관심을 끌어요. 외향적인 성격이 강점이에요.",
        "배우 🎬": "자신을 표현하고 다양한 역할을 소화해요. 무대에서 빛나는 ESFP라면 도전해볼 만해요!"
    },
    # 다른 MBTI 유형도 동일하게 확장 가능
}

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천 ✨", layout="centered")

# 타이틀
st.markdown("""
    <h1 style='text-align: center; color: #FF69B4;'>💫 MBTI 진로 추천기 💫</h1>
    <h3 style='text-align: center; color: #9370DB;'>당신의 성격 유형에 어울리는 직업을 찾아보세요! 🎯</h3>
    """, unsafe_allow_html=True)

# MBTI 선택
mbti_selected = st.selectbox("당신의 MBTI 유형을 선택해주세요 💁‍♀️", list(mbti_jobs.keys()))

# 추천 직업 토글 출력
if mbti_selected:
    st.markdown("---")
    st.markdown(f"### 🧬 <span style='color:#20B2AA'>[{mbti_selected}]</span>에게 추천하는 직업은...!", unsafe_allow_html=True)

    # 직업 별로 expander 사용
    for job, description in mbti_jobs[mbti_selected].items():
        with st.expander(f"💼 {job}"):
            st.markdown(f"📝 {description}")

    st.markdown("🎓 **각 직업을 눌러서 자세한 설명을 확인해보세요!**")
    st.balloons()  # 풍선 애니메이션

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center;'>✨ Made with ❤️ by [YourName] ✨</p>", unsafe_allow_html=True)
