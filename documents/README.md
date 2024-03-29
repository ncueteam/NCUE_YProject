# NCUE_YProject

畢業專題

## 硬體流程 pseudocode

>
> 從wifi清單中逐一建立連線
> 
> 若無成功連線任何一個
>> 開啟藍芽系統，並等待APP連線
>> 
>> 若APP連上
>> 
>> 等待APP傳送 wifi帳密
>>
>> 關閉藍芽，等待wifi連線 (成功連上則加入清單)，並跳到成功連線的執行區塊
>>
>> 若wifi沒連上
>>
>>> 開啟藍芽，並繼續等待App傳送wifi帳密
> 
> 
> 若是有成功連線
>> 開啟系統
> 
> 
> 

## 相關連結

### APP

> https://github.com/Yunitrish006006/ncue_yproject

### 硬體

> this

## 組員

> S0954005 林昀佑
>
> S0954020 邱靖云
>
> S0861016 王鈺婷
>
> S0954026 李妍瑄
>
> S0954016 戴育琪

## 環境安裝

vscode micropython <https://github.com/pycom/pymakr-vsc/blob/HEAD/GET_STARTED.md>

WSA <https://www.gdaily.org/28643/windows-11-install-google-play>

server端 <https://jade-impulse-6f8.notion.site/0f2234d368bb4eac8b94621e89ecebd7>

## 功能

### esp32端

* 傳統紅外線家電控制
* 傳統開關控制
* 新型MQTT家電控制
* 網路端、家用伺服器端控制
* 控制訊息加密

* 室內

    * 1.空氣監測<br>  
        * 檢測室內空氣<br>
            * DHT11/DHT22溫溼度傳感器(顯示在app上)<br>
            * GP2Y1014空氣顆粒物傳感器/PMS5003ST PM2.5<br>

    * 2.燈光控制(DHT22溫溼度傳感器/BH1750光照強度傳感器)<br>
        * 亮度<br>
            * LED燈泡<br>
        * 氛圍燈<br>
            * WS2812 LED<br>
        * 自動窗簾<br>
            * 舵機/DRV8833電機驅動<br>

    * 3.門窗控制<br>
        * 關窗<br>
            * 舵機/DRV8833電機驅動<br>
            * 雨滴感應器(顯示在app上)<br>
        * NFC門禁<br>
            * RC522<br>

* 室外

    * 1.花卉呵護<br>
        * 自動澆水<br>
            * 電容式土壤濕度傳感器<br>
        * 路燈<br>
            * BH1750光照強度傳感器<br>
            * LED燈泡<br>

    * 2.魚池/魚缸<br>

### 伺服器端

* nothing here

### app 端

* nothing here

## 使用說明

* 將裝置通電
* 連線至裝置
* 以瀏覽器進入下列網址 192.168.4.1
* 修改設定
* 連線至主裝置

## 傳遞格式/協定 (json)

[ 操作碼 ] "code"
>
> 【註冊】"register"
>
> 【修改】"modify"
>
> 【操作】"operate"
>
> 【取消註冊】"unregister"
>
[ ID ] "id"
>
> 除了註冊以外後面都需要有
>
[ 裝置類型 ] "type"
[ 擁有者 ] "owner"
[ 群組 ] "group"

## 範例 1

esp32 ➡️ server

> {
>
>> "code":"register",
>>
>> "data": {
>>
>>> "type":"temperature_sensor",
>>>
>>> "owner":"test_user"
>>
>> }
>>
>
> }

## 範例 2

server ➡️ esp32

> {
>
>> "code":"operate",
>>
>> "data": {
>>>
>>> "type":"air_conditioner",
>>>
>>> "id":"68943d7c-3c45-11ee-be56-0242ac120002",
>>>  
>>> "operation":"temperature_up"
>>>
>> }
>
> }
