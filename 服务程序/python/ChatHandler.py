import json

from DingBot import check_sig, replyOne
from HomeControl import get_all, get_temperature, get_humidity, get_light, one_open, one_close, light_open, light_close, \
    none, get_hefeng


def get_data(request):
    # 第一步验证：是否是post请求
    if request.method == "POST":
        # print(request.headers)
        # 签名验证 获取headers中的Timestamp和Sign
        timestamp = request.headers.get('Timestamp')
        sign = request.headers.get('Sign')
        # 第二步验证：签名是否有效
        if check_sig(timestamp) == sign:
            # 获取数据 打印出来看看
            text_info = json.loads(str(request.data, 'utf-8'))
            print(text_info)
            print('签名验证通过')
            return text_info
        print('签名验证不通过')
        return str(timestamp)

    return str(request.headers)


def chat(request):
    # 获取数据
    text_info = get_data(request)
    # 获取聊天内容
    chat_info = text_info['text']['content']
    # 控制机器
    reply = message_handler(chat_info)
    # 发送回复内容
    if reply != 'none':
        replyOne(text_info, reply)
    else:
        replyOne(text_info, '喵喵喵？')
    return text_info


def message_handler(message):
    switcher = {
        '当前温度': get_temperature
        , '温度': get_temperature
        , '当前湿度': get_humidity
        , '湿度': get_humidity
        , '当前光照': get_light
        , '光照': get_light
        , '亮度': get_light
        , '播报信息': get_all
        , '开灯': light_open
        , '关灯': light_close
        , '开启设备': one_open
        , '关闭设备': one_close
        , '亮灯': light_open
        , '闭灯': light_close
        , '当前天气': get_hefeng
        , '天气': get_hefeng
        , '播报': get_all
    }
    print(message)
    return switcher.get(message.strip(), none)()
