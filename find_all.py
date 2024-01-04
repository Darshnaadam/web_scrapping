import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

price = soup.find_all("h4",class_ = "float-end price card-title pull-right")
print(soup.price)