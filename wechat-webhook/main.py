from flask import Flask, request
import requests
import json


app = Flask(__name__)


wechat_boot_url=""

def send_wechat(text,time):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    body = {
        "msgtype": "markdown",
        "markdown": {
            "content": "事件内容: " + text + "\n 事件时间: " + time
        }
    }
    requests.post(wechat_boot_url, json.dumps(body), headers=headers)


@app.route('/', methods=['POST'])
def index():
    message = request.data
    message = json.loads(message)
    text = message['text']
    time = message['time']
    send_wechat(text,time)
    return ('This is a website.', 200, None)

if __name__ == '__main__':
    app.run(port=8080,host="0.0.0.0")
