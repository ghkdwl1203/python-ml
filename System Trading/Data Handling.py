import pandas_datareader.data as web


import datetime
import matplotlib.pyplot as plt

from pandas.tseries import converter

start = datetime.datetime(2010, 1, 1)

end = datetime.datetime(2016, 3, 19)


data = web.DataReader("AAPL", "yahoo", start, end)

converter.register()
plt.plot(data.index, data['Adj Close'])