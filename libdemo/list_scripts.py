URL = "http://www.srikanthtechnologies.com"
URL = "https://irctc.co.in"

import requests
from bs4 import BeautifulSoup

resp = requests.get(URL)
soup = BeautifulSoup(resp.text,'html.parser')
script_list = soup.find_all('script')
for script_tag in script_list:
    try:
        print(script_tag['src'])
    except:
        pass


