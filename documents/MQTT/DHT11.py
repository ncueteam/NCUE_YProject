import time
import network
from lib.umqtt.simple import MQTTClient
from machine import Pin
from documents import dht


def main():
    dht11 = dht.DHT11(Pin(14))

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

    counter = 0
    while True:
        client.check_msg()
        dht11.measure()
        string = "T:" + str(dht11.temperature()) + " H:" + str(dht11.humidity())
        print(string)
        client.publish("MQTT", string)
        counter = counter + 1
        time.sleep(1)