import pandas as pd

df = pd.read_hdf('C:\\Users\\han fengan\\Desktop\\coin_quant_class\\data\\class6\\eos_1min_data.h5',
                 key='all_data')                                  # 从hdf中读取1分钟数据

# df = df[df['candle_begin_time'] >= pd.to_datetime('2017-07-01 17:20:00')]  # 选取某一时间段
# df.set_index('candle_begin_time', inplace=True)                   # 将candle_begin_time设定为index
print(df.head(10))

# 周期转换方法
# rule_type = '5T'    # rule = '5T', 意思是转变为5分钟数据
# period_df = df['close'].resample(rule=rule_type).last()     # 一个[]中括号得到series
# period_df = df[['close']].resample(rule=rule_type).last()  # 两个[[]] 得到的是dataframe， last:取这5分钟最后一行数据
# print(period_df)
# print(period_df1)


# 开  高  低的价格, 成交量

# period_df['open'] = df['open'].resample(rule=rule_type).first()
# period_df['high'] = df['high'].resample(rule=rule_type).max()
# period_df['low'] = df['low'].resample(rule=rule_type).min()
# period_df['volume'] = df['volume'].resample(rule=rule_type).sum()
#
# period_df = period_df[['open', 'high', 'low', 'close', 'volume']]
# print(period_df)

#  第二种方法： 将1分钟数据转化为5分钟
rule_type = '2T'
period_df = df.resample(rule=rule_type, on='candle_begin_time', base=0, label='left', closed='left').agg(
    {'open': 'first',
     'high': 'max',
     'low': 'min',
     'close': 'last',
     'volume': 'sum',
    })

# period_df = period_df[['open', 'high', 'low', 'close', 'volume']]
# print(period_df)

# 去除不必要的数据
# 去除一天都没有交易的周期
period_df.dropna(subset=['open'], inplace=True)
# 去除成交量为0的周期
period_df = period_df[period_df['volume'] >0]
print(period_df)