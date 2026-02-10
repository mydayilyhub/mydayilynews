import os
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

# 시간 (KST)
now = datetime.utcnow() + timedelta(hours=9)

# 뉴스 소스 (예시: 네이버 IT 뉴스)
NEWS_URL = "https://news.naver.com/section/105"

def fetch_news():
    res = requests.get(NEWS_URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    items = []
    for a in soup.select("a.sa_text_title")[:5]:
        title = a.get_text(strip=True)
        link = a["href"]
        items.append((title, link))
    return items

news = fetch_news()

html_news = ""
for title, link in news:
    html_news += f"""
    <li>
      <a href="{link}" target="_blank">{title}</a>
    </li>
    """

html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>자동 수익 콘텐츠 시스템</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
  <style>
    body {{
      font-family: 'Noto Sans KR', sans-serif;
      background: #f4f6f8;
      padding: 40px;
    }}
    .container {{
      max-width: 900px;
      margin: auto;
      background: white;
      padding: 32px;
      border-radius: 16px;
      box-shadow: 0 10px 30px rgba(0,0,0,.08);
    }}
    h1 {{ margin-top: 0; }}
    ul {{ padding-left: 20px; }}
    li {{ margin-bottom: 10px; }}
    .time {{ color: #666; font-size: 14px; }}
    footer {{ margin-top: 40px; color: #999; font-size: 13px; }}
  </style>
</head>
<body>
  <div class="container">
    <h1>🤖 자동 생성 콘텐츠 사이트</h1>
    <p class="time">마지막 업데이트: {now.strftime("%Y-%m-%d %H:%M:%S")} KST</p>

    <h2>📰 오늘의 IT 뉴스</h2>
    <ul>
      {html_news}
    </ul>

    <footer>
      이 페이지는 자동으로 생성됩니다.<br>
      방문자는 별도 가입 없이 정보를 열람할 수 있습니다.
    </footer>
  </div>
</body>
</html>
"""

os.makedirs("_site", exist_ok=True)
with open("_site/index.html", "w", encoding="utf-8") as f:
    f.write(html)
