# GY_30光照强度传感器
import time
from machine import I2C, Pin

i2c = I2C(scl=Pin(15), sda=Pin(4), freq=10000)  # 软件I2C
addr_list = i2c.scan()
print('addr_list:', addr_list)
# result = bh1750fvi.sample(i2c) # in lux
# print(result)

# BH1750通电，进入等待测量状态
i2c.writeto(addr_list[0], b'\x01')

# 设置分辨率模式为连续 H分辨率模式
i2c.writeto(addr_list[0], b'\x10')

#VCC接3.3V
#GND接CND
#SCL接P15
#SDA接P4
#ADDR接P19

def GY_30_sensor():
    # 读取测量结果
    data = i2c.readfrom(35, 2)
    # 处理测量结果
    result = float(data[0] * 0xff + data[1]) / 1.2
    # 将测量结果返回
    return result


while True:
    print(GY_30_sensor())
    time.sleep_ms(2000)

