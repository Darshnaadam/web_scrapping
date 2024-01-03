import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"

r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
price = (soup.find("h4",{"class":"float-end price card-title pull-right"}))
print(price.string)
desc = (soup.find("p",class_ = "description card-text"))
print(desc.string)