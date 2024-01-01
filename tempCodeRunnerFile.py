import requests
from bs4 import beautifulSoup

url = "https://pomofocus.io/"
r = requests.get(url)
soup = beautifulSoup(r.text,"lxml")
print(soup)