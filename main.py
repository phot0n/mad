import requests
from bs4 import BeautifulSoup as bs

def scrap(soup):
  heading = soup.find('h1')
  subheading = soup.find('h2')
  print('\n' + '-->> ' + heading.text + ': ' + subheading.text + '\n')
  text_items = soup.find_all('p') #gives a list of all the data/text as well as tags in the <p> tags

  for t in text_items:
    if t.contents[0] == 'Written by':
      t.decompose()
      print('------end------')
    else:
      print(''.join(t.strings) + '\n')


if __name__ == "__main__":
  page = requests.get(input("url of medium article: "), timeout=None)
  soup = bs(page.text, 'html.parser')

  scrap(soup)