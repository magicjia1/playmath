import datetime
import pytz
import pysolar.solar as solar
import math

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




def calculate_dni(latitude, altitude, solar_altitude):
    G0 = 1.366  # 太阳常数，kW/m^2

    a = 0.4237 - 0.00821 * (6 - altitude)**2
    b = 0.5055 + 0.00595 * (6.5 - altitude)**2
    c = 0.2711 + 0.01858 * (2.5 - altitude)**2

    dni = G0 * (a + b * math.exp(-c / math.sin(math.radians(solar_altitude))))

    return dni

# 示例用法
latitude = 39.9  # 北纬39.9度
altitude_km = 3.0  # 海拔高度，单位：km
solar_altitude_deg = 45.0  # 太阳高度角，单位：度

dni = calculate_dni(latitude, altitude_km, solar_altitude_deg)
print("法向直接辐射辐照度 DNI（kW/m2）:", dni)


def calculate_field_output_power(dni, mirror_areas, optical_efficiencies):
    N = len(mirror_areas)

    if N != len(optical_efficiencies):
        raise ValueError("镜面数量和光学效率数量必须相等")

    total_power = dni * sum(mirror_areas[i] * optical_efficiencies[i] for i in range(N))

    return total_power


# 示例用法
dni = 1000.0  # 法向直接辐射辐照度，单位：kW/m^2
mirror_areas = [10.0, 12.0, 15.0]  # 定日镜采光面积列表，单位：m^2
optical_efficiencies = [0.85, 0.9, 0.88]  # 定日镜光学效率列表

output_power = calculate_field_output_power(dni, mirror_areas, optical_efficiencies)
print("定日镜场的输出热功率 Efield（kW）:", output_power)


def calculate_optical_efficiency(distance_to_receiver):
    # 阴影遮挡效率，这里假设阴影遮挡损失为0
    eta_sb = 1.0

    # 余弦效率，这里假设余弦损失为0
    eta_cos = 1.0

    # 计算大气透射率
    if distance_to_receiver <= 1000:
        eta_at = 0.99321 - 0.0001176 * distance_to_receiver + 1.97e-8 * distance_to_receiver ** 2
    else:
        eta_at = 0.99321  # 大气透射率的默认值

    # 集热器截断效率，这里假设截断效率为1
    eta_trunc = 1.0

    # 镜面反射率
    eta_ref = 0.92

    # 计算光学效率
    eta = eta_sb * eta_cos * eta_at * eta_trunc * eta_ref

    return eta


# 示例用法
distance_to_receiver = 5.0  # 镜面中心到集热器中心的距离，单位：m

optical_efficiency = calculate_optical_efficiency(distance_to_receiver)
print("定日镜的光学效率 𝜂:", optical_efficiency)
