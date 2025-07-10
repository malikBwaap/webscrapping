import requests

res = requests.get('https://www.welcometothejungle.com/en')

print(res)

print(res.content)
