import network
from lib.file_set import FileSet


class WifiUnit:
    wifiDataBase = FileSet(folder='database', file_name='wifi.json')
    connected = False

    def __init__(self, ssid: str, password: str):
        self.netWork = network.WLAN(network.STA_IF)
        self.netWork.active()
        for ssid, password in self.wifiDataBase.data.items():
            self.connected = self.connect(ssid, password)
            if self.connected:
                print("Connected!")
                self.printStatus()
                self.wifiDataBase.add(key=ssid, value=password)
                break
        while True:
            self.connected = self.connect(ssid, password)
            if self.connected:
                print("Connected!")
                self.printStatus()
                self.wifiDataBase.add(key=ssid, value=password)
                break

    def connect(self, ssid: str, password: str) -> bool:
        try:
            self.netWork.connect(ssid, password)
            return True
        except KeyboardInterrupt:
            return False
        except Exception:
            return False

    def printStatus(self):
        if self.netWork.active() and self.netWork.isconnected():
            config = self.netWork.ifconfig()
            print("IP Address:", config[0])
            print("Subnet Mask:", config[1])
            print("Gateway:", config[2])
            print("DNS Server:", config[3])
        else:
            print("wifi not connected")
