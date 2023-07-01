import uasyncio as asyncio
import network

SSIDs = ["Yunitrish", "c&k", "603", 'V2041']
PWDs = ["0937565253","0423151980", "0937565253", '123456789']


async def connect_wifi(ssid: str, pwd: str) -> bool:
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    try:
        wlan.connect(ssid, pwd)
        await asyncio.sleep_ms(1000)
        return True
    except KeyboardInterrupt:
        return False

async def main():
    # 從wifi清單中逐一建立連線
    if await connect_wifi("Yunitrish", "0937565253"):
        print("success")
    else:
        print("fail")
# 若無成功連線任何一個
# 開啟藍芽系統，並等待APP連線
# 若APP連上
# 等待APP傳送 wifi帳密
# 關閉藍芽，等待wifi連線 (成功連上則加入清單)，並跳到成功連線的執行區塊
# 若wifi沒連上
# 開啟藍芽，並繼續等待App傳送wifi帳密
# 若是有成功連線
# 開啟系統
