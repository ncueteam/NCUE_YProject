from umqtt.simple import MQTTClient as Client
import threading

class Unit:
    topic = "NCUEMQTT"
    port = 1883
    thread_list = []
    username = ""
    received_count = 0
    server = "test.mosquitto.org"
    client = Client(client_id=username, server=server)

    def on_connect(self, client, userdata, flags, rc) -> None:
        # print("Connected with result code "+str(rc))
        self.client.subscribe(self.topic)

    def on_message(self, userdata, msg):
        self.received_count += 1
        print(msg.topic + " " + str(msg.payload))

    def __init__(self, username: str):
        self.thread_list = []
        self.username = username
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.topic = self.topic
        self.client.port = self.port
        self.client.server = self.server
        self.client.ssl = False
        self.client.connect()

    def send_message(self) -> None:
        print('執行緒 ID:' + str(threading.get_ident()))
        self.client.publish(self.topic, "[" + self.username + "]\t" + input())
        # self.send_message()

    def run(self) -> None:
        self.thread_list.append(threading.Thread(target=self.send_message(), args=()))
        self.thread_list.append(threading.Thread(target=self.client.keepalive, args=()))
        for i in self.thread_list:
            i.start()

        for i in self.thread_list:
            i.join()


if __name__ == "__main__":
    runner = Unit(input("user name: "))
    runner.run()
