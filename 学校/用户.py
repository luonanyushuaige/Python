import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 假设得到了一个有缺失值的用户-物品评分矩阵（评分越高，表示此用户对该物品的喜好程度越高）
data = pd.DataFrame({
    "one": [4, np.nan, 2, np.nan],
    "two": [np.nan, 4, np.nan, 5],
    "three": [5, np.nan, 2, np.nan],
    "four": [3, 4, np.nan, 3],
    "five": [5, np.nan, 1, np.nan],
    "six": [np.nan, 5, np.nan, 5],
    "seven": [np.nan, np.nan, np.nan, 4]
}, index=list('ABCD'))

print(data)

# 去中心化（每一个用户的每一个项目的评分减去均值），这样每一个用户的项目的均值就为0了，那么0就是一个中性值，不会引入负面评价
new_data = data.apply(lambda x: x - x.mean(), axis=1)
print(new_data)

# 计算余弦相似度
Result = {}

def yonhu_similar(mubiao, data):
    for i in range(data.shape[0]):
        bijiao = data.index[i]
        if mubiao != bijiao:  # 排除用户自身
            sim = cosine_similarity(new_data.loc[mubiao, :].fillna(0).values.reshape(1, -1),
                                    new_data.loc[bijiao,].fillna(0).values.reshape(1, -1))
            result = f"sim_{mubiao}{bijiao}"
            Result[result] = sim

yonhu_similar("A", data=data)

# 根据相似度大小排序（降序排）
sorted_Result = sorted(Result.items(), key=lambda x: x[1], reverse=True)
yonhu_sorted_Result = [i[0] for i in sorted_Result]
print(sorted_Result)
print(yonhu_sorted_Result)

# 预测A对two商品的评分，从而做出是否推荐的判断
sim_AD = Result['sim_AD'] if 'sim_AD' in Result else 0
sim_AB = Result['sim_AB'] if 'sim_AB' in Result else 0

A_two = (sim_AD * data.loc["D", "two"] + sim_AB * data.loc["B", 'two']) / (sim_AD + sim_AB) if (sim_AD + sim_AB) != 0 else np.nan
print(A_two)

# 预测A对six商品的评分，从而做出是否推荐的判断
A_six = (sim_AD * data.loc["D", "six"] + sim_AB * data.loc["B", 'six']) / (sim_AD + sim_AB) if (sim_AD + sim_AB) != 0 else np.nan
print(A_six)