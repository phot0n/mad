import requests,sys
from bs4 import BeautifulSoup as bs


def scrape(x):
  heading = soup.find('h1')
  subheading = soup.find('h2') #if there's no subheading,gives author's name
  print('\n' + '-->> ' + heading.text + ': ' + subheading.text + '\n')
  text_items = soup.find_all('p') #gives a list of all the data/text as well as tags in the <p> tags

  for t in text_items:
    if t.contents[0] == 'Written by':
      t.decompose()
      print('------end------')
    else:
      out_text = ''.join(t.strings) + '\n'
  
  return out_text

def converter(y):
  pass


if __name__ == "__main__":
  page = requests.get(input("url of medium article: "), timeout=None)
  if (page.status_code != 200):
    print("\nInvalid....Exiting")
    sys.exit(0)

  soup = bs(page.text, 'html.parser')

  scrape(soup)