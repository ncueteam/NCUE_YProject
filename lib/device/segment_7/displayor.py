import uasyncio
import machine


async def flash(led_pin, gap: int):
    led_pin.on()
    await uasyncio.sleep_ms(gap)
    led_pin.off()
    await uasyncio.sleep_ms(gap)
    await uasyncio.create_task(flash(led_pin, gap))


async def show(pin, num):
    count = 0
    for i in num:
        if i == 0:
            pin[count].on()
        elif i == 1:
            pin[count].off()
        count += 1


async def cycle(sleep, to_display):
    for num in to_display:
        await uasyncio.create_task(show(default_register, patterns[num]))
        await uasyncio.sleep_ms(sleep)
    await uasyncio.create_task(cycle(sleep, to_display))


async def main(pattern=None, sleep=400, register=None):
    global default_register
    if register is not None:
        default_register = [machine.Pin(it, machine.Pin.OUT) for it in register]
    else:
        default_register = [machine.Pin(it, machine.Pin.OUT) for it in [15, 16, 17, 18, 19, 21, 22, 23]]
    if pattern is None:
        pattern = ['0', '.', '1', '.', '2', '.', '3', '.', '4', '.', '5', '.', '6', '.', '7', '.', '8', '.', '9', '.']
    sleep = sleep
    await uasyncio.create_task(cycle(sleep, pattern))

default_register = []
patterns = {
    '.': [0, 0, 0, 0, 0, 0, 0, 1],
    '0': [1, 1, 1, 1, 1, 1, 0, 0],
    '1': [0, 1, 1, 0, 0, 0, 0, 0],
    '2': [1, 1, 0, 1, 1, 0, 1, 0],
    '3': [1, 1, 1, 1, 0, 0, 1, 0],
    '4': [0, 1, 1, 0, 0, 1, 1, 0],
    '5': [1, 0, 1, 1, 0, 1, 1, 0],
    '6': [1, 0, 1, 1, 1, 1, 1, 0],
    '7': [1, 1, 1, 0, 0, 1, 0, 0],
    '8': [1, 1, 1, 1, 1, 1, 1, 0],
    '9': [1, 1, 1, 1, 0, 1, 1, 0]
}
