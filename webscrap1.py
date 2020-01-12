import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page.status_code);

#print (page.content);

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

import platform
print('Python Version used',platform.python_version())

ch = list(soup.children)
print('Length of children list',len(ch))

html = ch[2]
print(html)