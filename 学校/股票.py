import yfinance as yf
import matplotlib.pyplot as plt
# 获取茅台（600519.SS）的股票数据，日期范围从 2020-01-01 到 2021-01-01
stock_data = yf.download('600519.SS', start='2020-01-01', end='2021-01-01')

# 查看数据的前几行
print(stock_data.head())
# 删除"Volume"和"Adj Close"列
stock_data_cleaned = stock_data.drop(columns=[ 'Volume'])

# 绘制茅台收盘价曲线
plt.figure(figsize=(10, 6))
plt.plot(stock_data_cleaned['Close'], label='Close Price')
plt.title('Maotai Stock Price (2020)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Close Price (CNY)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()