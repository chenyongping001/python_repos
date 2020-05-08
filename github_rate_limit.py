import requests

s = requests.session()
s.keep_alive = False
url = 'https://api.github.com/rate_limit'
r = requests.get(url)
response = r.json()
print(response)