from http import client
from re import T
import paho.mqtt.client as mqtt
import threading

class MQTTUnit:
    # 設定MQTT代理和主題
    topic = "NCUEMQTT"
    client = mqtt.Client()
    thread_list = []
    # 處理收到的訊息
    def on_message(self,client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
    def __init__(self):
        self.thread_list = []
        # 連接到MQTT代理並啟動訊息處理程序
        self.client.on_connect = self.client.subscribe(self.topic)
        self.client.on_message = self.on_message
        self.client.connect("test.mosquitto.org", 1883, 60)
    
    def sendMessage(self) -> None:
        print('執行緒 ID:' + str(threading.get_ident()))
        self.client.publish(self.topic, input())
        self.sendMessage()

    def run(self) -> None:
        self.thread_list.append(threading.Thread(target=self.sendMessage, args=()))
        self.thread_list.append(threading.Thread(target=self.client.loop_forever))
        for i in self.thread_list:    
            i.start()
 
        for i in self.thread_list:
            i.join()

if __name__ == "__main__":
    runner = MQTTUnit()
    runner.run()
