import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

urllib.request.urlretrieve(url,savename)
print ("저장되었습니다.")

$ python3 download-png1.py