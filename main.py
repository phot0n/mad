import os,sys
import requests
from bs4 import BeautifulSoup as bs

def scrape(x):
  out_text = []
  text_items = x.find_all('p') #gives a list of all the data/text as well as tags in the <p> tags

  for t in text_items:
    if t.contents[0] == 'Written by':
      t.decompose()
    out_text.append(''.join(t.strings).encode('utf-8'))

  return out_text #returns a list of all the written material of the article


def converter(y,head,subhead):
  with open(os.path.join(root_dir,'articles',head.text + '.md'),'wb') as file:
    file.write(b'># ' + bytes(head.text, 'utf-8') + b'\n\n' + b'>### ' + bytes(subhead.text, 'utf-8') + b'\n\n')
    for i in range (0,len(y)):
      file.write(b'> '+y[i]+b'\n\n')
  print('\nDone')

if __name__ == "__main__":
  page = requests.get(input("url of medium article: "), timeout=None)
  if (page.status_code != 200):
    print("\nInvalid....Exiting")
    sys.exit(0)

  soup = bs(page.text, 'html.parser')
  heading = soup.find('h1')
  subheading = soup.find('h2') #if there's no subheading,gives author's name

  root_dir = os.path.abspath(os.path.dirname(__file__))
  if os.path.exists(os.path.join(root_dir,'articles')):
    converter(scrape(soup),heading,subheading)
  else:
    try:
      os.mkdir(os.path.join(root_dir,'articles'))
    except OSError:
      print("Failed to make directory...exiting")
      sys.exit(0)
    converter(scrape(soup),heading,subheading)