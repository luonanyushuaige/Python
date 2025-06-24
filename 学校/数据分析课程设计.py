import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 加载数据
data = pd.read_csv('house_data.csv')

# 选择关键特征和目标变量
features = [
    'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
    'waterfront', 'view', 'condition', 'grade', 'sqft_above',
    'sqft_basement', 'yr_built', 'yr_renovated', 'lat', 'long',
    'sqft_living15', 'sqft_lot15'
]
target = 'price'

# 修复：正确更新yr_renovated列
# 使用numpy的where函数替换yr_renovated为0的值
data['yr_renovated'] = np.where(data['yr_renovated'] > 0,
                                data['yr_renovated'],
                                data['yr_built'])

# 划分数据集
X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 特征标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 构建KNN模型（选择最佳k值）
best_k = 0
best_rmse = float('inf')

for k in range(3, 15):
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    if rmse < best_rmse:
        best_rmse = rmse
        best_k = k

# 使用最佳k值训练最终模型
final_model = KNeighborsRegressor(n_neighbors=best_k)
final_model.fit(X_train_scaled, y_train)

# 预测与评估
y_pred = final_model.predict(X_test_scaled)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# 输出结果
print(f"最佳K值: {best_k}")
print(f"测试集RMSE: {rmse:,.2f}")
print(f"测试集R²: {r2:.4f}")

# 随机抽取5个测试样本展示预测结果
sample_indices = np.random.choice(len(X_test), 5, replace=False)
sample_data = X_test.iloc[sample_indices].copy()
sample_data['实际房价'] = y_test.values[sample_indices]
sample_data['预测房价'] = y_pred[sample_indices]
sample_data['误差百分比'] = np.abs(
    (sample_data['预测房价'] - sample_data['实际房价']) / sample_data['实际房价'] * 100
).round(1)

print("\n随机测试样本预测结果:")
print(sample_data[['bedrooms', 'sqft_living', '实际房价', '预测房价', '误差百分比']])