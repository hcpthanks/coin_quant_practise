import pandas as pd
import os

#
# # ==== 将数据存入hdf文件
# # 批量读取文件名称
#
# file_list = []
# for root, dirs, files, in os.walk(r'C:\Users\han fengan\Desktop\coin_quant_class\data\class6'):
#     if files:
#         for f in files:
#             if f.endswith('.csv'):
#                 file_list.append(f)
#
# h5_store = pd.HDFStore('eos_data.h5', mode='w')
#
# # 批量导入并且存储数据
#
# for file in sorted(file_list):
#     date = file.split('_')[2]
#     print(date)
#
#
#     # 导入数据
#     df = pd.read_csv('C:\\Users\\han fengan\\Desktop\\coin_quant_class\\data\\class6\\BITFINEX\\EOSUSD\\' + file,
#                      skiprows=1,
#                      parse_dates=['candle_begin_time']
#                      )
#
#
#    #创建、存储数据到hdf
#     h5_store['eos_'+date] = df
#
# h5_store.close()

# 读取hdf数据
# 创建hdf文件
h5_store = pd.HDFStore('eos_data.h5', mode='r')

#  h5_store中的key
print(h5_store.keys())


# 读取某个key指向的数据
print(h5_store.get('eos_20170803'))
print(h5_store['eos_20180308'])

# 关闭hdf文件
h5_store.close()
