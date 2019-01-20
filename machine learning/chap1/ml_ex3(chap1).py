import urllib.request
import urllib.parse

import sys
import urllib.request as req
import urllib.parse as parse

if len(sys.argv) <= 1:
    print("USAGE: download-forecast-argv<Region Number>")
    sys.exit()

regionNumber = sys.argv[1]

print(regionNumber)
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnId':regionNumber
}

params = urllib.parse.urlencode(values) #url의 구조, get,post방식, 페이지호출,
url = API +"?" + params # ?  url에서 get방식 문법

data=urllib.request.urlopen(url).read()
data2= req.urlopen(url).read()

text=data.decode("utf-8")
text2=data2.decode("utf-8")

print(text2)