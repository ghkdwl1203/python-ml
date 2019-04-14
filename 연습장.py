if __name__ == "__main__":
    ### 자료가져오기
    code =list # 삼성전자 종목코드
    numHist =1 # 과거 100일치 데이터
    df=subStockChart(code, numHist)
    print(df)