import requests
from bs4 import BeautifulSoup as bs

page = requests.get(input("url of medium article/page(use quotes): "))
soup = bs(page.text, 'html.parser')

heading = soup.find('h1')
print('\n' + 'ARTICLE: ' + heading.text + '\n')
text_items = soup.find_all('p') #gives a list of all the data/text as well as tags in the <p> tags

for text in text_items:
  if text.contents[0] == 'Written by':
    text.decompose()
  else:
    print(''.join(text.strings) + '\n')
