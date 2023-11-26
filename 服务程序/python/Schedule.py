import os

from HomeControl import get_all
from DingBot import send_md_msg

assess_token = os.environ.get("ASSESS_TOKEN", "")

def start ():
    webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=' + assess_token
    send_md_msg(None, '启动信息', "黑米蜻蜓服务已启动,喵喵喵！", webhook_url)

def sendAll():
    webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=' + assess_token
    send_md_msg(None, '播报信息', get_all(), webhook_url)
