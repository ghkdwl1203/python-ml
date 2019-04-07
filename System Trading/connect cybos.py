from pandas import DataFrame
import win32com.client
import win32com


instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
print(instCpStockCode.GetData(1, 240810))   # 첫번째 인자 값이 0이면 종목코드, 1이면 좀목명, 2면 Fullcode 리턴

print(instCpStockCode.GetCount()) # 상장종목수


stockNum = instCpStockCode.GetCount()

# 종목코드, 종목명 찾는 로직
for i in range(stockNum):
    if instCpStockCode.GetData(1, i) == '원익IPS':
        print(" 종목코드 : ",instCpStockCode.GetData(0,i))
        print(" 종목명 : ",instCpStockCode.GetData(1,i))
        print(i)
        temp = instCpStockCode.GetData(0,i)


# ###################################################################################################
# ### file Name: practice_1_2_2_01.py
# ###################################################################################################
from pandas import DataFrame
from subDS import subStockChart # 위에 작성한 subStockChart 불러오기

if __name__ == "__main__":
    ### 자료가져오기
    code =temp # 삼성전자 종목코드
    numHist =100 # 과거 100일치 데이터
    df=subStockChart(code, numHist)
    print(df)