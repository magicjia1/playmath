import datetime
import pytz
import pysolar.solar as solar


def calculate_solar_altitude(latitude, longitude, year, month, day, hour, minute, second):
    # 北京时区
    beijing_timezone = pytz.timezone('Asia/Shanghai')

    # 指定特定日期和时间（在北京时区）
    beijing_time = beijing_timezone.localize(datetime.datetime(year, month, day, hour, minute, second))

    # 计算太阳高度角
    altitude = solar.get_altitude(latitude, longitude, beijing_time)

    # 将太阳高度角转化为度数
    altitude_deg = round(altitude, 2)

    return altitude_deg


# 示例用法
latitude = 39.9  # 北纬39.9度
longitude = 116.4  # 东经116.4度
year = 2016
month = 3
day = 8
hour = 12
minute = 0
second = 0

altitude = calculate_solar_altitude(latitude, longitude, year, month, day, hour, minute, second)
print("北京时区（UTC+8）的太阳高度角（度）:", altitude)




def calculate_solar_azimuth(latitude, longitude, year, month, day, hour, minute, second):
    # 北京时区
    beijing_timezone = pytz.timezone('Asia/Shanghai')

    # 指定特定日期和时间（在北京时区）
    beijing_time = beijing_timezone.localize(datetime.datetime(year, month, day, hour, minute, second))

    # 计算太阳方位角
    azimuth = solar.get_azimuth(latitude, longitude, beijing_time)

    # 将太阳方位角转化为度数
    azimuth_deg = round(azimuth, 2)

    return azimuth_deg


# 示例用法
latitude = 39.9  # 北纬39.9度
longitude = 116.4  # 东经116.4度
year = 2023
month = 9
day = 8
hour = 12
minute = 0
second = 0

azimuth = calculate_solar_azimuth(latitude, longitude, year, month, day, hour, minute, second)
print("北京时区（UTC+8）的太阳方位角（度）:", azimuth)