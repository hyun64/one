# article_parser.py
from newspaper import Article

def get_article_text(url):
    article = Article(url, language='ko')  # 언어 설정 필요 시 변경
    article.download()
    article.parse()
    return article.title, article.text
# summarizer.py
from transformers import pipeline

# BART 모델 로딩 (한국어 뉴스에는 영어보다 성능 떨어질 수 있음. 한국어 모델은 아래에 추천)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_length=130, min_length=30):
    if len(text.split()) < 50:
        return "요약할 수 있는 충분한 텍스트가 없습니다."
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
# app.py
import streamlit as st
from article_parser import get_article_text
from summarizer import summarize_text

st.set_page_config(page_title="뉴스 요약기", layout="centered")

st.title("📰 뉴스 요약기 (Streamlit)")

url = st.text_input("뉴스 기사 URL을 입력하세요:")

if st.button("요약하기") and url:
    with st.spinner("뉴스를 불러오고 요약하는 중입니다..."):
        try:
            title, article_text = get_article_text(url)
            summary = summarize_text(article_text)

            st.subheader("📰 기사 제목")
            st.write(title)

            st.subheader("✏️ 요약 결과")
            st.success(summary)

            with st.expander("원본 기사 보기"):
                st.text_area("본문", article_text, height=300)
        except Exception as e:
            st.error(f"문제가 발생했습니다: {e}")


