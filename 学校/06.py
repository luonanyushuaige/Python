import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {'Scores': [55, 70, 85, 90, 60, 75, 80, 95, 100, 65]}
df = pd.DataFrame(data)

# 绘制箱线图
df.plot(kind='box', title='Scores Boxplot', ylabel='Scores', figsize=(8, 5))
plt.show()