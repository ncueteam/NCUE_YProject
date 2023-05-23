# GY_30光照强度传感器
import time
from machine import I2C, Pin
import network
from umqtt.simple import MQTTClient


#VCC接3.3V
#GND接CND
#SCL接P15
#SDA接P4
#ADDR接P19

def main():
    i2c = I2C(scl=Pin(15), sda=Pin(4), freq=10000)  # 软件I2C
    addr_list = i2c.scan()
    print('addr_list:', addr_list)

    i2c.writeto(addr_list[0], b'\x01')# BH1750通电，进入等待测量状态
    i2c.writeto(addr_list[0], b'\x10')# 设置分辨率模式为连续 H分辨率模式

    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('V2041', '123456789')

    while not sta_if.isconnected():
        pass
    print("connected")

    client = MQTTClient(
        client_id="client",
        keepalive=5,
        server="test.mosquitto.org",
        ssl=False)

    client.connect()

    def get_msg(topic, msg):
        print(msg)

    client.set_callback(get_msg)
    client.subscribe("MQTT")


    def GY_30_sensor():
        # 读取测量结果
        data = i2c.readfrom(35, 2)
        # 处理测量结果
        result = float(data[0] * 0xff + data[1]) / 1.2
        # 将测量结果返回
        return result

    counter = 0
    while True:
        string ="光照值 = " + GY_30_sensor()
        print(string)
        client.publish("MQTT", string)
        time.sleep_ms(2000)

