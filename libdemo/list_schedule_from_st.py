URL = "http://www.srikanthtechnologies.com/schedule.xml"

import requests
from bs4 import BeautifulSoup

resp = requests.get(URL)
soup = BeautifulSoup(resp.text,'xml')
batches = soup.find_all('batch')
for batch in batches:
    print(batch['subject'], batch['stdate'])


