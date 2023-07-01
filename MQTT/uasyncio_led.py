import uasyncio as asyncio
import machine
import network
from umqtt.simple import MQTTClient as Client
SSIDs = ["c&k", "603", "Yunitrish", 'V2041']
PWDs = ["0423151980", "0937565253", "0937565253", '123456789']
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
        self.client.publish(self.topic, "[" + self.username + "]\t" + input())
        # self.send_message()
async def connect_net(ssid: list[str], password: list[str], num: int):
    if num >= len(ssid):
        ssid.append(input("SSID: "))
        password.append(input("PassWord: "))
    try:
        wlan = network.WLAN(network.STA_IF)
        if num == 0:
            wlan.active(True)
        wlan.connect(ssid[num], password[num])
        await asyncio.sleep_ms(1000)
        print("Connected to network:", wlan.ifconfig()[0])
    except KeyboardInterrupt:
        print("[" + str(num) + "]Connection interrupted by user.")
        num += 1
        await connect_net(ssid, password, num)
    except Exception as e:
        num += 1
        print("[" + str(num) + "]Error connecting to network:", e)
        await connect_net(ssid, password, num)
async def blink(led_pin, gap: int, time: int):
    if time == -1:
        while True:
            led_pin.on()
            await asyncio.sleep_ms(gap)
            led_pin.off()
            await asyncio.sleep_ms(gap)
    elif time == 0:
        led_pin.off()
        await asyncio.sleep_ms(gap)
    else:
        led_pin.on()
        await asyncio.sleep_ms(gap)
        led_pin.off()
        await asyncio.sleep_ms(gap)
        await blink(led_pin, gap, time - 1)
async def main():
    led_pin = machine.Pin(2, machine.Pin.OUT)
    await asyncio.create_task(blink(led_pin, 100, 10))
    await connect_net(SSIDs, PWDs, 0)
    runner = Unit(input("username: "))

    async def loopor():
        runner.send_message()
        await asyncio.create_task(blink(led_pin, 100, 1))
        await loopor()
    await loopor()

def run():
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
