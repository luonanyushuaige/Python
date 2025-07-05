import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.metrics import mean_squared_error, r2_score

# 设置中文显示
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# 构建数据
data = {
    'Y': [20.10, 22.30, 30.50, 28.20, 32.00, 40.10, 42.10, 48.80, 50.50, 60.10, 70.00, 75.00],
    'X1': [30.00, 35.00, 41.20, 51.30, 55.20, 61.40, 65.20, 70.00, 80.00, 92.10, 102.00, 120.30],
    'X2': [1.00, 1.02, 1.20, 1.20, 1.50, 1.05, 0.90, 0.95, 1.10, 0.95, 1.02, 1.05]
}
df = pd.DataFrame(data)

# 数据探索
print("数据基本统计描述：")
print(df.describe())

# 可视化探索
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].scatter(df['X1'], df['Y'])
axes[0].set_title('平均收入与平均消费水平关系')
axes[0].set_xlabel('平均收入 X1')
axes[0].set_ylabel('平均消费水平 Y')

axes[1].scatter(df['X2'], df['Y'])
axes[1].set_title('价格指数与平均消费水平关系')
axes[1].set_xlabel('价格指数 X2')
axes[1].set_ylabel('平均消费水平 Y')

plt.tight_layout()
plt.savefig('变量关系散点图.png')
plt.close()

# 构建多元线性回归模型
X = df[['X1', 'X2']]
X = sm.add_constant(X)  # 添加截距项
y = df['Y']

model = sm.OLS(y, X)
results = model.fit()

# 输出回归结果
print("\n回归分析结果摘要：")
print(results.summary())

# 提取系数
coefficients = results.params
print("\n回归方程:")
print(f"Y = {coefficients['const']:.4f} + {coefficients['X1']:.4f}*X1 + {coefficients['X2']:.4f}*X2")

# 计算VIF检验多重共线性
vif = pd.DataFrame()
vif["变量"] = X.columns
vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print("\n多重共线性检验(VIF):")
print(vif)

# 预测与模型评估
y_pred = results.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"\n均方误差(MSE): {mse:.4f}")
print(f"决定系数(R²): {r2:.4f}")

# 残差分析
residuals = y - y_pred

# 残差与预测值散点图
plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.title('残差与预测值散点图')
plt.xlabel('预测值')
plt.ylabel('残差')
plt.savefig('残差分析图.png')
plt.close()

# 保存结果到CSV
results_df = pd.DataFrame({
    '实际值': y,
    '预测值': y_pred,
    '残差': residuals
})
results_df.to_csv('回归预测结果.csv', index=False)

print("\n分析完成，结果已保存到文件。")