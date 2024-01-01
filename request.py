import requests 

url = "https://pomofocus.io/"
r = requests.get(url)
print(r.status_code)
print(r.text)