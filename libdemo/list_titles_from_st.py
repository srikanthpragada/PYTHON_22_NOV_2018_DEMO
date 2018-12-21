URL = "http://www.srikanthtechnologies.com/rss.xml"

import requests
from bs4 import BeautifulSoup

resp = requests.get(URL)
soup = BeautifulSoup(resp.text,'xml')
items = soup.find_all('item')
for item in items:
    print(item.find('title').text)
    print(item.find('link').text)


