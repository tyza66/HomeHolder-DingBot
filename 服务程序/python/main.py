from flask import Flask, request
from ChatHandler import chat
from flask_apscheduler import APScheduler
from Schedule import sendAll

app = Flask(__name__)
app.config['SCHEDULER_API_ENABLED'] = True

scheduler = APScheduler()
scheduler.init_app(app)


# 每天早上八点半发送一次
@scheduler.task('cron', id='morning', hour='8', minute='30')
def morning():
    sendAll()

# 每天晚上七点发送一次
@scheduler.task('cron', id='afternoon', hour='19', minute='0')
def afternoon():
    sendAll()


# 测试API
@app.route('/test', methods=["GET"])
def test():
    return '测试成功'


# 聊天API
@app.route('/chat', methods=["POST"])
def chatin():
    chat(request)
    return 'success'


if __name__ == '__main__':
    app.run('0.0.0.0', 3088)
