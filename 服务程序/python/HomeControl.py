import requests
import os

hard_server = os.environ.get('HARD_SERVER', '')

def get_temperature():
    response = requests.get(hard_server + '/wd')
    response.encoding = 'utf-8'
    print(response.text)