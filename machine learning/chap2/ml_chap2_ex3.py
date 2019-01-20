from bs4 import BeautifulSoup

html = """
<html><body>
<ul>
<li><a href="http://www.naver.com">naver</a></li>
<li><a href="http://www.daum.net">daum</a></li>
</ul>
</body></html> 
"""


soup = BeautifulSoup(html, 'html.parser')
links= soup.find_all("a")

for a in links:
    href = a.attrs['href'] # attrs 속성
    text = a.string
    print(text, ">",href)

print(soup.prettify())
a = soup.li.a
print(type(a.attrs))
print(a)
print('href' in a.attrs)
print(a['href'])