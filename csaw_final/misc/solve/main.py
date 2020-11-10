import requests

response = requests.get('http://172.21.0.6/')
print(response.text)
