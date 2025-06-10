from transformers import pipeline

# 영어 뉴스 요약 모델 (한국어 뉴스도 어느 정도 요약 가능)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_length=130, min_length=30):
    if len(text.split()) < 50:
        return "요약할 수 있는 충분한 텍스트가 없습니다."
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
