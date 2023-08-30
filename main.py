import uasyncio
from lib.file_set import FileSet
from lib.wifi.wifi_unit import WifiUnit
from lib.ble.ble_irq import BLE_IRQ

fileset = FileSet(folder='database', file_name='wifi.json')
# fileset.add("302", "0937565253")
# fileset.add("V2041", "123456789")

# wifi = WifiUnit(ssid="V2041", password="123456789")

BLE_IRQ(name='NCUE')

loop = uasyncio.get_event_loop()

