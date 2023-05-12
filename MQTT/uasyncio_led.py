import uasyncio as asyncio
import machine
import network

SSIDs = ["Yunitrish", "603"]
PWDs = ["0937565253", "0937565253"]


async def connect_net(ssid: list[str], password: list[str], num: int):
    try:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid[num], password[num])
        await asyncio.sleep_ms(2000)
        print("Connected to network:", wlan.ifconfig()[0])
    except KeyboardInterrupt:
        print("Connection interrupted by user.")
        await connect_net(ssid, password, num-1)
    except Exception as e:
        print("Error connecting to network:", e)
        await connect_net(ssid, password, num-1)


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
    await asyncio.create_task(blink(led_pin, 1500, -1))


def run():
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
