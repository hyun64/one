import streamlit as st
from article_parser import get_article_text
from summarizer import summarize_text

st.set_page_config(page_title="뉴스 요약기", layout="centered")
st.title("📰 뉴스 요약기")

url = st.text_input("뉴스 기사 URL을 입력하세요:")

if st.button("요약하기") and url:
    with st.spinner("뉴스를 불러오고 요약하는 중입니다..."):
        try:
            title, content = get_article_text(url)
            summary = summarize_text(content)

            st.subheader("📰 기사 제목")
            st.write(title)

            st.subheader("✏️ 요약 결과")
            st.success(summary)

            with st.expander("📄 원문 기사 보기"):
                st.text_area("본문", content, height=300)

        except Exception as e:
            st.error(f"오류 발생: {e}")



