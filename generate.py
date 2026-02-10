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
    {"name": "무선 블루투스 이어폰", "desc": "일상·업무용으로 많이 선택되는 제품", "link": "https://example.com"},
    {"name": "노트북 거치대", "desc": "장시간 작업 시 자세 개선", "link": "https://example.com"},
    {"name": "USB-C 멀티 허브", "desc": "노트북 확장에 필수", "link": "https://example.com"}
]

news_html = []
for n in news_list:
    news_html.append(
        f'<div class="news-item">'
        f'<span class="source">{n["source"]}</span>'
        f'<a href="{n["link"]}" target="_blank">{n["title"]}</a>'
        f'</div>'
    )

product_html = []
for p in products:
    product_html.append(
        f'<div class="product-card">'
        f'<h3>{p["name"]}</h3>'
        f'<p>{p["desc"]}</p>'
        f'<a href="{p["link"]}" target="_blank">자세히 보기</a>'
        f'</div>'
    )

html_parts = [
    "<!DOCTYPE html>",
    "<html lang='ko'>",
    "<head>",
    "<meta charset='UTF-8'>",
    "<title>IT 뉴스 브리핑</title>",
    "<link href='https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap' rel='stylesheet'>",
    "<style>",
    "body { margin:0; font-family:'Pretendard',sans-serif; background:#f5f6f8; color:#222; }",
    ".wrap { max-width:960px; margin:auto; padding:40px 20px; }",
    ".news-item { background:#fff; padding:18px 22px; border-radius:12px; margin-bottom:14px; box-shadow:0 4px 10px rgba(0,0,0,.04); }",
    ".source { font-size:13px; color:#888; margin-bottom:6px; display:block; }",
    ".products { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:18px; }",
    ".product-card { background:#fff; padding:22px; border-radius:14px; box-shadow:0 6px 14px rgba(0,0,0,.05); }",
    "</style>",
    "</head>",
    "<body>",
    "<div class='wrap'>",
    "<h1>IT 뉴스 브리핑</h1>",
    f"<div class='time'>업데이트: {now.strftime('%Y-%m-%d %H:%M')}</div>",
    "<h2>최신 뉴스</h2>",
    *news_html,
    "<h2>관련 제품</h2>",
    "<div class='products'>",
    *product_html,
    "</div>",
    "<footer>© 2026 IT News Brief</footer>",
    "</div>",
    "</body>",
    "</html>"
]

html = "\n".join(html_parts)

os.makedirs("_site", exist_ok=True)
with open("_site/index.html", "w", encoding="utf-8") as f:
    f.write(html)
