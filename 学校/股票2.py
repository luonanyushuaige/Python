import yfinance as yf
import matplotlib.pyplot as plt
# 获取茅台（600519.SS）的股票数据，日期范围从 2020-01-01 到 2021-01-01
stock_data = yf.download('600519.SS', start='2020-01-01', end='2021-01-01')

# 删除"Volume"和"Adj Close"列
stock_data_cleaned = stock_data.drop(columns=[ 'Volume'])

# 计算日收益率
stock_data_cleaned['Daily_Return'] = stock_data_cleaned['Close'].pct_change()

# 计算累计收益率
stock_data_cleaned['Cumulative_Return'] = (1 + stock_data_cleaned['Daily_Return']).cumprod()

# 绘制累计收益率
plt.figure(figsize=(10, 6))
plt.plot(stock_data_cleaned['Cumulative_Return'], label='Cumulative Return')
plt.title('Cumulative Return of Maotai Stock (2020)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Cumulative Return', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
