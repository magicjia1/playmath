import pandas as pd
from utils import *
from utils.solarCalculations import *



# 指定Excel文件路径
excel_file_path = './ms/附件.xlsx'  # 替换成你的Excel文件路径

# 使用pandas读取Excel文件
df = pd.read_excel(excel_file_path)

# 使用iterrows()逐行迭代
for index, row in df.iterrows():
    # 访问每一行的数据

    dis =  set_distance(row[0], row[1],4)
    df.at[index, 'distance'] = dis



    print(row[0],row[1] , row[2],)  # 替换成你的列名

# 保存DataFrame到Excel文件
df.to_excel(excel_file_path, index=False)




