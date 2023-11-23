import requests
import os

hard_server = os.environ.get('HARD_SERVER', '')

#温度
def get_temperature():
    try:
        response = requests.get("http://"+hard_server + '/wd')
        response.encoding = 'utf-8'
    except:
        response = "出错了，检查主控硬件是否正常"
        return response
    print(response)
    return "ok"

#湿度
def get_humidity():
    try:
        response = requests.get("http://" + hard_server + '/sd')
        response.encoding = 'utf-8'
    except:
        response = "出错了，检查主控硬件是否正常"
        return response
    print(response)
    return "ok"

#光照
def get_light():
    try:
        response = requests.get("http://" + hard_server + '/ld')
        response.encoding = 'utf-8'
    except:
        response = "出错了，检查主控硬件是否正常"
        return response
    print(response)
    return "ok"

#全部
def get_all():
    return "ok"

#用电器开
def one_open():
    try:
        response = requests.get("http://" + hard_server + '/wo')
        response.encoding = 'utf-8'
    except:
        response = "出错了，检查主控硬件是否正常"
        return response
    print(response)
    return "ok"

#用电器关
def one_close():
    try:
        response = requests.get("http://" + hard_server + '/wc')
        response.encoding = 'utf-8'
    except:
        response = "出错了，检查主控硬件是否正常"
        return response
    print(response)
    return "ok"

#灯开
def light_open():
    try:
        response = requests.get("http://" + hard_server + '/kd')
        response.encoding = 'utf-8'
    except:
        response = "出错了，检查主控硬件是否正常"
        return response
    print(response)
    return "ok"

#灯关
def light_close():
    try:
        response = requests.get("http://" + hard_server + '/gd')
        response.encoding = 'utf-8'
    except:
        response = "出错了，检查主控硬件是否正常"
        return response
    print(response)
    return "ok"

def none():
    return "none"
