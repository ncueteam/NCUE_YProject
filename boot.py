from lib.ota import ugit
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID', 'Password')

ugit.pull_all(isconnected=True)