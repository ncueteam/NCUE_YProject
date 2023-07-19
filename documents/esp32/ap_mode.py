import machine
import time
led = machine.Pin(2, machine.Pin.OUT)
led.value(1)
time.sleep(2)
led.value(0)
try:
  import usocket as socket
except:
  import socket

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'MicroPython-AP'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, authmode=network.AUTH_WPA_WPA2_PSK, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

def web_page():
  html = """
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                text-align:center
            }
            before::body {
            
            }
        </style>
    </head>
    <body>
        <h1>Test Device</h1>
        <h2>UUID: befegk_usdelk_2j9s0b_12k02</h2>
        <h2>type: light_switch</h2>
        <h2>status: off</h2>
        <button type="button">save</button>
    </body>
</html>
"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  response = web_page()
  conn.send(response)
  conn.close()