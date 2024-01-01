import requests
from bs4 import BeautifulSoup

url = "https://pomofocus.io/"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
print(soup)