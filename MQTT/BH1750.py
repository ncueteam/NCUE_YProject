from machine import Pin,I2C
import time

i2c = I2C(0,scl = Pin(15),sda = Pin(4),freq = 1_000_000)
scan = i2c.scan()
print(scan)
#print(hex(i2c.scan()[0]),hex(i2c.scan()[1]))  # 打印器件I2C地址
BH1750_I2C_ADD  = 0x23

#i2c.writeto(BH1750_I2C_ADD,chr(0x01)) # 通电运行
#i2c.writeto(BH1750_I2C_ADD,chr(0x07)) # 复位
#i2c.writeto(BH1750_I2C_ADD,chr(0x10)) # 横向分辨率连续读取 1 Lx 120ms

while True:
    gy = 0
    gy = i2c.readfrom(BH1750_I2C_ADD,2) #0-65535 1 8bit 2  int 16 char 8
    gy30 = float(gy[0] << 8 | gy[1])/1.2 #左移动，可以理解为乘法 gy[0]*0xff
    time.sleep_ms(2000)
    print("光照值 = %.2f Lx" %gy30)
