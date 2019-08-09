from bs4 import BeautifulSoup
import urllib.request as req

url="https://finance.naver.com/marketindex"

res = req.urlopen(url).read().decode("EUC-KR")  #
soup = BeautifulSoup(res,"html.parser")

title= soup.select_one("div#container")


print(title)

 print("=======================시작===================")
 li_list = soup.select_one("ul#exchangeList").select("li")
 print("환율 리스트")
 for li in li_list:
     print(li)
     h3 = li.select_one("h3").string
     print(h3)
     value = li.select_one(".value").string
     print(value)
     print(h3,"=",value)