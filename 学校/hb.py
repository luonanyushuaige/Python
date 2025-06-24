import pandas as pd

import numpy as np
import array

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

# first: 寻找与A最相似的其它用户  ； second: 预测A对未接触的物品（即原来评分为NaN的物品，如two）的评分，从而做出是否推荐的判断


# ！！！对缺失值的处理要适当（想象一下，如果直接将缺失值填充为0，则会引入负面评价，因为此时0并不是一个中性值，甚至可以说是一个最小的值，直接拉低了评分），所以我们要先对这个矩阵进行去中心化，再将缺失值填充为0

# 去中心化（每一个用户的每一个项目的评分减去均值） ， 这样每一个用户的项目的均值就为0了，那么0就是一个中性值，不会引入负面评价

new_data = data.apply(lambda x: x - x.mean(), axis=1)

print(new_data)

# 计算余弦相似度
"""

from sklearn.metrics.pairwise import cosine_similarity

sim_AB = cosine_similarity(new_data.loc["A", :].fillna(0).values.reshape(1, -1), new_data.loc["B",].fillna(0).values.reshape(1, -1))  

print(sim_AB)
sim_AC = cosine_similarity(new_data.loc["A", :].fillna(0).values.reshape(1, -1), new_data.loc["C",].fillna(0).values.reshape(1, -1))

print(sim_AC)

sim_AD = cosine_similarity(new_data.loc["A", :].fillna(0).values.reshape(1, -1), new_data.loc["D",].fillna(0).values.reshape(1, -1))

print(sim_AD)

"""

# 这样一个一个计算太麻烦了，可定义一个函数来循环遍历

Result = {}


def yonhu_similar(mubiao, data):
    for i in range(data.shape[0]):
        bijiao = data.index[i]

        sim = cosine_similarity(new_data.loc[mubiao, :].fillna(0).values.reshape(1, -1),
                                new_data.loc[bijiao,].fillna(0).values.reshape(1, -1))

        result = f"sim_{mubiao}{bijiao}"

        Result[result] = sim


yonhu_similar("A", data=data)

# print(Result)


# 根据相似度大小排序（降序排）

sorted_Result = sorted(Result.items(), key=lambda x: x[1], reverse=True)

yonhu_sorted_Result = [i[0] for i in sorted_Result]

print(sorted_Result)



# 同理这里也可以写一个循环来遍历，然后将结果存于一个列表中
