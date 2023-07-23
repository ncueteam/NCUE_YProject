import uasyncio
from lib.device.segment_7 import displayor

from lib.file_set import FileSet
from lib.wifi.wifi_unit import WifiUnit
from lib.device.ir_rx.test import test

fileset = FileSet(folder='database', file_name='wifi.json')
fileset.add("302", "0937565253")
fileset.add("V2041", "123456789")

wifi = WifiUnit(ssid="c&k", password="0937565253")

# 紅外遙控測試
# test()

loop = uasyncio.get_event_loop()
loop.run_until_complete(displayor.main())
