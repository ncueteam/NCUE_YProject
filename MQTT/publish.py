import paho.mqtt.client as mqtt

# 建立MQTT連線
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883)

# 發布訊息
client.publish("NCUEMQTT", "hello from Python")

# 關閉MQTT連線
client.disconnect()