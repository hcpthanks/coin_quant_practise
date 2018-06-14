"""
如何批量导入数据
"""

import pandas as pd  # 将panadas作为第三方库导入,我们一般将pandas 取一个别名叫pd
import os
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


file_list = []
for root, dirs, files in os.walk(r'C:\Users\han fengan\Desktop\coin_quant_class\data\class6'):
    # 当files不为空时
    if files:
        for f in files:
            if f.endswith('.csv'):
                file_list.append(f)
print(file_list)

# 遍历文件名,批量导入数据
all_data = pd.DataFrame()
for file in sorted(file_list):
    # print(file)
    #  导入数据
    df = pd.read_csv('C:\\Users\\han fengan\\Desktop\\coin_quant_class\\data\\class6\\BITFINEX\\EOSUSD\\' + file,
                     skiprows=1,
                     parse_dates=['candle_begin_time'])
    # 合并数据
all_data = all_data.append(df, ignore_index=True)


# 对数据进行排序
all_data.sort_values(by=['candle_begin_time'], inplace=True)
# print(all_data)

print(all_data.to_csv("all_data.csv", index=False))