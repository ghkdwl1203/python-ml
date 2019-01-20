import urllib.request

url="http://api.aoikujira.com/ip/ini"
#url2="ftp://api.aoikujira.com/ip/ini"  #ftp가 뭐
res = urllib.request.urlopen(url)

data=res.read()


text = data.decode("utf-8") #utf-8?
text2= data #decode 메서드를 이용하여 바이너리를 문자열로 변환
print(text)
print(text2)
