# playground for
# ffn scraper.py

# import packages
from lxml import html
import requests

# initialize program with fic URL and length
ficUrl = 'https://www.fanfiction.net/s/10847788/'

# create filetree
page = requests.get(ficUrl)
tree = html.fromstring(page.content)

# pull text
page = requests.get(ficUrl)
tree = html.fromstring(page.content)

contents = tree.xpath('//*[@id="storytext"]/p/text() | //*[@id="storytext"]/p/*/text()')
#contents = tree.xpath('//*[@id="storytext"]/p/text()')

print(contents[:10])
