from machine import Pin, PWM
import time

ir_pin = Pin(14, Pin.IN)
pwm_pin = PWM(Pin(12))

pwm_pin.freq(40)

while ir_pin.value() == 0:
    pass

pwm_pin.duty(512)

while ir_pin.value() == 1:
    pass

pwm_pin.duty(0)