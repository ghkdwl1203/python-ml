import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

urllib.request.urlretrieve(url,savename)  '
print ("저장되었습니다.")

mem = urllib.request.urlopen(url).read()  # request  : 곧바로 저장 ㄴㄴ 파이썬 메모리 위에 올림'

with open(savename,mode="WB") as f:  # WITH 자동으로 열고닫기처리'
    f.write(mem)
    print("저장되었습니다.")