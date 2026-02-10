import os
import feedparser
from datetime import datetime, timedelta

now = datetime.utcnow() + timedelta(hours=9)

NEWS_SOURCES = {
    "네이버 IT": "https://rss.etnews.com/Section901.xml",
    "연합뉴스 IT": "https://www.yna.co.kr/rss/it.xml",
    "ZDNet Korea": "https://feeds.feedburner.com/zdkorea",
    "블로터": "https://www.bloter.net/feed"
}

def fetch_news():
    articles = []
    for source, url in NEWS_SOURCES.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            articles.append({
                "source": source,
                "title": entry.title,
                "link": entry.link
            })
    return articles

news_list = fetch_news()

products = [
    {
        "name": "무선 블루투스 이어폰",
        "desc": "일상·업무용으로 많이 선택되는 제품",
        "link": "https://example.com"
    },
    {
        "name": "노트북 거치대",
        "desc": "장시간 작업 시 자세 개선",
        "link": "https://example.com"
    },
    {
        "name": "USB-C 멀티 허브",
        "desc": "노트북 확장에 필수",
        "link": "https://example.com"
    }
]

news_html = ""
for n in news_list:
    news_html += f"""
    <div class="news-item">
      <span class="source">{n['source']}</span>
      <a href="{n['link']}" target="_blank">{n['title']}</a>
    </div>
    """

product_html = ""
for p in products:
    product_html += f"""
    <div class="product-card">
      <h3>{p['name']}</h3>
      <p>{p['desc']}</p>
      <a href="{p['link']}" target="_blank">자세히 보기</a>
    </div>
    """

html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>IT 뉴스 브리핑</title>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    body {{
      margin: 0;
      font-family: 'Pretendard', sans-serif;
      background: #f5f6f8;
      color: #222;
    }}
    .wrap {{
      max-width: 960px;
      margin: auto;
      padding: 40px 20px;
    }}
    h1 {{
      font-size: 28px;
      margin-bottom: 8px;
    }}
    .time {{
      font-size: 14px;
      color: #777;
      margin-bottom: 40px;
    }}
    .section {{
      margin-bottom: 56px;
    }}
    .news-item {{
      background: #fff;
