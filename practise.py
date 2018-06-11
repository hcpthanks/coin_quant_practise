"""
pandas 常用方法
"""

import pandas as pd  # 将panadas作为第三方库导入,我们一般将pandas 取一个别名叫pd
import os
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行

# df = pd.read_csv(
#     #  改参数是数据在本地电脑的路径
#     filepath_or_buffer=r'C:\Users\han fengan\Desktop\coin_quant_class\data\class5\BITFINEX-1H-data-20180124.csv',
#     skiprows=1,
#     parse_dates=['candle_begin_time'],
#
# )


# df1 = df.iloc[0:10][['candle_begin_time', 'symbol', 'close', 'volume']]
# print(df1)
#
# df2 = df.iloc[5:20][['candle_begin_time', 'symbol', 'close', 'volume']]
# print(df2)
#
# df3 = (df1.append(df2, ignore_index=True))
# df3.drop_duplicates(
#     subset=['candle_begin_time', 'symbol'],
#     keep='first',
#     inplace=True
# )
#
# df3.reset_index(inplace=True)
#
# print(pd.DataFrame().empty)
#
# print(df.T)
#
# print(df['symbol'].str[:3])
#
# print(df['symbol'].str.replace('AID', 'AVT'))

# print(df.at[0, 'close'])
# print(df.at[5, 'low'])
# print(type(df.at[5,'low']))
#
# df['candle_begin_time'] = pd.to_datetime(df['candle_begin_time'])
# print(df.at[0, 'candle_begin_time'])
# print(type(df.at[0, 'candle_begin_time']))
# print(df['candle_begin_time'] + pd.Timedelta(hours=2))


# df['close_最近三天'] = df['close'].rolling(6).mean()
#
# df['close_至今均值'] = df['close'].expanding().max()
# df['close_最大值'] = df['close'].rolling(6).max()
#
#
# print(df[['close', 'close_最近三天', 'close_至今均值', 'close_最大值']])
# 批量读取文件名称
file_list= []
for files in os.walk(r'C:\Users\han fengan\Desktop\coin_quant_class\data'):
    # 当files不为空时
    if files:
        for f in files:
            if f.endswith('.csv'):
                file_list.append(f)



exit()







