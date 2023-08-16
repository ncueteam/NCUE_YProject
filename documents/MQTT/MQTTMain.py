import network
import machine
import time

def main():
    print("Launching esp32...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    led = machine.Pin(2, machine.Pin.OUT)
    count = 0

    SSIDs = ["Yunitrish", "603"]
    PWDs = ["0937565253", "0937565253"]

    def flashor(timor):
        led.value(1)
        time.sleep(2)
        led.value(0)
        timor -= 1
        if timor > 0:
            flashor(timor)

    flashor(1)

    def mn(n):
        try:
            ssid = input("[" + str(n) + "]Enter Wi-Fi SSID: ")
            password = input("[" + str(n) + "]Enter Wi-Fi password: ")
            wlan.connect(ssid, password)
            print("Connected to network:", wlan.ifconfig()[0])
        except KeyboardInterrupt:
            print("Connection interrupted by user.")
        except Exception as e:
            print("Error connecting to network:", e)

        if not wlan.isconnected() & n < 3:
            n += 1
            mn(n)

    mn(count)

    print("WLAN connected")

    flashor(3)