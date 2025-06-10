from newspaper import Article

def get_article_text(url):
    article = Article(url, language='ko')  # 한국어 뉴스용
    article.download()
    article.parse()
    return article.title, article.text
