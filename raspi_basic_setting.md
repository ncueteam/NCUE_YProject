# 樹莓派伺服器安裝備忘錄

## 樹莓派基礎設定指令

    sudo raspi-config
>
> 鍵盤修改
>
> ssh啟用
>
> 啟用遠端root-ssh登入
>
> - sudo nano /etc/ssh/sshd_config
>
> - PermitRootLogin xxxxxx -> PermitRootLogin yes
>
> - sudo reboot
>
> 系統風扇啟用
>
> 網路國碼更改
>
> 連上網路
>
> 更新
>
> 安裝python
>
> - sudo apt-get install python
>
> 安裝pip
>
> - sudo apt-get install python3-pip
>

## 固定ip

        sudo nano /etc/dhcpcd.conf

## frpc安裝

### 下載 frpc

        wget https://github.com/fatedier/frp/releases/download/v0.46.0/frp_0.46.0_linux_arm.tar.gz

### 解壓縮

        tar -zxvf frp_0.46.0_linux_arm.tar.gz

### 建立資料夾

        sudo mkdir /var/frpc

### 搬移frpc至/var/frpc

        sudo mv ./frp_0.46.0_linux_arm/* /var/frpc/

### 更改 frpc.ini 成下列配置

        sudo nano /var/frpc/frpc.ini

### 配置 frpc.ini

    [common]
    server_addr = 你的撥接伺服器網址
    server_port = 7000
    token = 你的撥接伺服器網址密碼
    pool_count = 10000
    authentication_method = token

    [rsdpi_ssh_1]
    type = tcp
    local_ip = 127.0.0.1
    local_port = 22
    remote_port = 25522

    [raspi_web_1]
    type = tcp
    local_ip = 127.0.0.1
    local_port = 80
    remote_port = 25580

### 測試

        sudo /var/frpc/frpc -c /var/frpc/frpc.ini

### 將 frpc 註冊成開機自動啟動的服務

        sudo nano /lib/systemd/system/frpc.service

### 配置 frpc.service

        [Unit]
        Description=FRPC
        After=network.target
        Wants=network.target

        [Service]
        Restart=on-failure
        RestartSec=5

        ExecStart=/var/frpc/frpc -c /var/frpc/frpc.ini

        [Install]
        WantedBy=multi-user.target

### 啟動frp

        sudo systemctl enable frpc.service //開機時自動啟動 FRPC服務
        sudo systemctl start frpc.service //啟動 FRPC 服務
        sudo systemctl status frpc.service // 檢查狀態
        sudo systemctl is-failed frpc.service // 查看失敗狀態
        sudo systemctl daemon-reload  // reload 
        sudo reboot // 重開機

## 安裝apache
>
> - sudo apt-get install apache2
>
## 在 /var/www/html 中建立CGI-BIN連結
>
> - sudo nano /etc/apache2/conf-enabled/serve-cgi-bin.conf
>
    <IfModule mod_alias.c>
            <IfModule mod_cgi.c>
                    Define ENABLE_USR_LIB_CGI_BIN
                    Define ENABLE_WWW_CGI_BIN
            </IfModule>

            <IfModule mod_cgid.c>
                    Define ENABLE_USR_LIB_CGI_BIN
                    Define ENABLE_WWW_CGI_BIN
            </IfModule>

            <IfDefine ENABLE_USR_LIB_CGI_BIN>
                    ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
                    <Directory "/usr/lib/cgi-bin">
                            AllowOverride None
                            Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
                            Require all granted
                    </Directory>
            </IfDefine>
            <IfDefine ENABLE_WWW_CGI_BIN>
                    ScriptAlias /cgi-www/ /var/www/html/cgi-bin/
                    <Directory "/var/www/html/cgi-bin">
                            AllowOverride None
                            Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
                            Require all granted
                    </Directory>
            </IfDefine>
    </IfModule>
>
> - cd /etc/apache2/mods-enabled
>
> - sudo ln -s ../mods-available/cgi.load
>
> - sudo service apache2 reload
>