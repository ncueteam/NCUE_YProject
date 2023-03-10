# NCUE_YProject

畢業專題

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

## 開會紀錄

* 1/13 <https://youtu.be/ifOYMJg-3Ak>
* 2/1 <https://youtu.be/qnjHYRQzu_k>

## 功能

### esp32端

* 傳統紅外線家電控制
* 傳統開關控制
* 新型MQTT家電控制
* 網路端、家用伺服器端控制
* 控制訊息加密

### esp8266端

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

## 傳遞格式 (json)

### 設定

setting:{
    devicename:"",
    option:"",
    value:"",
    crypto:"",
    date:"",
    user:""
}

### 使用

use:{
    devicename:"",
    option:"",
    value:"",
    crypto:"",
    user:""
}
