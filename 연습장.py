import win32com.client
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

print(instStockChart.SetInputValue(0, "A003540"))  # 0: 종목코드
instStockChart.SetInputValue(1, ord('2')) # 1 : 기간으로 요청 , 2 : 개수로 요청
instStockChart.SetInputValue(4, 10) # 4: 요청개수
instStockChart.SetInputValue(5, 5) # 5: 종가에 해당하는 값
instStockChart.SetInputValue(6, ord('D')) #6 : 일단위
instStockChart.SetInputValue( 9, ord('1')) # 수정주가

instStockChart.BlockRequest() # 데이터 처리 요청
instStockChart.BlockRequest()

numData = instStockChart.GetHeaderValue(3)
for i in range(numData):
    print(instStockChart.GetDataValue(0, i))