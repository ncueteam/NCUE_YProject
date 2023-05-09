import network

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    ssid = "Yunitrish"
    password = "0937565253"

    wlan.connect(ssid, password)
    print("Connected to network:", wlan.ifconfig()[0])
