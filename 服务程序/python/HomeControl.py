import requests
import os

hard_server = os.environ.get('HARD_SERVER', '')

#温度
def get_temperature():
    response = requests.get(hard_server + '/wd')
    response.encoding = 'utf-8'
    print(response.text)
    return "ok"

#湿度
def get_humidity():
    response = requests.get(hard_server + '/sd')
    response.encoding = 'utf-8'
    print(response.text)
    return "ok"

#光照
def get_light():
    response = requests.get(hard_server + '/ld')
    response.encoding = 'utf-8'
    print(response.text)
    return "ok"

#全部
def get_all():
    return "ok"

#用电器开
def one_open():
    response = requests.get(hard_server + '/oneOpen')
    response.encoding = 'utf-8'
    print(response.text)
    return "ok"

#用电器关
def one_close():
    response = requests.get(hard_server + '/oneClose')
    response.encoding = 'utf-8'
    print(response.text)
    return "ok"

#灯开
def light_open():
    response = requests.get(hard_server + '/lightOpen')
    response.encoding = 'utf-8'
    print(response.text)
    return "ok"

#灯关
def light_close():
    response = requests.get(hard_server + '/lightClose')
    response.encoding = 'utf-8'
    print(response.text)
    return "ok"
