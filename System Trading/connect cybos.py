import win32com.client
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
print(instCpStockCode.GetData(1, 111))   # 첫번째 인자 값이 0이면 종목코드, 1이면 좀목명, 2면 Fullcode 리턴

for i in range(0,10):
    print(instCpStockCode.getdata(1,i))