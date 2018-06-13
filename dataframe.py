import pandas as pd
import numpy as np


#  创建DataFrame对象
df = pd.DataFrame([1, 2, 3, 4, 5], columns=['cols'], index=['a', 'b', 'c', 'd', 'e'])
# print(df)

df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['col1', 'col2', 'col3'], index=['a', 'b'])
# print(df2)

df3 = pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['col1', 'col2'], index=['a', 'b'])
# print(df3)

df4 = pd.DataFrame({'col1': [1, 3], 'col2': [2, 4]}, index=['a', 'b'])
# print(df4)

#  基本操作

#  DataFrame对象的基本操作

# print(df2.index)
#
# print(df2.columns)

#  根据索引查看数据
# print(df2.loc['a'])
# print(df2.iloc[1])

# 访问多行数据， 索引参数为一个列表对象
# print(df2.loc[['a', 'b']])
# print(df.loc[df.index[1:3]])

# 访问列数据
# print(df2[['col1', 'col3']])

# 计算
# DataFrame元素求和
# 默认是对每列元素求和
# print(df2.sum())
# print(df2.sum(1))

# 对每个元素乘以2
# print(df2.apply(lambda x: x * 2))
# print(df2 * 2)

# 对每个元素求平方（支持ndarray一样的向量化操作)
# print(df2 ** 2)


# 列扩充
# 对DataFrame对象进行列扩充
# df2['col4'] = ['cnn', 'rnn']
# print(df2)

#也可以通过一个新的DataFrame对象来定义一个新列，索引自动对应
# df2['col5'] = pd.DataFrame(['machinelearning', 'deeplearning'], index=['a', 'b'])
# print(df2)

# 行扩充
# 行进行扩充
# df2 = df2.append(pd.DataFrame({'col1': 7, 'col2': 8, 'col3': 9, 'col4': 'rcnn',
#                          'col5': 'reinforcementlearning'}, index=['c']))
# print(df2)
#
# print(df2.append(pd.DataFrame({'col1': 7, 'col2': 8, 'col3': 9, 'col4': 'rcnn','col5': 'reinforcementlearning'}, index=['c'])))
#

# 注意！
# 如果在进行 行扩充时候没有指定index的参数， 索引会被数字取代
# print(df2.append({'col1': 10, 'col2': 11, 'col3': 12, 'col4': 'frnn','col5': 'DRL'}, ignore_index=True))

#print(df2.loc['c'])

# DataFrame对象的合并
#DataFrame 对象的合并

df_a = pd.DataFrame(['wang', 'jing', 'hui', 'is', 'a', 'master'], columns=['col6'], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(df_a)

# 默认合并， 只保留dfd中的全部索引
dfb = pd.DataFrame([1, 2, 3, 4, 5, 6, 7], columns=['col1'], index=['a', 'b', 'c', 'd', 'e', 'f','g'])
print(dfb.join(df_a))

# 默认合并之接受索引已经存在的值
# 通过指定参数 how, 指定合并的方式

print(dfb.join(df_a, how='inner')) # 合并两个Dataframe的交集

# 合并两个dataframe对象的并集

print(dfb.join(df_a, how='outer'))