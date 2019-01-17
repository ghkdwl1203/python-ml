import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

urllib.request.urlretrieve(url,savename)
print ("저장되었습니다.")

'$ python3 download-png1.py 명령줄?'

mem = urllib.request.urlopen(url).read()

with open(savename,mode="WB") as f:  ' WITH 자동으로 열고닫기처리'
    f.write(mem)
    print("저장되었습니다.")