import base64
import hashlib
import hmac
import os
import requests


def check_sig(timestamp):
    # 配置app_secret
    app_secret = os.environ.get("SECRET", "")
    app_secret_enc = app_secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, app_secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(app_secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = base64.b64encode(hmac_code).decode('utf-8')
    return sign


def send_md_msg(userid, title, message, webhook_url):
    '''
    userid: @用户 钉钉id
    title : 消息标题
    message: 消息主体内容
    webhook_url: 通讯url
    '''
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": message
        },
        '''
        "msgtype": "text",
        "text": {
            "content": message
        },
        '''
        "at": {
            "atUserIds": [
                userid
            ],
        }
    }
    # 利用requests发送post请求
    req = requests.post(webhook_url, json=data)


def replyOne(request_data, reply):
    webhook_url = request_data['sessionWebhook']
    senderid = request_data['senderId']
    # print('***************text_info：', text_info)
    # if判断用户消息触发的关键词，然后返回对应内容
    # python3.10 以上还可以用 switch case...
    title = "状态消息"
    text = reply
    # 调用函数，发送markdown消息
    send_md_msg(senderid, title, text, webhook_url)
    return 'success'
