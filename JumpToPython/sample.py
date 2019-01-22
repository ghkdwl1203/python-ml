from bs4 import BeautifulSoup
import urllib.request as req

url="http://news.einfomax.co.kr/news/articleView.html?idxno=4004050"

res = req.urlopen(url).read()  #
soup = BeautifulSoup(res,"html.parser")


title= soup.find("article-view-content-div")
#select_one(".usd").select_one(".value").string
ul= soup.select_one(".user-content").select_one("div#article-view-content-div")
print(ul)