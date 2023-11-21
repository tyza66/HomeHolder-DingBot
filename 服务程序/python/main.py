from flask import Flask,request
from ChatHandler import chat

app = Flask(__name__)


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
    # 指定host和port
    app.run(host='0.0.0.0', port=3096)
