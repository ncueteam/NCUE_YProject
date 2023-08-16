import network
import savor

async def init_wifi(wlan) -> bool:
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    connected = False
    for ssid, pwd in savor.query_all_accounts().items():
        connected = False
        connected = await connect_wifi(wlan,ssid, pwd)
        if connected: break
    await wifi_status(wlan)

async def connect_wifi(wlan, ssid: str, pwd: str) -> bool:
    try:
        wlan.connect(ssid, pwd)
        return True
    except KeyboardInterrupt:
        return False
    except Exception:
        return False
async def wifi_status(wlan):
    if wlan.active() and wlan.isconnected():
        config = wlan.ifconfig()
        ip_address = config[0]
        subnet_mask = config[1]
        gateway = config[2]
        dns_server = config[3]
        # Print the information
        print("IP Address:", ip_address)
        print("Subnet Mask:", subnet_mask)
        print("Gateway:", gateway)
        print("DNS Server:", dns_server)
    else:
        print("WLAN is not connected.")