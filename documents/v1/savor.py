import ujson
import os

# 初始化檔案系統
def initialize_filesystem():
    try:
        os.mkdir('/database')
    except OSError as e:
        if e.args[0] != 17:  # 17: EEXIST (File exists)
            raise
# 新增wifi帳密
def add_data(ssid, pwd):
    data = load_data()
    data[ssid] = pwd
    save_data(data)
# 刪除wifi帳密
def remove_data(ssid):
    data = load_data()
    if ssid in data:
        del data[ssid]
        save_data(data)
# 查詢密碼
def get_password(ssid):
    data = load_data()
    return data.get(ssid)
# 查詢 帳號,密碼 對
def query_all_accounts():
    data = load_data()
    return data

def load_data():
    try:
        with open('/database/data.json', 'r') as f:
            return ujson.load(f)
    except OSError as e:
        if e.args[0] == 2:  # 2: ENOENT (No such file or directory)
            return {}
        else:
            raise

def save_data(data):
    with open('/database/data.json', 'w') as f:
        ujson.dump(data, f)


