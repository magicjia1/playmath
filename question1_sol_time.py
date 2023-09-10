from utils.solarCalculations import *
from datetime import datetime, timedelta
import pandas as pd
# 设置起始日期和结束日期
start_date = datetime(2023, 1, 21)  # 起始日期为2023年1月21日
end_date = datetime(2023, 12, 21)  # 结束日期为2023年12月21日

# 设置时间列表，您可以根据需要修改
# 定义时间点
times = ['9:00', '10:30', '12:00', '13:30', '15:00']

# 初始化日期时间列表
date_times_list = []

# 生成日期时间列表
current_date = start_date
while current_date <= end_date:
    for time in times:
        date_time_str = f"{current_date.strftime('%Y-%m-%d')} {time}"
        date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')

        # 分解日期时间为 [年，月，日，小时，分钟，秒]
        date_time_list = [date_time.year, date_time.month, date_time.day, date_time.hour, date_time.minute,
                          date_time.second]

        date_times_list.append(date_time_list)
    # 增加一个月，以便生成下一个月的日期
    if current_date.month == 12:
        current_date = current_date.replace(year=current_date.year + 1, month=1)
    else:
        current_date = current_date.replace(month=current_date.month + 1)

# 打印结果列表
for date_time in date_times_list:
    # print(date_time)

    year, month, day, hour, minute, second = date_time
    # print(f"Year: {year}, Month: {month}, Day: {day}, Hour: {hour}, Minute: {minute}, Second: {second}")
    altitude = calculate_solar_altitude(39.6, 98.5, year, month, day, hour, minute, second)
    dni = calculate_dni(3.0,altitude)
    date_time.append(altitude)
    date_time.append(dni)
    print(
            f"Year: {year}, Month: {month}, Day: {day}, Hour: {hour}, Minute: {minute}, Second: {second}, "
            f"solar_altitude: {altitude}, dni: {dni}, ")


for date_time in date_times_list:
    year, month, day, hour, minute, second,altitude,dni = date_time
    efflist = []
    eta_trunclist = []
    eta_sb=[]
    # 指定Excel文件路径
    excel_file_path = 'ms/附件.xlsx'  # 替换成你的Excel文件路径

    # 使用pandas读取Excel文件
    df = pd.read_excel(excel_file_path)
    data_points = []
    sumdata=0
    # 使用iterrows()逐行迭代
    for index, row in df.iterrows():
        efficiency = calculate_optical_efficiency(df.at[index, 'distance'],altitude)
        df.at[index, 'efficiency'] = efficiency
        data_points.append([row[0], row[1],df.at[index, 'efficiency']])
        efflist.append(efficiency)
        area = 6*6
        sumdata += area *efficiency

    efficiency_values = []
    average = 0
    efficiency_values = [element[2] for element in data_points]
    # 使用内置函数sum()计算总和
    total = sum(efficiency_values)

    # 使用len()函数计算数字的数量
    count = len(efficiency_values)

    # 计算平均数
    average = total / count
    efficiency_values = []
    average = 0


    import matplotlib.pyplot as plt



    x_values = [point[0] for point in data_points]
    y_values = [point[1] for point in data_points]
    z_values = [point[2] for point in data_points]

    plt.scatter(x_values, y_values, c=z_values, cmap='viridis')
    color_bar = plt.colorbar()
    color_bar.set_label('Z Values')
    # 创建日期时间对象
    str_date_time = datetime(year, month, day, hour, minute, second)

    # 使用strftime将每个组件转换为字符串并拼接
    date_time_str = str_date_time.strftime("%Y-%m-%d %H:%M:%S")

    plt.title('Heatmap of Z Values: '+date_time_str)
    plt.xlabel('X')
    plt.ylabel('Y')
    # 显示热力图
    plt.show()

    field_output_power = dni * sumdata
    date_time.append(field_output_power)
    print(
        f"Year: {year}, Month: {month}, Day: {day}, Hour: {hour}, Minute: {minute}, Second: {second}, "
        f"solar_altitude: {altitude}, dni: {dni}, field_output_power: {field_output_power},average:  {average}")



# 创建DataFrame
df = pd.DataFrame(date_times_list, columns=['Year', 'Month', 'Day', 'Hour', 'Minute', 'Second','altitude','dni','field_output_power'])

# 保存DataFrame到Excel文件
excel_file = 'ms/date_times.xlsx'
df.to_excel(excel_file, index=False, engine='openpyxl')

print(f'Data saved to {excel_file}')