import requests
import os

hard_server = os.environ.get('HARD_SERVER', '')
location_code = os.environ.get('LOCATION_CODE', '')
hefeng_key = os.environ.get('HEFENG_KEY', '')

#温度
def get_temperature():
    try:
        response = requests.get("http://"+hard_server + '/wd')
        response = "当前室内温度为：" + response.text + "℃"
    except:
        response = "出错了，检查主控硬件是否正常"
    return response

#湿度
def get_humidity():
    try:
        response = requests.get("http://" + hard_server + '/sd')
        response = "当前室内湿度为：" + response.text + "（空气电阻）"
    except:
        response = "出错了，检查主控硬件是否正常"
    return response

#光照
def get_light():
    try:
        response = requests.get("http://" + hard_server + '/ld')
        response = "当前室内光照情况为：" + response.text
    except:
        response = "出错了，检查主控硬件是否正常"
    return response

#全部
def get_all():
    try:
        weather = requests.get("https://devapi.qweather.com/v7/weather/now?location="+location_code+"&key="+hefeng_key)
        response = "外界天气信息：" + weather.json()['now']['text'] + "，" + weather.json()['now']['temp'] + "℃，" + \
                   weather.json()['now']['windDir'] + weather.json()['now']['windScale'] + "级  \n"
        response = response + "  \n当前室内温度：" + requests.get("http://" + hard_server + '/wd').text + "℃"
        response = response + "  \n当前室内湿度：" + requests.get("http://" + hard_server + '/sd').text + "（空气电阻）"
        response = response + "  \n当前室内光照：" + requests.get("http://" + hard_server + '/ld').text
    except:
        response = "出错了，检查主控硬件是否正常"
    return response

#用电器开
def one_open():
    try:
        response = requests.get("http://" + hard_server + '/wo')
        response = response.text
    except:
        response = "出错了，检查主控硬件是否正常"
    return response

#用电器关
def one_close():
    try:
        response = requests.get("http://" + hard_server + '/wc')
        response = response.text
    except:
        response = "出错了，检查主控硬件是否正常"
    return response

#灯开
def light_open():
    try:
        requests.get("http://" + hard_server + '/kd')
        response = "灯已开启"
    except:
        response = "出错了，检查主控硬件是否正常"
    return response

#灯关
def light_close():
    try:
        requests.get("http://" + hard_server + '/gd')
        response = "灯已关闭"
    except:
        response = "出错了，检查主控硬件是否正常"
    return response

# 获得当前天气预报
def get_hefeng():
    try:
        response = requests.get("https://devapi.qweather.com/v7/weather/now?location="+location_code+"&key="+hefeng_key)
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
