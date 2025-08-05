import requests
from bs4 import BeautifulSoup

# 검색 키워드
keyword = "AI"
url = f"https://search.naver.com/search.naver?where=news&query={keyword}"

# 사용자 에이전트 설정 (크롤링 차단 방지)
headers = {
    "User-Agent": "Mozilla/5.0"
}

# 페이지 요청
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 뉴스 제목 추출
titles = soup.select(".news_tit")  # 뉴스 제목이 있는 a 태그 클래스

print(f"🔍 '{keyword}'에 대한 뉴스 제목 5개:")
print("-" * 40)

for i, title in enumerate(titles[:5], start=1):
    print(f"{i}. {title.text}")
    print(f"   ➜ 링크: {title['href']}")

