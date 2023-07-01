import uasyncio
from device.segment_7 import displayor

loop = uasyncio.get_event_loop()
loop.run_until_complete(displayor.main())
