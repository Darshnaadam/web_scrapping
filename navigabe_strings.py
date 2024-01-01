import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
tag = soup.div.p.string # this will only print the string inside the paragraph tag
print(tag)