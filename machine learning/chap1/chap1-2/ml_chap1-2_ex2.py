from bs4 import BeautifulSoup

html="""
<html><body>
 <h1 id = "title">스크레이핑이란?</h1>
 <p id="body">웹 페이지를 분석하는 것</p>
 <p>원하는 부분을 추출</p>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

title= soup.find(id="title")
body= soup.find(id="body")
print(title)
print("#title="+ title.string)  # string 텍스트만 가져온다.
print("#body=" + body.string)

