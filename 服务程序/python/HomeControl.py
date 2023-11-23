import requests
import os

hard_server = os.environ.get('HARD_SERVER', '')
location_code = os.environ.get('LOCATION_CODE', '')
hefeng_key = os.environ.get('HEFENG_KEY', '')

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

# 获得当前天气预报
def get_hefeng():
    try:
        response = requests.get("https://devapi.qweather.com/v7/weather/now?location="+location_code+"&key="+hefeng_key)
        print(response.json())
        markdown = "总览信息：" + response.json()['now']['text'] + "，" + response.json()['now']['temp'] + "℃，" + response.json()['now']['windDir'] + response.json()['now']['windScale'] + "级  \n"
        markdown += "体感温度：" + response.json()['now']['feelsLike'] + "℃  \n"
        markdown += "相对湿度：" + response.json()['now']['humidity'] + "%  \n"
        markdown += "能见度：" + response.json()['now']['vis'] + "km  \n"
        markdown += "降水量：" + response.json()['now']['precip'] + "mm  \n"
        markdown += "气压：" + response.json()['now']['pressure'] + "hPa  \n"
        markdown += "云量：" + response.json()['now']['cloud'] + "%  \n"
        response = markdown
    except:
        response = "出错了，检查天气API配置"
        return response
    return response


def none():
    return "none"
