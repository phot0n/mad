import requests
from bs4 import BeautifulSoup as bs

page = requests.get(input("url of medium article/page(use quotes): "))
soup = bs(page.text, 'html.parser')

text_items = soup.find_all('p')

for t in text_items:
  text = t.contents[0]
  print(text)
