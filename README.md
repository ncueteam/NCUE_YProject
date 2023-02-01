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

## 環境安裝

server端 <https://jade-impulse-6f8.notion.site/0f2234d368bb4eac8b94621e89ecebd7>

## 開會紀錄

* 1/13 <https://www.youtube.com/watch?v=kr1WZAYzVcs>
* 2/1 <https://www.youtube.com/watch?v=ESlwJbC6gb0>

## 功能

### esp32端

* 傳統紅外線家電控制
* 傳統開關控制
* 新型MQTT家電控制
* 網路端、家用伺服器端控制
* 控制訊息加密

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
