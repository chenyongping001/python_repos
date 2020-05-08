import requests
from operator import itemgetter

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
s = requests.session()
s.keep_alive = False
r = requests.get(url)
print('Status code:', r.status_code)