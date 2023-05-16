import machine
import time
if __name__ == '__main__':
    led = machine.Pin(2, machine.Pin.OUT)
    led.value(1)
    time.sleep(2)
