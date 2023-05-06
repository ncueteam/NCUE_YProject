import machine
import time
led = machine.Pin(2, machine.Pin.OUT)
led.value(1)
time.sleep(2)
led.value(0)