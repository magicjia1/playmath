import math

# 太阳高度角（Solar Elevation Angle），以度为单位
solar_elevation_angle = 90  # 例如，假设太阳高度角为30度

# 计算余弦损失
cosine_loss = math.cos(math.radians(solar_elevation_angle))

# 打印结果
print(f"太阳高度角（Solar Elevation Angle）: {solar_elevation_angle} 度")
print(f"余弦损失（Cosine Loss）: {cosine_loss:.4f}")
