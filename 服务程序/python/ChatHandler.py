import json

from DingBot import check_sig,replyOne

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
    reply = erine(chat_info)
    # 发送回复内容
    replyOne(text_info, reply)
    return text_info
