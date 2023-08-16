import network
from lib.file_set import FileSet
import utime


class WifiUnit:
    wifiDataBase = FileSet(folder='database', file_name='wifi.json')

    def __init__(self, ssid: str, password: str):
        for ssid, password in self.wifiDataBase.data.items():
            self.connect_wifi(ssid, password)
            if self.sta.isconnected():
                self.wifiDataBase.add(ssid, password)
                return
            else:
                self.wifiDataBase.delete(ssid)
        if ssid and password:
            self.connect_wifi(ssid, password)
            if self.sta.isconnected():
                self.wifiDataBase.add(ssid, password)
                return
        self.printStatus()

    def connect_wifi(self, ssid: str, password: str):
        utime.sleep(3)
        self.sta = network.WLAN(network.STA_IF)
        if self.sta.isconnected():
            self.sta.disconnect()
            self.sta.active(False)
            utime.sleep(1)
        self.sta.active(True)
        utime.sleep(1)
        self.sta.connect(ssid, password)
        utime.sleep(1)

    def printStatus(self):
        if self.sta.active() and self.sta.isconnected():
            config = self.sta.ifconfig()
            print("IP Address:", config[0])
            print("Subnet Mask:", config[1])
            print("Gateway:", config[2])
            print("DNS Server:", config[3])
        else:
            print("wifi not connected")


