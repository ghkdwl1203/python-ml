from pandas import DataFrame
import win32com.client
import win32com
from subDS import subStockChart # 위에 작성한 subStockChart 불러오기

instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
print(instCpStockCode.GetData(1, 240810))   # 첫번째 인자 값이 0이면 종목코드, 1이면 좀목명, 2면 Fullcode 리턴

print(instCpStockCode.GetCount()) # 상장종목수


stockNum = instCpStockCode.GetCount()
list = ['원익IPS','비에이치','하이비전시스템','현대제철','SK네트웍스','포스코케미칼','한화케미칼','SK텔레콤','제이콘텐트리',
        '한온시스템','팬오션','삼성증권']
code = []
name =[]
price=[]

# 종목코드, 종목명 찾는 로직
for j in  range(len(list)):
    for i in range(stockNum):
        if instCpStockCode.GetData(1, i) == list[j]:
            temp = instCpStockCode.GetData(0,i)

    code.append(temp)
print(list)
print(code)


if __name__ == "__main__":
    ### 자료가져오기
    # 삼성전자 종목코드
    numHist = 100 # 과거 100일치 데이터
    df=subStockChart(code[1], numHist)
    print(df)